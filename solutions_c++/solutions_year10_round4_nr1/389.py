#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <memory.h>
using namespace std;


int d[200][200];
int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <=T; t++) {
		int k;
		scanf("%d", &k);
		memset(d, -1, sizeof(d));
		getchar();
		for (int i = 0; i < 2*k-1; i++) {
			char line[200];
			gets(line);
			for (int j = 0; line[j]; j++) if (line[j] != ' ') d[i][j] = line[j] - '0';
		}
		int ml = 123456789;
		for (int cy = 0; cy < 2*k-1; cy++) {
			for (int cx = 0; cx < 2*k-1; cx++) {
				bool ok = true;
				for (int y = 0; y < 2*k-1 && ok; y++) {
					for (int x = 0; x < 2*k-1 && ok; x++) {
						int y1 = y, x1 = cx + (cx - x);
						if (x1 >= 0 && x1 < 2*k-1 && d[y][x] != d[y1][x1] && d[y][x] != -1 && d[y1][x1] != -1)
							ok = false;
						int y2 = cy + (cy - y), x2 = x;
						if (y2 >= 0 && y2 < 2*k-1 && d[y][x] != d[y2][x2] && d[y][x] != -1 && d[y2][x2] != -1)
							ok = false;
					}
				}
				if (ok) {
					int len = abs(k-1-cy) + abs(k-1-cx);
					ml = min(ml, len);
				}
			}
		}
		printf("Case #%d: %d\n", t, (k+ml)*(k+ml) - k*k);
	}
}

