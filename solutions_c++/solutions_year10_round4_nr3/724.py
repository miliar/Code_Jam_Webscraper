#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>

#define rep(i, n) repb(i, 0, n)
#define repb(i, b, n) repbc(i, b, n, <)
#define repe(i, n) repbe(i, 0, n)
#define repbe(i, b, n) repbc(i, b, n, <=)
#define repbc(i, b, n, c) for(int i = b; i c n; i++)

using namespace std;

int main()
{
	int C, R, x1, x2, y1, y2, mx = 0, my = 0, minx, miny, m[2][110][110], res;
	scanf("%i", &C);
	rep(t, C) {
		mx = my = res = 0;
		minx = 999;
		miny = 999;
		memset(m, 0, sizeof(m));
		scanf("%i", &R);
		rep(r, R) {
			scanf("%i %i %i %i\n", &x1, &y1, &x2, &y2);
			repbe(i, x1, x2) {
				repbe(j, y1, y2) {
					m[0][i][j] = 1;
				}
			}
			minx = min(minx, x1);
			mx = max(mx, x2);
			miny = min(miny, y1);
			my = max(my, y2);
		}
		//printf("(mx, my) = (%i, %i)\n", mx, my);
		for(res = 0;; res++) {
			bool cont = false;
			repbe(i, minx, mx) {
				repbe(j, miny, my) {
					//printf("(i, j, m): (%i, %i, %i)\n", i, j, m[res%2][i][j]);
					if(m[res%2][i][j]) {
						if(!m[res%2][i - 1][j] && !m[res%2][i][j - 1]) {
							m[!(res%2)][i][j] = 0;
						} else {
							m[!(res%2)][i][j] = 1;
							cont = true;
						}
					} else {
						if(m[res%2][i - 1][j] && m[res%2][i][j - 1]) {
							m[!(res%2)][i][j] = 1;
							cont = true;
						} else {
							m[!(res%2)][i][j] = 0;
						}
					}
				}
			}
			if(!cont) break;
		}
		printf("Case #%i: %i\n", t + 1, res + 1);
	}
	
  return 0;
}
