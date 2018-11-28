#include <stdio.h>
#include <string.h>
#define MAXN 256
int f[MAXN][MAXN];
int max(int a, int b) {
	return a>b?a:b;
}
int min(int a,int b) {
	return a<b?a:b;
}
int main(int argc, char* argv[]) {
	int T;
	scanf("%d", &T);
	int cas = 1;
	while (T--) {
		int n;
		scanf("%d", &n);
		getchar();
		//printf("n: %d\n", n);
		memset(f, -1, sizeof(f));
		for (int i=1; i<=(2*n-1); ++i) {
			int len;
			if (i <= n) {
				len = n + i - 1;
			} else {
				len = n + (2*n-i-1);
			}
			//printf("len: %d\n", len);
			for (int j=1; j<=len; ++j) {
				char c;
				c = getchar();
				if (c != ' ') {
					f[i][j] = c - '0';
				}
			}
			getchar();
			//printf("kick\n");
		}
		//printf("over\n");
		int ans = MAXN;
		for (int i=1; i<=(2*n-1); ++i) {
			for (int j=1; j<=(2*n-1); ++j) {
				bool ok = true;
				// i
				int r1 = i-1;
				int r2 = i+1;
				int c1 = j-1;
				int c2 = j+1;
				while (r1>=1 && r2<=(2*n-1)) {
					for (int c=1; c<=(2*n-1); ++c) {
						if (f[r1][c] == -1 || f[r2][c] == -1) {
							continue;
						}
						if (f[r1][c] != f[r2][c]) {
							ok = false;
							break;
						}
					}
					if (!ok) {
						break;
					}
					r1--;
					r2++;
				}
				if (!ok) {
					continue;
				}
				// j
				while (c1>=1 && c2<=(2*n-1)) {
					for (int r=1; r<=(2*n-1); ++r) {
						if (f[r][c1] == -1 || f[r][c2] == -1) {
							continue;
						}
						if (f[r][c1] != f[r][c2]) {
							ok = false;
							break;
						}
					}
					if (!ok) {
						break;
					}
					c1--;
					c2++;
				}
				if (!ok) {
					continue;
				}
				// ok
				int temp = max(i, 2*n-i);
				/*if (j%2==0) {
					temp = max(temp, 2* max(j/2, n- j/2));
				} else {
					temp = max(temp, 2 * max((j+1)/2, n-(j-1)/2) - 1);
				}*/
				temp = (max(j, 2*n-j) + max(n-i, i-n));
				//temp = max(i, max(j, max(2*n-i, 2*n-j)));
				ans = min(ans, temp);
				//printf("%d %d %d\n", i, j, temp);
			}
		}
		ans = ans*ans - n*n;
		printf("Case #%d: %d\n", cas++, ans);
	}
}