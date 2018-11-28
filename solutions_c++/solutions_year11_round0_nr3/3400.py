#include <stdio.h>
const int INF = 1<<29;
int main()
{	freopen("C-large.in", "r", stdin);
	freopen("C-large.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int n;
		scanf("%d", &n);
		int min = INF, ans, sum;
		ans = sum = 0;
		for (int i = 0; i < n; ++i) {
			int num;
			scanf("%d", &num);
			ans ^= num;
			sum += num;
			if (min > num)
				min = num;
		}
		printf("Case #%d: ", t);
		if (!ans)	printf("%d\n", sum - min);
		else		puts("NO");
	}
	return 0;
}
