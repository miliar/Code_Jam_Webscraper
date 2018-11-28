#include<stdio.h>
int x[10005], l[10005], d[10005], N, F;
int main()
{
	freopen("large-input.txt", "r", stdin);
	freopen("large-output.txt", "w", stdout);
	int T, t, i, j, k;
	scanf("%d", &T);
	for(t = 1; t <= T; t++){
		scanf("%d", &N);
		for(i = 1; i <= N; i++) scanf("%d %d", &x[i], &l[i]);
		scanf("%d", &F);
		for(i = 1; i <= N; i++) d[i] = 1000000001;
		for(i = 1; i <= N; i++)
			if(F - x[i] <= l[i]) d[i] = F - x[i];

		for(i = N; i > 1; i--)
		{
			for(j = i - 1; j >= 1; j--)
			{
				if(x[i] - x[j] < d[i]) continue;
				if(d[j] > x[i] - x[j] && x[i] - x[j] <= l[j]) d[j] = x[i] - x[j];
			}
		}
		if(d[1] <= l[1] && d[1] <= x[1])
			printf("Case #%d: YES\n", t);
		else
			printf("Case #%d: NO\n", t);
	}
	return 0;
}