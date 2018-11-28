#include <string>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define MP make_pair
#define ST first
#define ND second

typedef long long LL; typedef pair<LL,LL> PLL;
const int INF = 1000000000;
inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

int N,K,B,T;
LL X[64];
LL V[64];
LL F[64];
int penalty[64];
int lewat[64][64];

int solve(int idx,int mask) {

	if(idx==N) {
		int ctr = 0;
		REP(i,N) if(mask & (1<<i)) ctr++;

		if(ctr>=K) {
			int ret = 0;
			REP(i,N) if(mask & (1<<i)) ret += penalty[i];
			return ret;
		}
		return INF;
	}

	// tidak ambil
	int ret = solve( idx+1, mask );

	if( F[idx] >= B ) {
		// ambil
		int v = solve( idx+1, mask | (1<<idx) );
		ret = min( ret, v );
	}

	return ret;
}

int main() {
	OPEN("b");
	REP(ncase,getint()) {
		N=getint();
		K=getint();
		B=getint();
		T=getint();
		REP(i,N) F[i] = X[i]=getint();
		REP(i,N) V[i]=getint();
		REP(i,N) REP(j,N) lewat[i][j]=0;
		REP(i,N) F[i] = X[i] + LL(T) * V[i];
		// cout << "B = " << B << endl;
		// REP(i,N) cout << F[i] << endl;
		REP(i,N) if( F[i] >= B ) {
			penalty[i] = 0;
			FOR(j,i+1,N-1) if( F[j] < B ) penalty[i]++;
		}

/*
		REP(loop,T) {
			REP(i,N) F[i] += V[i];
			REP(i,N) {
				FOR(j,i+1,N-1) if( F[i] > F[j] ) lewat[i][j] = 1;
			}
		}

		REP(i,N) {
			penalty[i] = 0;
			REP(j,N) penalty[i] += lewat[i][j];
		}
*/

		PLL data[64];
		REP(i,N) data[i] = MP( penalty[i], F[i] );
		sort( data, data + N );
		int take = 0;
		// int ans = solve(0,0);
		int ans = 0;
		REP(i,N) {
			if(take==K) continue;
			if( data[i].ND < LL(B)) continue;
			take++;
			ans += data[i].ST;
		}

		if(take<K) printf("Case #%d: IMPOSSIBLE\n",ncase+1);
		else printf("Case #%d: %d\n",ncase+1,ans);
	}
	return 0;
}
