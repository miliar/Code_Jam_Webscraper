#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <ctime>

using namespace std;

#define Nul(a) memset(a, 0, sizeof(a))
#define Fil(a, b) memset(a, b, sizeof(a))
#define Size(a) ((int)a.size())
const int maxa = 100, maxb = 400;
string l[30][30][maxa + maxb + 10];
char a[30][30];
struct SPos {
	int i, j, v;
	void Init(int ii, int jj, int vv) {
		i = ii;
		j = jj;
		v = vv;
	}
} s[30 * 30 * (maxa + maxb) + 1 + 1000];
int di[4] = {-1, 1, 0, 0};
int dj[4] = {0, 0, -1, 1};
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		printf("Case #%d:\n", ti);
		Fil(l, 0);
		int n, m;
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%s", a[i]);
		}
		int u = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (a[i][j] <= '9' && a[i][j] >= '0') {
					l[i][j][a[i][j] - '0' + maxa] = a[i][j];
					s[u++].Init(i, j, a[i][j] - '0');
				}
			}
		}
		for (SPos *p = s; p < s + u; p++) {
			int i = p->i, j = p->j, v = p->v;
			for (int d1 = 0; d1 < 4; d1++) {
				int r1 = i + di[d1], c1 = j + dj[d1];
				char c = a[r1][c1];
				if (r1 >= 0 && c1 >= 0 && r1 < n && c1 < n) {
					for (int d2 = 0; d2 < 4; d2++) {
						int r2 = r1 + di[d2], c2 = c1 + dj[d2];
						if (r2 >= 0 && c2 >= 0 && r2 < n && c2 < n) {
							int cv = v;
							if (c == '+') {
								cv += a[r2][c2] - '0';
							} else {
								cv -= a[r2][c2] - '0';
							}
							if (cv < -maxa || cv > maxb) continue;
							string ss = (l[i][j][v + maxa] + c) + a[r2][c2];
							if (!l[r2][c2][cv + maxa].length()) {
								s[u++].Init(r2, c2, cv);
								l[r2][c2][cv + maxa] = ss;
							} else if (l[r2][c2][cv + maxa].length() == ss.length() && ss.compare(l[r2][c2][cv + maxa]) < 0) {
								l[r2][c2][cv + maxa] = ss;
							}
						}
					}
				}
			}
		}
		for (int i = 0; i < m; i++) {
			int t;
			scanf("%d", &t); t += maxa;
			string best;
			for (int j = 0; j < n; j++) {
				for (int k = 0 ; k < n; k++) {
					if (l[j][k][t].length()) {
						if (!best.length() || l[j][k][t].length() < best.length() || l[j][k][t].length() == best.length() && l[j][k][t].compare(best) < 0) {
							best = l[j][k][t];
						}
					}
				}
			}
			printf("%s\n", best.c_str());
		}
	}
//#ifdef pperm
//	printf("%.3lf", clock() * 1e-3);
//#endif
	return 0;
}
