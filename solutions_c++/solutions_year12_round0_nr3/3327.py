#include <cstdio>
#include <cstring>

using namespace std;

int hash[2000001];

int main() {
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; t++) {
		memset(hash, 0, sizeof(hash));
		int a, b;
		scanf("%d%d", &a, &b);
		int ans = 0;
		for (int n = a; n < b; n++) {
			int d[10], len = 0;
			int tmp = n;
			while (tmp > 0) {
				d[len++] = tmp % 10;
				tmp /= 10;
			}
			for (int i = 0; i < len; i++)
				if (d[i] > 0) {
					int m = 0;
					for (int j = 0; j < len; j++) {
						int p = i - j;
						if (p < 0) p += len;
						m = m * 10 + d[p];
					}
					if (m > n && m <= b) {
						if (hash[m] != n) {
							ans++;
							hash[m] = n;
						}
					}
				}
		}
		printf("Case #%d: %d\n", t, ans);
	}
}