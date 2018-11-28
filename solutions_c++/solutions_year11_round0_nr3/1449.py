#include<cstdio>
#include<cstdlib>

int main() {
	int t;
	freopen("C-large.in", "r", stdin);
	freopen("OutLargeC.txt", "w", stdout);
	scanf("%d", &t);
	
	for(int kase = 1; kase <= t; ++kase) {
		fprintf(stderr, "%d\n", kase);
		
		
		int n, ans = 0, all = 0, min = 0, c;
		scanf("%d", &n);
		for(int i = 0; i < n; ++i) {
			scanf("%d", &c);
			all ^= c;
			ans += c;
			if(!min || min > c) {
				ans += min;
				min = c;
				ans -= min;
			}
		}

		
		printf("Case #%d: ", kase);
		if(all)
			printf("NO");
		else
			printf("%d", ans);
		printf("\n");
	}
}
