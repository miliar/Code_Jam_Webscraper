#include<stdio.h>

#define MAX_N 101

int N, L, H, Num[MAX_N];

void leerEntrada()
{
	scanf("%d %d %d\n", &N, &L, &H);
	for (int j=0; j<N; j++)
		scanf("%d", Num+j);
	return;
}

int go()
{
	for (int r = L; r <= H; r++)
	{
		int sirve = 1;
		for (int n = 0; n < N; n++)
		{
			if (r == Num[n])
				continue;

			if ((r > Num[n]) && (r % Num[n] != 0))
			{
				sirve = 0;
				break;
			}

			if ((r < Num[n]) && (Num[n] % r != 0))
			{
				sirve = 0;
				break;
			}

		}
		if (sirve == 1)
			return r;
	}
	return -1;
}

int main(void)
{
	int T;
	scanf("%d\n", &T);
	for (int t=1; t<=T; t++)
	{
		leerEntrada();
		int ret = go();

		printf("Case #%d: ", t);
		if (ret == -1)
			printf("NO\n");
		else
			printf("%d\n", ret);
	}
}