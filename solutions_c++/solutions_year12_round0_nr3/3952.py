#include <cstdio>
#include <cstring>

int cnt[2000000];

int main() {
	int test, A, B, res;
	scanf("%d", &test);
	for (int i = 0; i < test; i++) {
		scanf("%d %d",&A,&B);
		res = 0;
		memset(cnt, 0, sizeof(cnt));
		for (int j = A; j <= B; j ++) {
			int k = 1, t = j, r = j;
			while (k <= j) k *= 10;
			k /= 10;
			do {
				t = t / 10 + t % 10 * k;
				if (t < r) r = t;
			} while (t != j);
			res += cnt[r];
			cnt[r] ++;
		}
		printf("Case #%d: %d\n", i + 1, res);
	}
	return 0;
}
