#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

int cur[1000][1000], last[1000][1000];
int r, x1, x2, y1, y2;


int main() {
	int ca, cases = 0;
	int i, j, k;
	scanf("%d", &ca);
	while (ca--) {
		printf("Case #%d: ", ++cases);
		scanf("%d", &r);
		memset(cur, 0, sizeof(cur));
		int maxx = 0;
		int maxy = 0;
        for (i = 0; i < r; ++i) {
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            if (x1 > x2) swap(x1, x2);
            if (y1 > y2) swap(y1, y2);
            for (j = x1; j <= x2; ++j) {
                for (k = y1; k<= y2; ++k) {
                    cur[j][k] = 1;
                    maxx = max(maxx, j);
                    maxy = max(maxy, k);
                }
            }
        }
        int tot = 0;
        int ok = true;
        while (ok) {
            ++tot;
            ok = false;
            memcpy(last, cur, sizeof(cur));
            memset(cur, 0, sizeof(cur));
            for (i = 0; i <= maxx + 1; ++i) {
                for (j = 0; j <= maxy + 1; ++j)
                {
                    if (last[i-1][j] && last[i][j-1] ||
                            last[i][j] && (last[i-1][j] || last[i][j-1])) {
                        cur[i][j] = 1;
                        maxx = max(maxx, i);
                        maxy = max(maxy, j);
                        ok = true;
                    }
                }
            }
        }
        printf("%d\n", tot);
	}
	return 0;
}
