#include <stdio.h>
const int MAXN = 100;
int n, l, h;
int a[MAXN];
int main() {
	int cases;
	scanf("%d", &cases);
	for (int k = 0; k < cases; ++k) {
		printf("Case #%d: ", k + 1);
		scanf("%d%d%d", &n, &l, &h);
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		bool flag = false;
		for (int i = l; i <= h; ++i) {
			bool is_ans = true;
			for (int j = 0; j < n; ++j) 
				if ((a[j] % i != 0) && (i % a[j] != 0)) {
					is_ans = false;
					break;
				}
			if (is_ans) {
				flag = true;
				printf("%d\n", i);
				break;
			}
		}
		if (!flag) printf("NO\n");
	}
	return 0;
}
