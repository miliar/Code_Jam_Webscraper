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
using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << endl)

#define a(v) (v).begin(), (v).end()
#define ra(v) (v).rbegin(), (v).rend()
#define _foreach(it, b, e) for (typeof(b) it = (b); it != (e); ++it)
#define foreach(x...) _foreach(x)
#define rep(i, n) foreach(i, 0, n)

#define MSET(c, v) memset(c, v, sizeof(c))

const  int INF = 0x3f3f3f3fLL; const int NEGINF = 0xC0C0C0C0;
const int NULO = -1;
double EPS = 1.e-10;

inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}
int canmiss[1200];
 int price[15][1200];
 int PD[15][1200][15];
int main() {
	TRACE(setbuf(stdout, NULL));
	int _42;
	scanf("%d", &_42);
	rep(_41, _42) {
		printf("Case #%d:", _41+1);
		int P;
		scanf("%d", &P);
		rep(i, 1<<P) scanf("%d", &canmiss[i]);
		rep(i, P) {
			rep(j, 1<<(P-i-1)) scanf("%d", &price[i][j]);
		}
		MSET(PD, INF);
		rep(j, 1 << P) {
			rep(k, canmiss[j]+1) PD[0][j][k] = 0;
		}
		foreach(i, 1, P+1) rep(j, 1<<(P-i)) rep(k, P-i+2) {
			// dont buy
			int ans1 = PD[i-1][2*j][k+1] + PD[i-1][2*j+1][k+1];
			// buy
			int ans2 = PD[i-1][2*j][k] + PD[i-1][2*j+1][k] + price[i-1][j];
			if (PD[i-1][2*j][k] == INF || PD[i-1][2*j+1][k] == INF)
				ans2 = INF;
			PD[i][j][k] = min(ans1, ans2);
		}
		printf(" %d\n", PD[P][0][0]);
	}
	return 0;
}
