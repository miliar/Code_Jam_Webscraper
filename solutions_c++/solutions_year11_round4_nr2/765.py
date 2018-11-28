
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>

#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

#define forn(i, n) for (i = 0; i < (int)(n); ++i)
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> vi;

const int maxr = 500 + 100;

int w[maxr][maxr];

struct point {
	double x, y;
	point () {}
	point (double _x, double _y): x(_x), y(_y) {}
};

point operator - (const point & a, const point & b)
{
	return point(a.x - b.x, a.y - b.y);
}

point operator + (const point & a, const point & b)
{
	return point(a.x + b.x, a.y + b.y);
}

point operator * (const point & a , const double w)
{
	return point(a.x*w, a.y*w);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T, it;
	//cin >> T;
	scanf("%d\n", &T);
	forn(it, T) {
		printf("Case #%d: ", it + 1);

		int r, c, d, i, j;
		//cin >> r >> c >> d;
		scanf("%d%d%d\n", &r, &c, &d);
		forn(i, r) {
			char buf[500 + 55];
			gets(buf);
			forn(j, c) {
				//cin >> w[i][j];
				w[i][j] = buf[j] - '0';
				w[i][j] += d;
			}
		}

		int mxk = min(r, c), k;
		int ok = 0;
		int ii, jj;
		for (k = mxk; k >= 3; --k) {
			forn(i, r - k + 1) {
				forn(j, c - k + 1) {
					point cc(k / 2.0, k / 2.0); 
					point res(0, 0);
					forn(ii, k) {
						forn(jj, k) {
							if (ii == 0 && (jj == 0 || jj == k - 1) || ii == k - 1 && (jj == 0 || jj == k - 1))
								continue;
							point p(0.5 + ii, 0.5 + jj);
							point ff = ((p - cc)*w[ii + i][jj + j]);
							res.x += ff.x;
							res.y += ff.y;
						}
					}
					if (abs(res.x) < 1e-10 && abs(res.y) < 1e-10) {printf("%d\n", k); ok = 1; break;}
				}
				if (ok)
					break;
			}
			if (ok)
				break;
		}
		if (!ok)
			puts("IMPOSSIBLE");
	}




	return 0;
}
