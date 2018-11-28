#include<stdio.h>
#include<math.h>

#define SZ 1005

int g[SZ];
int cnt[SZ];
int next[SZ];

int main()
{
	//freopen("C:\\Codejam 2010\\Qualification\\C-small-attempt0.in", "rt", stdin);
	//freopen("C:\\Codejam 2010\\Qualification\\C-small-test1.out", "wt", stdout);

	freopen("C:\\Codejam 2010\\Qualification\\C-large.in", "rt", stdin);
	freopen("C:\\Codejam 2010\\Qualification\\C-large.out", "wt", stdout);
	int inp, r, kase, n, k, i, j;
	scanf("%d", &inp);
	//printf("%d\n", inp);
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d %d %d", &r, &k, &n);
		//printf("100000000 %d %d\n", k, n);
		for(i = 0; i < n; i++)
		{
			scanf("%d", &g[i]);
			//printf("%d ", g[i]);
		}
		//printf("\n");
		for(i = 0; i  < n; i++)
		{
			int st = g[i];
			for(j = i; ; )
			{
				j = (j + 1) % n;
				if((j == i) || (st + g[j] > k))
					break;
				st = st + g[j];
			}
			cnt[i] = st;
			next[i] = j;
		}
		__int64 sum = 0;
		int cur = 0;
		for(i = 0; i < r; i++)
		{
			sum = sum + cnt[cur];
			cur = next[cur];
		}
		printf("Case #%d: %I64d\n", kase, sum);
	}
	return 0;
}

