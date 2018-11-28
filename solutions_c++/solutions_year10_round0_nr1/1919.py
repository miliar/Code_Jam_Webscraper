#include <stdio.h>

int N,K;
int T;

int main()
{
//	freopen("d:\\A-large.in","r",stdin);
//	freopen("d:\\output.txt","w",stdout);
	scanf("%d",&T);
	int i;
	for (i = 1;i <= T;i++)
	{
		scanf("%d %d",&N,&K);
		int value = (1 << N) - 1;
		if (K < value)
			printf("Case #%d: OFF\n",i);
		else if (K == value || (K - value) % (1 << N) == 0)
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
	}
	return 0;
}