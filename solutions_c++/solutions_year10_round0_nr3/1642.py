//by shuangYY

#include <cstdio>
#include <cstring>

int main()
{
	int t, r, k, n;
	int g[1000];
	long long count[1000][2];

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	scanf("%d", &t);
	for(int i=1; i<=t; i++){
		scanf("%d%d%d", &r, &k, &n);
		for(int j=0; j<n; j++)
			scanf("%d", &(g[j]));

		memset(count, 0, sizeof(count));
		for(int j=0; j<n; j++){
			count[j][0] = g[j];
			count[j][1] = j;

			int r = (j + 1) % n;
			while(r != j && (count[j][0] + g[r]) <= k){
				count[j][0] = count[j][0] + g[r];
				count[j][1] = r;
				r = (r+1) % n;
			}
		}

		int cur = 0;
		long long  total = 0;
		for(int j=0; j<r; j++){
			total += count[cur][0];
			cur = (count[cur][1] + 1) % n;
		}

		printf("Case #%d: %lld\n", i, total);
	}

	return 0;
}