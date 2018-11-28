#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <map>
#include <set>
#include <functional>
#include <algorithm>

using namespace std;

#define	PI	3.14159265358979323846

int main(int argc, char *argv[])
{
	int nc, ci;
	int i, j, k, n;
	static char c[1024][1024], d[1024][1024];
	
	scanf("%d", &nc);
	for (ci = 1; ci <= nc; ci++) {
		scanf("%d", &n);
		int x1, y1, x2, y2;
		memset(c, 0, sizeof(c));
		int sx = 0x7FFFFFFF, ex = 0, sy = 0x7FFFFFFF, ey = 0;
		for (k = 0; k < n; k++) {
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for (i = x1; i <= x2; i++)
				for (j = y1; j <= y2; j++)
					c[i][j] = 1;
			sx = min(sx, x1);
			ex = max(ex, x2);
			sy = min(sy, y1);
			ey = max(ey, y2);
		}
		
		// printf("%d %d %d %d\n", sx, ex, sy, ey);
		
		for (k = 0; ; k++) {
			memcpy(d, c, sizeof(c));
			int count = 0;
			for (i = sx; i <= ex; i++)
				for (j = sy; j <= ey; j++) {
					if (c[i][j]) {
						count++;
						if ((i == 0 || c[i-1][j] == 0) && (j == 0 || c[i][j-1] == 0))
							d[i][j] = 0;
					} else {
						if (i > 0 && c[i-1][j] && j > 0 && c[i][j-1])
							d[i][j] = 1;
					}
				}
			if (count == 0) break;
			memcpy(c, d, sizeof(c));
		}


		printf("Case #%d: %d\n", ci, k);
	}

	return 0;
}
