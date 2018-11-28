#include<cstdio>

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		int N;
		scanf("%d", &N);
		int res = 0;
		for (int i = 1; i <= N; i++)
		{
			int x;
			scanf("%d", &x);
			res += (x != i);
		}
		printf("Case #%d: %d.000000\n", t, res);
	}
	
	return 0;
}
