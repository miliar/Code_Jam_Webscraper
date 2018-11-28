#include <stdio.h>
#include <string.h>

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,T;
	scanf("%d", &T);
	for (t=1; t<=T; t++)
	{
		int N,K;
		scanf("%d %d", &N, &K);
		int digit;
		for (digit=0; digit<N; digit++)
		{
			if (K%2==0)
				break;
			K/=2;
		}
		if (digit==N)
			printf("Case #%d: ON\n",t);
		else
			printf("Case #%d: OFF\n",t);
	}
	return 0;
}