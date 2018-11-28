#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <string>
#include <queue>
#include <ext/hash_map>
#include <ext/hash_set>
#include <ext/slist>

using namespace __gnu_cxx;
using namespace std;
typedef pair<int,int> PI;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;

#define REP(i,n)	for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,s,k)	for(int i=(s),_k=(k);i<=_k;++i)
#define FORD(i,s,k)	for(int i=(s),_k=(k);i>=_k;--i)
#define FORE(it,q)	for(__typeof((q).begin()) it=(q).begin();it!=(q).end();++it)
#define FORED(it,q) for(__typeof((q).rbegin())it=(q).rbegin();it!=(q).rend();++it)
#define SIZE(x)     x.size()
#define ALL(v)      v.begin(),v.end()
#define SE          second
#define FI          first
#define pb          push_back
#define pf          push_front
#define mp	    	make_pair
map<string,int> Col;
vector<PI> V[310];

struct Z {
	int a,b,c;
	Z() {}
	Z(int a,int b,int c) : a(a),b(b),c(c){}
	bool operator<(const Z& z) const {
		if(a==z.a) {
			if(b==z.b) return c<z.c;
			return b<z.b;
		}
		return a<z.a;
	}
};

vector<Z> W;
int dyn[10001][300][3];
int dyn2[10001][300][4];
	
void testcase() {
	int n;
	int a,b,cnt=0,c;
	char cstr[20];
	Col.clear();
	REP(i,300) V[i].clear();
	W.clear();
	scanf("%d",&n);
	REP(i,n) {
		scanf("%s%d%d",cstr,&a,&b);
		if(Col.find(string(cstr)) == Col.end()) {
			c = cnt;
			Col[string(cstr)] = cnt++;
		} else {
			c = Col[string(cstr)];
		}
		V[c].pb(mp(a,b));
//		W.pb(Z(a,b,c));
	}
	/*
	REP(i,10001) REP(j,cnt) {
		REP(k,3) dyn[i][j][k] = dyn2[i][j][k] = 1000000;
		dyn2[i][j][3] = 1000000;
	}
	
	int mn[4],mn2[4];
	FORE(it,W) {
		REP(k,4) mn[k] = mn2[k] = 1000000;
		FOR(i,it->a-1,it->b-1) {
			REP(k,3) mn[k] = min(mn[k],dyn[i][it->c][k]);
			REP(k,4) mn2[k] = min(mn2[k],dyn[i][it->c][k]);
		}
		FOR(k,1,3)
			dyn2[it->b][it->c][k] = min(dyn[it->b][it->c][k], min(mn[k-1],mn2[k]) + 1);
			
		REP(c,cnt) FOR(k,0,2)
			dyn[it->b][c][k] = 
	}*/
	
	REP(i,cnt) sort(ALL(V[i]));
	vector<PI> R;
	int dyn[10001],res=1000000;
	REP(a,cnt) FOR(b,a,cnt-1) FOR(c,a,cnt-1) {
		R.clear();
		FORE(it,V[a]) R.pb(*it);
		if(b != a) FORE(it,V[b]) R.pb(*it);
		if(c != b) FORE(it,V[c]) R.pb(*it);
		sort(ALL(R));
		REP(i,10001) dyn[i] = 1000000;
		dyn[0] = 0;
		int mn;
		FORE(it,R) {
			mn = 1000000;
			FOR(j,it->FI-1,it->SE-1) mn = min(mn,dyn[j]);
			dyn[it->SE] = min(dyn[it->SE],1 + mn);
		}
		res = min(res,dyn[10000]);
	}
	if(res >= 1000000) printf("IMPOSSIBLE\n");
	else printf("%d\n", res);
	
	/*
	REP(i,cnt) {
		printf("%d: ", i);
		FORE(it,V[i]) printf("%d %d\n", it->FI, it->SE);
		
	}*/
	// [n][x] - pomalowane [1..n], kolorow uzytych x
	
	/*
	int dyn[10100][4][2];
	
	REP(i,10001) REP(j,4) REP(k,2) dyn[i][j][k] = 1000000;
	REP(j,4) REP(k,2) dyn[0][j][k] = 0;
	REP(i,cnt) {
		REP(j,10001) REP(k,4) {
			dyn[j][k][0] = min(dyn[j][k][0],dyn[j][k][1]);
			dyn[j][k][1] = 1000000;
		}
		REP(j,SIZE(V[i])) {
			int mn[4][2];
			REP(a,4) REP(b,2) mn[a][b] = 1000000;
			FOR(s,V[i][j].FI-1,V[i][j].SE-1) {
				REP(k,4) REP(j,2)
					mn[k][j] = min(mn[k][j],dyn[s][k][j]);
			}
			FOR(k,1,3) {
				dyn[V[i][j].SE][k][1] = min(dyn[V[i][j].SE][k][1], 1 + min(mn[k-1][0],mn[k][1]));
			}
		}
	}
	int res = 1000000;
	REP(k,4) {
		res = min(res, dyn[10000][k][0]);
		res = min(res, dyn[10000][k][1]);
	}
	if(res == 1000000) printf("IMPOSSIBLE\n");
	else printf("%d\n", res);*/
}


int main()
{
	int T;
	scanf("%d",&T);
	FOR(cs,1,T) {
		printf("Case #%d: ", cs);
		testcase();
	}
}

