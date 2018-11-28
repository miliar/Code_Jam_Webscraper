#include <cstdio>

int a[1010], b[1010];

int main() {
	int n, it;
	int t, ct=1;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d %d", &a[i], &b[i]);

		it = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				if (i != j)
				if ((b[j]-a[j] != b[i]-a[i]) && (b[j]-b[i])*(a[j]-a[i]) < 0)
					it++;

		printf("Case #%d: %d\n", ct++, it/2);
	}
	return 0;
}
