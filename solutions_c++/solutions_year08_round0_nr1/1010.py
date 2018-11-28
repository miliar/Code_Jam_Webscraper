#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <list>
#include <deque>
#include <stack>
#include <sstream>
#include <fstream>

#define ll long long int
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define RFOR(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define RREP(i,n) RFOR(i,0,n)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define V(x) vector< x >
#define vi V(int)
#define vs V(string)
#define pb push_back
#define mkp make_pair
#define PII pair <int,int>
#define uli unsigned long long int
#define GI ({int t;scanf("%d",&t);t;})
const int INF = (int)1<<30;

using namespace std;

int main() {	int t=GI;
	REP(T,t) {
		int n=GI;
		set<string> st,Q;
		char c[10000];
		REP(i,n) getchar(),scanf("%[^\n]",c),st.insert((string)c);
		int q=GI,cnt=0;
		REP(i,q) {
			getchar(),scanf("%[^\n]",c);
			if(st.count((string)c)) Q.insert((string)c);
			if(Q.size()==n) {
				cnt++;
				Q.clear();
				Q.insert(c);
			}
		}
		cout<<"Case #"<<T+1<<": "<<cnt<<endl;
	}
	return 0;
}
