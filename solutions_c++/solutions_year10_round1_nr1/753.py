#include <stdio.h>
#include <memory.h>

int dx[] = {0, 1, 1, -1};
int dy[] = {1, 1, 0, 1};
char z[55][55];
int dp[55][55][4];

void go() {
	int n, k;
	scanf("%d%d\n", &n, &k);
	for (int i = 0; i < n; ++i)
		gets(z[i]);
	for (int i = 0; i < n; ++i) {
		for (int j = n-1, l = n - 1; j >= 0; --j) 
			if (z[i][j] != '.') {
				z[i][l] = z[i][j];
				if (j != l)
					z[i][j] = '.';
				--l;
			}
	}
	memset(dp, 0, sizeof dp);
	bool red = false, blue = false;
	for (int j = n-1; j >= 0; --j)
		for (int i = n-1; i >= 0; --i)
			for (int l = 0; l < 4; ++l) {
				if (z[i][j] != '.') {
					if (i + dx[l] >= 0 && i + dx[l] < n && j + dy[l] < n && z[i][j] == z[i + dx[l]][j + dy[l]]) 
						dp[i][j][l] = dp[i + dx[l]][j + dy[l]][l] + 1;
					else
						dp[i][j][l] = 1;
					if (z[i][j] == 'R' && dp[i][j][l] >= k)
						red = true;
					if (z[i][j] == 'B' && dp[i][j][l] >= k)
						blue = true;

				}
			}
	if (red && blue)
		puts("Both");
	else if (red)
		puts("Red");
	else if (blue)
		puts("Blue");
	else
		puts("Neither");
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		printf ("Case #%d: ", i+1);
		go();
	}
}