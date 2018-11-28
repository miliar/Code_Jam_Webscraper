#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
using namespace std;

#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>

int cond = (ll)1;
#define db(x) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }

int X[60], Y[60], R[60];

ld dyst(int i, int j) {
	ld dx = X[i] - X[j];
	ld dy = Y[i] - Y[j];
	db(dx<<" "<<dy);
	return sqrt(dx * dx + dy * dy);
}

ld solve() {
	int N;
	scanf("%d", &N);
	rep (i, N) {
		scanf("%d%d%d", &X[i], &Y[i], &R[i]);
	}
	if (N == 1) {
		R[1] = R[0];
		X[1] = X[0]; Y[1] = Y[0]; N++;
	}
	if (N == 2) {
		R[2] = R[0];
		X[2] = X[0]; Y[2] = Y[0]; N++;
	}
	ld wynik = (ld)1e9;
	rep (i, 1<<3) {
		vi z1, z2;
		rep (j, 3) if ((1<<j)&i) z1.pb(j); else z2.pb(j);
		if (z1.size() == 1) {
			ld reszta = (R[z2[0]] + R[z2[1]] + dyst(z2[0], z2[1])) / 2;
			wynik = min(wynik, max((ld)R[z1[0]], reszta));
		}
	}
	return wynik;
}

int main(int argc, char ** argv) {
    ios::sync_with_stdio(false);
    cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
    int t;
    scanf("%d", &t);
    fo (i, 1, t) {
	    printf("Case #%d: ", i);
	    ld wynik = solve();
	    printf("%.9lf", (double)wynik);
	    printf("\n");
    }
    return 0;
}

