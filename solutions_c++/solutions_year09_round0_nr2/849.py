#include <iostream>
#include <vector>

using namespace std;

int a[200][200];
char ans[200][200];
char next;
int w,h;

char step(int i, int j) {
	if (ans[i][j] != 0)
		return ans[i][j];
	if (i > 0 && a[i - 1][j] < a[i][j] && (j>0 && a[i - 1][j] <= a[i][j-1] || j == 0) && (j < w-1 && a[i - 1][j] <= a[i][j+1] || j==w-1) && (i<h-1&& a[i-1][j] <= a[i+1][j] || i==h-1)) {
		return ans[i][j] = step(i - 1, j);
	} else if (j > 0 && a[i][j-1] < a[i][j] && (j<w-1&&a[i][j-1] <= a[i][j+1]||j==w-1) && (i<h-1&&a[i][j-1] <= a[i+1][j]||i==h-1)) {
		return ans[i][j] = step(i, j - 1);
	} else if (j < w - 1 && a[i][j + 1] < a[i][j] && (i<h-1&&a[i][j + 1] <= a[i+1][j]||i==h-1)) {
		return ans[i][j] = step(i, j + 1);
	} else if (i < h - 1 && a[i + 1][j] < a[i][j]) {
		return ans[i][j] = step(i + 1, j);
	}
	return ans[i][j] = next++;
}

void solve(int test) {
	next = 'a';
	scanf("%d%d", &h,&w);
	for (int i = 0; i < h; ++i)
		for (int j = 0; j < w; ++j)
			scanf("%d", &a[i][j]);
	memset(ans, 0, sizeof(ans));
	for (int i = 0; i < h; ++i)
		for (int j = 0; j < w; ++j)
			ans[i][j] = step(i, j);
	printf("Case #%d:\n", test);
	for (int i = 0; i < h; ++i) {
		for (int j = 0; j < w; ++j)
			if (j == w - 1)
				printf("%c", ans[i][j]);
			else
				printf("%c ", ans[i][j]);
		printf("\n");
	}
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		solve(i + 1);
	}

	return 0;
}

