#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
#include <cstring>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) ((int)(x).size())

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

int R, C, D;

ll w[510][510];
ll acum[510][510];
ll horiz[510][510];
ll vert[510][510];

int main() {
	int casos;
	scanf("%d", &casos);
	REP(caso, casos) {
		scanf("%d %d %d\n", &R, &C, &D);
		REP(r, R) {
			REP(c, C) {
				scanf("%c", &w[r+1][c+1]);
				w[r+1][c+1] -= '0';
			}
			scanf("\n");
		}
		acum[0][0] = horiz[0][0] = vert[0][0] = 0;
		for (int r = 1; r <= R; r++) acum[r][0] = horiz[r][0] = vert[r][0] = 0;
		for (int c = 1; c <= C; c++) acum[0][c] = horiz[0][c] = vert[0][c] = 0;
		for (int r = 1; r <= R; r++) {
			for (int c = 1; c <= C; c++) {
				acum[r][c] = w[r][c] + acum[r][c-1] + acum[r-1][c] - acum[r-1][c-1];
				horiz[r][c] = r*w[r][c] + horiz[r][c-1] + horiz[r-1][c] - horiz[r-1][c-1];
				vert[r][c] = c*w[r][c] + vert[r][c-1] + vert[r-1][c] - vert[r-1][c-1];
				//printf("%d %d %I64d\n", r, c, vert[r][c]);
			}
		}
		int best = -1;
		for (int r = 1; r <= R; r++) {
			for (int c = 1; c <= C; c++) {
				for (int k = max(3,best); r+k-1 <= R && c+k-1 <= C; k++) {
					ll dx = 0, dy = 0;
					
					dx = horiz[r+k-1][c+k-1] + horiz[r-1][c-1] - horiz[r+k-1][c-1] - horiz[r-1][c+k-1];
					dx -=  (r+r+k-1)/2*(acum[r+k-1][c+k-1] + acum[r-1][c-1] - acum[r+k-1][c-1] - acum[r-1][c+k-1]);
					if (k % 2 == 0) {
						dx -= (acum[r+k/2-1][c+k-1] + acum[r-1][c-1] - acum[r+k/2-1][c-1] - acum[r-1][c+k-1]);
					}
					dx += w[r][c] * (k/2);
					dx += w[r][c+k-1] * (k/2);
					dx -= w[r+k-1][c] * (k/2);
					dx -= w[r+k-1][c+k-1] * (k/2);

					dy = vert[r+k-1][c+k-1] + vert[r-1][c-1] - vert[r+k-1][c-1] - vert[r-1][c+k-1];
					/*if (r == 2 && c == 2 && k == 4) {
						printf("%I64d %I64d\n", dx, dy);
						printf( "%d\n", (r+r+k)/2);
					}*/
					dy -= (c+c+k-1)/2*(acum[r+k-1][c+k-1] + acum[r-1][c-1] - acum[r+k-1][c-1] - acum[r-1][c+k-1]);
					/*if (r == 2 && c == 2 && k == 4) {
						printf("%I64d %I64d\n", dx, dy);
						printf( "%d\n", (r+r+k)/2);
					}*/
					if (k % 2 == 0) {
						dy -= (acum[r+k-1][c+k/2-1] + acum[r-1][c-1] - acum[r+k-1][c-1] - acum[r-1][c+k/2-1]);
					}
					/*if (r == 2 && c == 2 && k == 4) {
						printf("%I64d %I64d\n", dx, dy);
						printf( "%d\n", (r+r+k)/2);
					}*/
					dy += w[r][c] * (k/2);
					dy -= w[r][c+k-1] * (k/2);
					dy += w[r+k-1][c] * (k/2);
					dy -= w[r+k-1][c+k-1] * (k/2);
					
					
					if (dx == 0 && dy == 0) best = max(best, k);
				}
			}
		}
		if (best == -1) {
			printf("Case #%d: IMPOSSIBLE\n", caso+1);
		} else {
			printf("Case #%d: %d\n", caso+1, best);
		}
		//cout << "Case #" << caso+1 << ": " << (b%2?"BLACK":"WHITE") << endl;
	}
	return 0;
}
