#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int a[2][102][102];

int main() {
	freopen("E://C-small-attempt0.in", "r", stdin);
	freopen("E://out.txt", "w", stdout);
	int t, n;
	int tc = 0;
	scanf("%d", &t);
	while(t--) {
		scanf("%d", &n);
		int ans = 1;
		int cnt = 0;
		memset(a[0], 0, sizeof(a[0]));
		while(n--) {
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &y1, &x1, &y2, &x2);
			for(int i = x1; i <= x2; i++) {
				for(int j = y1; j <= y2; j++) {
					a[0][i][j] = 1;
				}
			}
		}
		for(int i = 1; i <= 100; i++) {
			for(int j = 1; j <= 100; j++) {
				if(a[0][i][j]) cnt++;
			}
		}
		int curr = 0;
		int next = 1;
		while(cnt) {
			//printf("%d\n", cnt);
			memset(a[next], 0, sizeof(a[next]));
			for(int i = 1; i <= 100; i++) {
				for(int j = 1; j <= 100; j++) {
					if(a[curr][i][j] == 1) {
						if(a[curr][i - 1][j] == 0 && a[curr][i][j - 1] == 0) {
							a[next][i][j] = 0;
						} else a[next][i][j] = 1;
					} else {
						if(a[curr][i - 1][j] == 1 && a[curr][i][j - 1] == 1) {
							a[next][i][j] = 1;
						}
					}
				}
			}
			cnt = 0;
			for(int i = 1; i <= 100; i++) {
				for(int j = 1; j <= 100; j++) {
					if(a[next][i][j]) cnt++;
				}
			}
			if(cnt) {
				ans++;
				curr = next;
				next ^= 1;
			}
		}
		printf("Case #%d: %d\n", ++tc, ans);
	}
	return 0;
}