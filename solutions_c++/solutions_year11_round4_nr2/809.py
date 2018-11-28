#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <sys/time.h>
#include <sys/stat.h>
#include <fstream>

using namespace std;

typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
typedef unsigned char BYTE;

#define FOR(i, n) for (int i = 0; i < (n); ++i)
#define FORU(i, s, e) for (int i = (s); i <= (e); ++i)
#define FORD(i, s, e) for (int i = (s); i >= (e); --i)
#define ALL(x) x.begin(),x.end()
#define FOREACH(i, v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)
#define SIZE(x) ((int)x.size())
#define MP make_pair
#define PB push_back
#define BIT(x, b) (((x) >> (b)) & 1)
#define SWAP(a, b, t) do {t = a; a = b; b = t;} while (0);
#define INF 1000000000
#define EPS 1e-9

static inline double getTime () {
   timeval tv;
   gettimeofday(&tv, 0);
   return tv.tv_sec + tv.tv_usec * 1e-6;
}

#define MAXD 50

int w[MAXD][MAXD];
int rsum[MAXD][MAXD][MAXD]; // [row][cstart][cend] (inc)
int csum[MAXD][MAXD][MAXD]; // [col][rstart][rend] (inc)
double rcm[MAXD][MAXD][MAXD]; // [row][cstart][cend] (inc)
double ccm[MAXD][MAXD][MAXD]; // [col][rstart][rend] (inc)
int ssum[MAXD][MAXD][MAXD]; // [row][col][size]
double scc[MAXD][MAXD][MAXD]; // [row][col][size]
double scr[MAXD][MAXD][MAXD]; // [row][col][size]

int main () {
	int T;
	scanf("%d", &T);
	FORU(itr, 1, T) {
		int R, C, D;
		scanf("%d%d%d", &R, &C, &D);
		FOR(i, R) {
			scanf(" ");
			FOR(j, C) {
				char c;
				scanf("%c", &c);
				w[i][j] = c - '0' + D;
			}
		}

//		cerr << "meep1" << endl << flush;

		FOR(r, R)
			FOR(c1, C) {
				rsum[r][c1][c1] = w[r][c1];
				rcm[r][c1][c1] = c1;
				FORU(c2, c1+1, C-1) {
					rsum[r][c1][c2] = rsum[r][c1][c2-1] + w[r][c2];
					rcm[r][c1][c2] = (rcm[r][c1][c2-1] * rsum[r][c1][c2-1] + c2 * w[r][c2]) / rsum[r][c1][c2];
				}
			}

//		cerr << "meep2" << endl << flush;

		FOR(c, C)
			FOR(r1, R) {
//				cerr << c << " " << r1 << endl << flush;
				csum[c][r1][r1] = w[r1][c];
				ccm[c][r1][r1] = r1;
				FORU(r2, r1+1, R-1) {
					csum[c][r1][r2] = csum[c][r1][r2-1] + w[r2][c];
					ccm[c][r1][r2] = (ccm[c][r1][r2-1] * csum[c][r1][r2-1] + r2 * w[r2][c]) / csum[c][r1][r2];
				}
			}

//		cerr << "meep3" << endl << flush;

		FOR(r, R)
			FOR(c, C) {
				ssum[r][c][1] = w[r][c];
				scc[r][c][1] = c;
				scr[r][c][1] = r;
				FORU(d, 2, min(R, C)) {
					ssum[r][c][d] = ssum[r][c][d-1] + csum[c+d-1][r][r+d-1] + rsum[r+d-1][c][c+d-2];
					scc[r][c][d] = (scc[r][c][d-1] * ssum[r][c][d-1] + (c+d-1) * csum[c+d-1][r][r+d-1] + rcm[r+d-1][c][c+d-2] * rsum[r+d-1][c][c+d-2]) / ssum[r][c][d];
					scr[r][c][d] = (scr[r][c][d-1] * ssum[r][c][d-1] + ccm[c+d-1][r][r+d-1] * csum[c+d-1][r][r+d-1] + (r+d-1) * rsum[r+d-1][c][c+d-2]) / ssum[r][c][d];
				}
			}

//		cerr << "meep4" << endl << flush;

		int out = 0;
		FOR(r, R)
			FOR(c, C)
				FORU(d, 3, min(R, C)) {
					int mass = ssum[r][c][d] - (w[r][c] + w[r+d-1][c] + w[r][c+d-1] + w[r+d-1][c+d-1]);
					double cc = (scc[r][c][d] * ssum[r][c][d] - (c * (w[r][c] + w[r+d-1][c]) + (c+d-1) * (w[r][c+d-1] + w[r+d-1][c+d-1]))) / mass;
					double cr = (scr[r][c][d] * ssum[r][c][d] - (r * (w[r][c] + w[r][c+d-1]) + (r+d-1) * (w[r+d-1][c] + w[r+d-1][c+d-1]))) / mass;
					if (abs(cc - .5 * (2*c+d-1)) <= EPS && abs(cr - .5 * (2*r+d-1)) <= EPS) {
						out = max(out, d);
					}
				}

		if (out == 0)
			printf("Case #%d: IMPOSSIBLE\n", itr);
		else
			printf("Case #%d: %d\n", itr, out);
	}
	return 0;
}
