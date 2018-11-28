#include <stdio.h>
#include <algorithm>

using namespace std;

char s[100][100];
int f[100];

int solve() {
	int n = 0;
	scanf("%d\n", &n);
	int res = 0;
	for (int i = 0; i < n; ++i) {
		gets(s[i]);
		f[i] = 0;
		for (int j = 0; j < n; ++j) if (s[i][j] == '1') f[i] = j;
	}
	for (int i = 0; i < n; ++i) {
		if (f[i] > i) {
			int j = i + 1;
			while (j < n && f[j] > i) ++j;
			if (j == n) return -1;
			for (int k = j; k > i; --k)
				swap(f[k], f[k-1]), ++res;
		}
	}
	return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: %d\n", i+1, solve());
	}
}