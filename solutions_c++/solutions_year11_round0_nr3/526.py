#include<cstdio>
#include<cstring>

int n;
int a[1111];

int main()
{
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		scanf("%d", &n);
		int sum = 0, min = 100000011;
		int ans = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			sum ^= a[i];
			ans += a[i];
			if (a[i] < min) min = a[i];
		}
		printf("Case #%d: ", tt);
		if (sum == 0) 
			printf("%d\n", ans - min);
		else printf("NO\n");
	}
	return 0;
}	
