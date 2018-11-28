#include<cstdio>
#include<cstdlib>

int main()
{
	int C, cas;
	scanf("%d", &C);
	for(cas = 1; cas <=C; cas ++)
	{
		int N, K, B, T;
		int X[100], V[100];
		int i, j, k;
		scanf("%d %d %d %d", &N, &K, &B, &T);
		for(i = 0; i < N; i ++)
		{
			scanf("%d", &X[i]);
		}
		for(i = 0; i < N; i ++)
		{
			scanf("%d", &V[i]);
		}
		int ans = 0;
		for(i = N-1; i >= 0; i --)
		{
			if(K == 0)break;
			if(V[i]*T >= B-X[i])
			{
				K --;
			}
			else {
				ans += K;
			}
		}
		if(K > 0)
		{
			printf("Case #%d: IMPOSSIBLE\n", cas);
		}
		else {
			printf("Case #%d: %d\n", cas, ans);
		}
	}
	return 0;
}
