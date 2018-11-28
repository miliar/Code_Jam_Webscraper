#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <utility>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define _foreach(it, b, e) for (typeof(b) it = (b); it != (e); ++it)
#define foreach(x...) _foreach(x)
#define rep(i, n) foreach(i, 0, n)

#define MSET(c, v) memset(c, v, sizeof(c))

const int INF = 0x3f3f3f3f; const int NEGINF = 0xC0C0C0C0;
const int NULO = -1;
double EPS = 1.e-10;

inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

int bact[200][200][2];

int main() {
	TRACE(setbuf(stdout, NULL));
	int _42;
	scanf("%d", &_42);
	rep(_41, _42) {
		printf("Case #%d:", _41+1);
		MSET(bact, 0);
		int R;
		scanf("%d", &R);
		rep(i, R) {
			int X1, X2, Y1, Y2;
			scanf("%d %d %d %d", &X1, &Y1, &X2, &Y2);
			int Xm = min(X1, X2), XM = max(X1, X2);
			int Ym = min(Y1, Y2), YM = max(Y1, Y2);
			foreach(i, Xm, XM+1) foreach(j, Ym, YM+1) bact[i][j][0] = 1;
		}
		int ans = 0;
		int conta = 0;
		rep(i, 200) rep(j, 200) conta += bact[i][j][0];
		int atu = 0;
		int outro = 1;
		while (conta > 0) {
			ans++;
			WATCH(ans);
			WATCH(conta);
			conta = 0;
			rep(i, 200) rep(j, 200) {
				if (i == 0 || j == 0) {
					bact[i][j][outro] = 0;
					continue;
				}
				if (bact[i][j][atu]) {
					if (bact[i-1][j][atu] || bact[i][j-1][atu]) {
						bact[i][j][outro] = 1;
						conta++;
					} else
						bact[i][j][outro] = 0;
				} else {
					if (bact[i-1][j][atu] && bact[i][j-1][atu]) {
						bact[i][j][outro] = 1;
						conta++;
					} else
						bact[i][j][outro] = 0;
				}
			}
			atu = 1-atu;
			outro = 1-outro;
		}
		printf(" %d\n", ans);
	}
	return 0;
}
