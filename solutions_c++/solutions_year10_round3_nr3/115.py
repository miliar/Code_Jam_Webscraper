#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int mat[512][512];
char str[1024];
int cnt[1024];
int n, m, k;

inline bool valid(int sx, int sy, int x, int y) {
	return x >= sx && x < sx + k && y >= sy && y < sy + k;
}

int main() {
	int t, tc = 0;
	freopen("E://in.txt", "r", stdin);
	freopen("E://out.txt", "w", stdout);
	scanf("%d", &t);
	while(t--) {
		scanf("%d%d", &n, &m);
		for(int i = 0; i < n; i++) {
			scanf("%s", str);
			for(int j = 0; j < m / 4; j++) {
				int x;
				if(str[j] >= 'A') x = str[j] - 'A' + 10;
				else x = str[j] - 48;
				for(int k = 0; k < 4; k++) {
					mat[i][j * 4 + 3 - k] = (x >> k) & 1;
				}
			}
		}
		int size = min(n, m);
		for(int i = 0; i <= size; i++) cnt[i] = 0;
		for(k = size; k >= 1; k--) {
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < m; j++) {
					if(i + k <= n && j + k <= m) {
						bool find = true;
						for(int ii = i; ii < i + k && find; ii++) {
							for(int jj = j; jj < j + k; jj++) {
								if(mat[ii][jj] == -1) {
									find = false;
									break;
								}
								if(valid(i, j, ii - 1, jj) && mat[ii][jj] == mat[ii - 1][jj]) {
									find = false;
									break;
								}
								if(valid(i, j, ii, jj - 1) && mat[ii][jj] == mat[ii][jj - 1]) {
									find = false;
									break;
								}
							}
						}
						if(find) {
							cnt[k]++;
							for(int ii = i; ii < i + k; ii++) for(int jj = j; jj < j + k; jj++) mat[ii][jj] = -1;
						}
					}
				}
			}
		}
		int sum = 0;
		for(int i = 1; i <= size; i++) if(cnt[i]) sum++;
		printf("Case #%d: %d\n", ++tc, sum);
		for(int i = size; i >= 1; i--) {
			if(cnt[i]) {
				printf("%d %d\n", i, cnt[i]);
			}
		}
	}
	return 0;
}