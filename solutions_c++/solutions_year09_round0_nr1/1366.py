#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int t;scanf(" %d",&t);t;})
#define GC(x) scanf(" %c",&x)
#define sz size()
#define rz resize
#define inf 1e9
#define pb push_back

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef double DD;
typedef long long LL;

int L,D,N;
VS dict,test;
string T;

int rec() {
	int t=0,k=0;
	REP (i,dict.sz) {
		k=0;
		REP (j,dict[i].sz)
			if(!binary_search(test[j].begin(), test[j].end(),dict[i][j])) {k=1; break;}
		if(k==0) t++;
	}
	return t;
}

int main() {
	char x;
	L=GI;
	D=GI;
	N=GI;
	dict.rz(D);
	REP (i,D) cin>>dict[i];
	sort(dict.begin(), dict.end());
	REP (i,N) {
		test.clear();
		test.rz(L);
		REP (j,L) {
			GC(x);
			if(x=='(') {
				while(1) {
					GC(x);
					if(x==')') break;
					test[j].pb(x);
				}
			}
			else test[j].pb(x);
			sort(test[j].begin(), test[j].end());
		}
//		REP (j,L) cout<<test[j]<<endl;
		printf("Case #%d: %d\n",i+1,rec());
	}
	return 0;
}

/*
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc
*/

