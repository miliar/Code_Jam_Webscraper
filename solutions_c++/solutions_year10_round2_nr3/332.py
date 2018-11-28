// By mirosuaf v.2.1 modified for CodeJam
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(f,w) ({ bool _ok=true; f _ok=_ok && (w); _ok; })
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 

int SR = 600;
int main() {
	int ile;
	scanf("%d",&ile);

	int tab[SR*3][SR*3]; REP(i, SR*3) REP(j, SR*3) tab[i][j] = 0;
	int result[SR]; REP(i, SR) result[i] = 0;
	REP(i, 600) tab[SR+0][SR+i] = 1;
	REP(i, 600) tab[SR+i][SR+0] = 0;

	REP(n, 600) REP(m, 600) {
		FOR(k, 1, m) {
			tab[SR+n][SR+m]+=tab[SR+n-k][SR+m];
			tab[SR+n][SR+m]%=100003;
		}
	}
	FOR(kk, 1, 500) {
	int wynik=0;
	REP(k, kk+1) {
		wynik+=tab[SR+kk-k][SR+0+k];
		wynik%=100003;
	}
	result[kk] = wynik;
	}
	FOR(iile,1,ile) {
		int n;
		scanf("%d",&n);
		printf("Case #%d: %d\n",iile, result[n-1]);
	}
	return 0;
}

