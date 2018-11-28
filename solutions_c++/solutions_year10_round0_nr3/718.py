#include <stdio.h>
#include <string.h>
int a[1111];
int cango[1111];
long long sa[1111];
char mark[1111];

int main() {
	int prob = 0;
	int tn;
	long long sum, ans;
	int len, r, k, n;
	for (scanf("%d", &tn); tn--; ) {
		scanf("%d%d%d", &r, &k, &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
		}
		for (int i = 0; i < n; i++) {
			sa[i] = a[i];
			cango[i] = i;
			for (int j = (i + 1) % n; j != i; j = (j + 1) % n) {
				if (sa[i] + a[j] > k) {
					cango[i] = j;
					break;
				}
				sa[i] += a[j];
			}
		}
		printf("Case #%d: ", ++prob);
		int now = 0;
		ans = sum = 0, len = 0;
		int rest = r;
		memset(mark, 0, sizeof(mark));
		while (rest) {
			if (mark[now]) {
				break;
			}
			mark[now] = 1;
			ans += sa[now];
			rest--;
			now = cango[now];
		}
		memset(mark, 0, sizeof(mark));
		while (rest) {
			if (mark[now]) {
				break;
			}
			mark[now] = 1;
			sum += sa[now];
			ans += sa[now];
			len++;
			rest--;
			now = cango[now];
		}
		if (!rest) {
			printf("%I64d\n", ans);
		} else {
			sum *= rest / len;
			ans += sum;
			rest %= len;
			while (rest) {
				ans += sa[now];
				now = cango[now];
				rest--;
			}
			printf("%I64d\n", ans);
		}
	}
	return 0;
}

