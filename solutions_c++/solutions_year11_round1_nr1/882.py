#include<stdio.h>

long long P1, P2, N;

int T;

void Go(long long P, long long &up, long long &down)
{
	// P * down = 100 * up

	long long div;
	for(div=100;div>=1;div--)
	{
		if(100 % div == 0)
		{
			if(P % div == 0)
			{
				down = 100 / div;
				up = P / div;
				return;
			}
		}
	}
}

int main(void)
{
	int l1, l0;
	long long G1, W1, G2, W2;
	long long gob;

	freopen("a2.in","r",stdin);
	freopen("a2.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		printf("Case #%d: ",l0);
		scanf("%lld %lld %lld",&N,&P1,&P2);
		Go(P1, W1, G1);
		Go(P2, W2, G2);
		if(G1 > N)
		{
			printf("Broken\n");
			continue;
		}

		if(W2 == G2 && W1 != G1)
		{
			printf("Broken\n");
			continue;
		}

		if(W1 > 0 && W2 == 0)
		{
			printf("Broken\n");
			continue;
		}
		

		printf("Possible\n");
	}

	return 0;
}