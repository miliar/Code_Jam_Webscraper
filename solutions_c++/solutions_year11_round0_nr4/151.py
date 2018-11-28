#include <cstdio>
#include <algorithm>

double f[1010][1010];
int v[1010], ov[1010];
double s[1000];
int main() {
	f[1][1] = 1;
	for (int i = 1; i <= 1000; ++i) {
		for (int j = 0; j <= i; ++j) {
			f[i + 1][j + 1] += f[i][j] / (i + 1);
			f[i + 1][j] += f[i][j] * (i - j) / (i + 1);
			if (j)
				f[i + 1][j - 1] += f[i][j] * j / (i + 1);
		}
	}
	s[0] = 0;
	s[1] = 0;
	for (int i = 2; i <= 1000; ++i) {
		for (int j = 1; j <= i; ++j) {
			s[i] += f[i][j] * (s[i - j] + 1);
		}
		s[i] = (s[i] + f[i][0]) / (1 - f[i][0]);
	}
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		int n;
		scanf("%d", &n);
		for (int i = 0; i< n; ++i) {
			scanf("%d", &v[i]);
			ov[i] = v[i];
		}
		std::sort(v, v + n);
		int cnt = 0;
		for (int i = 0; i < n; ++i)
			cnt += (ov[i] != v[i]);
		printf("Case #%d: %.6lf\n", Ti, s[cnt]);
	}
}
