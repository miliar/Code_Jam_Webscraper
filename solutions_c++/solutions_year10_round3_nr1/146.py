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

#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define RREPEAT(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) RREPEAT(i,n-1,0)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define INF (int)1<<30
#define vi vector<int>
#define vs vector<string>
#define pb push_back
#define mkp make_pair
#define ll unsigned long long int
#define uli unsigned long int
#define MAX (int)1e6

using namespace std;

ifstream fin ("A-large10.in");
#define cin fin
ofstream fout ("A-large10.out");
#define cout fout
int n,a[1001],b[1001];
bool intersect(int i, int j) {
	if(a[i]	< a[j] && b[i]<b[j]) return false;
	if(a[i]	> a[j] && b[i]>b[j]) return false;
	return true;
}
int main() {
    int t;
    cin>>t;
    REP(T,t) {
		cin>>n;
		REP(i,n) cin>>a[i]>>b[i];
		int cnt=0;
		REP(i,n) REPEAT(j,i+1,n) if(intersect(i,j)) cnt++;
		cout<<"Case #"<<T+1<<": "<<cnt<<endl; 
    }
    system("pause");
    return 0;
}
