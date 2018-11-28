#include <stdio.h>

int main()
{
	int T;
	scanf("%d", &T);

	for(int t=0; t<T; t++)
	{
		int mn = 200000000;
		int sum = 0;
		int s_pat = 0;
		int N, x;

		scanf("%d", &N);

		for(int i=0; i<N; i++)
		{
			scanf("%d", &x);
			sum+=x;
			if(mn>x)mn=x;
			s_pat ^= x;
		}

		if(s_pat)
		{
			printf("Case #%d: NO\n", t+1);
		}
		else
		{
			printf("Case #%d: %d\n", t+1, sum-mn);
		}
	}
}