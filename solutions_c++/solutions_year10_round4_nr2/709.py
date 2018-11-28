#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define RFOR(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,n) FOR(i,0,n)
#define RREP(i,n) RFOR(i,n-1,0)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define INF (int)1<<30
#define vi vector<int>
#define vs vector<string>
#define pb push_back
#define mkp make_pair
#define ll long long int
#define uli unsigned long long int
#define MAX (int)1e6

using namespace std;

ifstream fin ("B-small-attempt0.in");
#define cin fin
ofstream fout ("B-small.out");
#define cout fout

#define LEFT(i) (1<<(i))
#define RIGHT(i) ((1<<(i)) + 1)
#define PARENT(i) ((i)>>1)
void process(int i, int k, int a[20000],int n, int match[100000]) {
	if(k<1) return;
	process(i,PARENT(k),a,n,match);
	if(a[i]<n) {
		a[i]++;
		match[k]=1;
	}
	return;
}
int main() {
	int t=0;
	cin>>t;
	REP(T,t) {
		int n,a[20000],cost=0,match[100000];
		REP(i,100000) match[i]=0;
		cin>>n;
		RREP(k,n+1)
			REP(i,1<<k) {
				if(k==n) {
					cin>>a[i];
				}
				else cin>>cost;
			}
		REP(i,1<<n) {
			int k=(1<<n)+ i;
			process(i,k,a,n,match);

		}
		int cnt=0;
		REP(i,1<<n) cnt+=match[i];
		cout<<"Case #"<<T+1<<": "<<cnt*cost<<endl;
	}
	return 0;
}
