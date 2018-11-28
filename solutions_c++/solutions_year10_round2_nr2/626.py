#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int ans;

int cmp(const void *a, const void *b)
{
	if(*(int*)a > *(int*)b) return -1;
	return 1;
}

int main()
{
	int t;
	int i, j, j1;
	int n, k, b, c;
	int x[120], v[120], p[120], min[120], f[120], xs[120], vs[120];
	int minv;
	int minb;
	int passd = 0;
	freopen("Redownload B-large.in","r",stdin);freopen("Redownload B-large.out","w",stdout);
	scanf("%d", &c);
	for(i = 1; i <= c; i++) {
		scanf("%d %d %d %d", &n, &k, &b, &t);
		for(j = 0; j < n; j++)scanf("%d", &x[j]);
		for(j = 0; j < n; j++)scanf("%d", &v[j]);
		ans = 0;
		passd = 0;
		if(k == 0) {
			printf("Case #%d: %d\n", i, ans);
			continue;
		}
		for(j = n - 1; j >= 0 && k > 0; j--) {
			minb = x[j] + v[j] * t;
			if(minb >= b){
				k--;
				ans += passd;
			}
			else {
				passd++;
			}
		}
/*		for(j = 0; j < n; j++) {
			f[j] = 0;
			vs[j] = v[j];
			min[j] = (b - x[j])/t;
			if( (b - x[j]) % t != 0)min[j]++;
		}
		qsort(&vs, n, sizeof(int) ,cmp);
		for(j = 0; j < n; j++)printf("vs[%d] = %d\n", j, vs[j]);
		for(j = 0, j1 = n - k; j1 < n; j1++, j++) {
			minb = x[j1] + vs[j] * t;
			if(minb < b)break;
		}*/
		if(k) {
			printf("Case #%d: IMPOSSIBLE\n", i);
			continue;
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}