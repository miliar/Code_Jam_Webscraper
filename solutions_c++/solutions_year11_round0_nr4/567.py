#include <stdio.h>

int main()
{
	int T;
	scanf("%d", &T);

	for(int t=1; t<=T; t++)
	{
		int N, x, y=0;

		scanf("%d", &N);

		for(int i=1; i<=N; i++)
		{
			scanf("%d", &x);
			if(x!=i)y++;
		}

		printf("Case #%d: %d.000000\n", t, y);
	}
	
	return 0;
}