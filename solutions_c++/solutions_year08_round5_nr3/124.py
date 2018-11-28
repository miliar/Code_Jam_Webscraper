#include <cstdio>
#include <iostream>
using namespace std;
const int mx=13;

int f[mx][3000], g[mx];
int ts, o, n, m, b[mx], i, x, x2, j;
char ch;

int chck(int x, int o) {
	return !x & b[o];
}

int fnd(int x) {
	for (int i=0; i<m-1; i++)
	if (chck(x, i) && chck(x, i+1)) return 0;
	return 1;
}
int lf(int x, int x2) {
	for (int i=0; i<m; i++){
	   if (i<m-1 && chck(x,i) && chck(x2, i+1)) return 0;
	   if (i>0 && chck(x,i) && chck(x2, i-1)) return 0;
	}
	return 1;
}

main() {
    freopen("1.in", "r", stdin);
    freopen("2.out", "w", stdout);
     
    b[0] = 1;
	for (i=1; i<=11; i++)
		b[i] = b[i-1]<<1;
    for (cin >> ts; ++o <= ts;) {
        cin >> n >> m;
		for (i=1; i<=n; i++){
			g[i] = 0;
			for (j=1; j<=m; j++) {
                cin >> ch;
				g[i] = g[i]<<1;
				if (ch=='x') g[i] += 1;
			}
		}
		memset(f, 0, sizeof(f));
		for (x=0; x<(1<<m); x++)
		if (!(x&g[1]) && fnd(x)){
			f[1][x] = __builtin_popcount(x);
		}

		for (i=2; i<=n; i++)
		for (x=0; x<(1<<m); x++)
            if (!(x&g[i]) && fnd(x)) 
		for (x2=0; x2<(1<<m); x2++)
            if (!(x2&g[i-1]) && fnd(x2))
		if (lf(x, x2))
		  f[i][x] >?= f[i-1][x2] + __builtin_popcount(x);

		int ret=0;
		for (x=0; x<(1<<m); x++)
			ret >?= f[n][x];
		cout << "Case #" << o << ": " << o << ' ' << ret;
	}
}
