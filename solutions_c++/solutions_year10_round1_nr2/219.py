#include <iostream>
using namespace std;

const int	MAXN	=	100 + 10;
const int	MAXM	=	256;
const int	MAXNUM	=	1000000000;

int		T, N, D, I, M;
int		a[MAXN];
int		F[MAXN][MAXM];

void Init ()
{
	scanf ("%d%d%d%d", &D, &I, &M, &N);
	for (int i = 0; i < N; ++i)
		scanf ("%d", a + i);
}

int abs (int x)
{
	if (x > 0)
		return x;
	else
		return -x;
}

void update (int &S, int v)
{
	if (v < S)
		S = v;
}

void Dp ()
{
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < MAXM; ++j)
		{
			F[i][j] = MAXNUM;
			if (i == 0)
			{
				update (F[i][j], D);
			} else
			{
				update (F[i][j], F[i - 1][j] + D);
			}
			
			if (i == 0)
			{
				update (F[i][j], abs (j - a[i]));
			} else
			{
				for (int k = 0; k < MAXM; ++k)
					if (abs (k - j) <= M)
						update (F[i][j], F[i - 1][k] + abs (j - a[i]));
			}
		}

		int flag = 1;
		while (flag)
		{
			flag = 0;
			for (int j = 0; j < MAXM; ++j)
				for (int k = 0; k < MAXM; ++k)
					if (abs (j - k) <= M && F[i][j] + I < F[i][k])
					{
						update (F[i][k], F[i][j] + I);
						flag = 1;
					}
		}
	}

	int min = MAXNUM;
	for (int i = 0; i < MAXM; ++i)
	{
		if (F[N - 1][i] < min)
		{
			min = F[N - 1][i];
		}
	}

	printf ("%d\n", min);
}

int main()
{
	freopen ("B-large.in", "r", stdin);
	freopen ("out.txt", "w", stdout);
	
	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf ("Case #%d: ", i);
		Init ();
		Dp ();
	}

	return 0;
}
