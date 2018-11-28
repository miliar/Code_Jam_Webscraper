#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAX_N = 60;
const int dx[] = {0, 0, 1, 1, 1, -1, -1, -1};
const int dy[] = {1, -1, 0, 1, -1, 0, 1, -1};

int cas, n, m;
char a[MAX_N][MAX_N];

int main() {
	freopen("D:\\A-large.in", "r", stdin);
	freopen("D:\\A-large.out", "w", stdout);
	scanf("%d", &cas);
	for (int cc = 1; cc <= cas; ++cc) {
		scanf("%d%d", &n, &m);
		memset(a, 0, sizeof(a));
		for (int i = 1; i <= n; ++i) {
			scanf("%s", a[i] + 1);
		}
		for (int i = 1; i <= n; ++i) {
			for (int j = n - 1; j; --j) {
				for (int k = j; k < n; ++k)
					if (a[i][k + 1] == '.') swap(a[i][k + 1], a[i][k]);
			}
		}
		bool red = false, blue = false;
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				if (!red && a[i][j] == 'R') {
					for (int d = 0; d < 8; ++d) {
						int cnt = 1;
						for (int x = i + dx[d], y = j + dy[d]; a[x][y] == 'R'; x += dx[d], y += dy[d]) ++cnt;
						if (cnt >= m) red = true;
					}
				}
				if (!blue && a[i][j] == 'B') {
					for (int d = 0; d < 8; ++d) {
						int cnt = 1;
						for (int x = i + dx[d], y = j + dy[d]; a[x][y] == 'B'; x += dx[d], y += dy[d]) ++cnt;
						if (cnt >= m) blue = true;
					}
				}
			}
		}
		printf("Case #%d: ", cc);
		if (red && blue) puts("Both");
		if (red && !blue) puts("Red");
		if (!red && blue) puts("Blue");
		if (!red && !blue) puts("Neither");
	}
	return 0;
}
