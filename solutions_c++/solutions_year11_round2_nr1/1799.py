#include<stdio.h>
#include<iostream>

using namespace std;

#define MAX_N 101

int T, N;
char Res[MAX_N][MAX_N];
double WP[MAX_N], OWP[MAX_N], OOWP[MAX_N], RPI[MAX_N];

void leerEntrada()
{
	scanf("%d\n", &N);
	for (int r = 0; r < N; r++)
	{
		for (int c = 0; c < N; c++)
			scanf("%c", &(Res[r][c]));
		scanf("\n");
	}
}

void mostrarEntrada()
{
	printf("N = %d\n", N);
	for (int r = 0; r < N; r++)
	{
		for (int c = 0; c < N; c++)
			printf("%c", Res[r][c]);
		printf("\n");
	}
	return;
}

void go()
{
	for (int t = 0; t < N; t++)
	{
		int ops = 0;
		int wins = 0;
		for (int o = 0; o < N; o++)
			if (Res[t][o] != '.')
			{
				ops++;
				wins += (Res[t][o] - '0');
			}
		WP[t] = (((double) wins) / ((double) ops));
	}

	for (int t = 0; t < N; t++)
	{
		double d = 0;
		int ops = 0;
		for (int o = 0; o < N; o++)
			if (Res[t][o] != '.')
			{
				ops++;
				int to = 0, tw = 0;
				for (int j = 0; j < N; j++)
					if ((Res[o][j] != '.') && (j != t))
					{
						to++;
						tw += (Res[o][j] - '0');
					}
				d += (((double) tw) / ((double) to));
			}
		OWP[t] = (d / ((double) ops));
	}

	for (int t = 0; t < N; t++)
	{
		int ops = 0;
		double d = 0;
		for (int o = 0; o < N; o++)
			if (Res[t][o] != '.')
			{
				ops++;
				d += OWP[o];
			}
		OOWP[t] = (d / ((double) ops));
	}

	for (int t = 0; t < N; t++)
		RPI[t] = .25f * WP[t] + .5f * OWP[t] + .25f * OOWP[t];
}

int main(void)
{
	scanf("%d\n", &T);
	for (int t = 0; t < T; t++)
	{
		leerEntrada();
		go();
		printf("Case #%d:\n", (t+1));
		for (int x = 0; x < N; x++)
			printf("%.10f\n", RPI[x]);
	}
}
