#include <stdio.h>
#include <string.h>

const int	MAXP	=	10;
const int	MAXT	=	(1 << MAXP);
const int	MAXNUM	=	1000000000;

int		M[MAXT];
int		price[MAXP][MAXT];
int		F[MAXP][MAXT][MAXP + 1];
int		P, T;

void Init ()
{
	scanf ("%d", &P);
	for (int i = 0; i < (1 << P); ++i)
	{
		scanf ("%d", M + i);
		M[i] = P - M[i];

		//printf ("%d ", M[i]);
	}
	//printf ("\n");

	for (int i = 0; i < P; ++i)
		for (int j = 0; j < (1 << (P - i - 1)); ++j)
			scanf ("%d", price[i] + j);
}

int MAX (int a, int b)
{
	return a > b ? a : b;
}

void Solve ()
{
	memset (F, 0, sizeof (F));

	for (int i = 0; i < (1 << (P - 1)); ++i)
	{
		for (int j = 0; j < MAX (M[i * 2], M[i * 2 + 1]) - 1; ++j)
			F[0][i][j] = MAXNUM;

		if (MAX (M[i * 2], M[i * 2 + 1]) == 0) F[0][i][0] = 0;
		else
		{
			F[0][i][MAX (M[i * 2], M[i * 2 + 1]) - 1] = price[0][i];
			F[0][i][MAX (M[i * 2], M[i * 2 + 1])] = 0;
		}
	}

	for (int i = 1; i < P; ++i)
		for (int j = 0; j < (1 << (P - i - 1)); ++j)
			for (int k = 0; k <= P; ++k)
			{
				F[i][j][k] = MAXNUM;

				int temp = F[i - 1][j * 2][k] + F[i - 1][j * 2 + 1][k];
				if (temp < F[i][j][k])
					F[i][j][k] = temp;

				if (k == P)
					continue;

				temp = F[i - 1][j * 2][k + 1] + F[i - 1][j * 2 + 1][k + 1] + price[i][j];
				if (temp < F[i][j][k])
					F[i][j][k] = temp;
			}
	
	for (int i = 0; i < P; ++i)
		for (int j = 0; j < (1 << (P - i - 1)); ++j)
			for (int k = 0; k <= P; ++k)
			{
				//printf ("%d %d %d    %d\n", i, j, k, F[i][j][k]);
			}
	
	printf ("%d\n", F[P - 1][0][0]);
}

int main()
{
	freopen ("B-large.in", "r", stdin);
	freopen ("ou.txt", "w", stdout);

	int T;

	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf ("Case #%d: ", i);
		Init ();
		Solve ();
	}

	return 0;
}
