#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int max_n = 200;
const int oo = 1000000000;
const double eps = 1e-9;

int n;
bool vis[max_n][max_n], get[max_n][max_n];

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int testID = 0;testID < test;testID++) {
		int x, y, x1, y1, cnt = 0, mx = 0, my = 0;
		scanf("%d", &n);
		for (int i = 0;i < n;i++) {
			scanf("%d %d %d %d", &x, &y, &x1, &y1);
			mx = max(mx, x1);
			my = max(my, y1);
			for (int q = x;q <= x1;q++) {
				for (int r = y;r <= y1;r++) {
					if (!vis[q][r])
						cnt++;
					vis[q][r] = true;
				}
			}
		}
		mx += 50, my += 50;
		int ans = 0;
		memcpy(get, vis, sizeof(get));
		while (cnt) {
			cnt = 0;
			ans++;
			for (int i = 0;i <= mx;i++) {
				for (int j = 0;j <= my;j++) {
					if (vis[i][j] && !vis[i - 1][j] && !vis[i][j - 1]) {
						get[i][j] = false;
					}
					else if (!vis[i][j] && vis[i - 1][j] && vis[i][j - 1]) {
						get[i][j] = true;
					}
				}
			}
			for (int i = 0;i <= mx;i++) {
				for (int j = 0;j <= my;j++) {
					cnt += get[i][j];
				}
			}
			memcpy(vis, get, sizeof(vis));
		}
		printf("Case #%d: %d\n", testID + 1, ans);
	}
	return 0;
}
