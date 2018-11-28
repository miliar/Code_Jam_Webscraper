#include <iostream>

using namespace std;

const int N = 101;

int abs(int a, int b) {
	return a > b ? a - b : b - a;
}

int main() {

	int Tc;
	
	freopen("A-large.in", "r", stdin);
	freopen("qa-large.out", "w", stdout);

	scanf("%d", &Tc);

	for (int tc = 1; tc <= Tc; ++tc) {

		int n;

		scanf("%d", &n);

		int pos[N], mark[N], sum[N];

		for (int i = 0; i < n; ++i) {
			char s[2];
			int p;

			scanf("%s%d", s, &p);

			if ('O' == s[0]) {
				mark[i] = 0;
			} else {
				mark[i] = 1;
			}

			pos[i] = p;
		}
		
		int pre[2] = {-1, -1};

		for (int i = 0; i < n; ++i) {
			
			int res = 0;
			if (pre[mark[i]] == -1) {
				res = pos[i];
				if (i > 0) {
					if (res < sum[i - 1] + 1) {
						res = sum[i - 1] + 1;
					}
				}
			} else {
				res = abs(pos[i] - pos[pre[mark[i]]]) + sum[pre[mark[i]]] + 1;
				if (res < sum[i - 1] + 1) {
					res = sum[i - 1] + 1;
				}
			}

			sum[i] = res;
			pre[mark[i]] = i;
		}

		printf("Case #%d: %d\n", tc, sum[n - 1]);
	}

	return 0;
}

