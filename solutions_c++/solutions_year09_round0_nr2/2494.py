#include <cstdio>
#define NMAX 128
#define infinit 32767

int N, M, T, K;
int V[NMAX][NMAX];
char C[NMAX][NMAX], Q[NMAX];

int minim(int a, int b, int c, int d)
{
	int minim = a;
	minim  = (b < minim? b: minim);
	minim  = (c < minim? c: minim);
	minim  = (d < minim? d: minim);
	return minim;
}

int descent(int i, int j, int k, int l)
{
	// este sink
	if (minim(V[i][j+1], V[i][j-1], V[i-1][j], V[i+1][j]) >= V[i][j])
		return 0;

	int min = infinit, x, y;
	
	// selectez minimul dinspre sud
	if (i < N && V[i+1][j] <= min && V[i+1][j] < V[i][j])
	{
		min = V[i+1][j];
		x = i+1;
		y = j;
	}

	// selectez minimul dinspre est
	if (j < M && V[i][j+1] <= min && V[i][j+1] < V[i][j])
	{
		min = V[i][j+1];
		x = i;
		y = j+1;
	}

	// selectez minimul dinspre vest
	if (j > 1 && V[i][j-1] <= min && V[i][j-1] < V[i][j])
	{
		min = V[i][j-1];
		x = i;
		y = j-1;
	}

	// selectez minimul dinspre nord
	if (i > 1 && V[i-1][j] <= min && V[i-1][j] < V[i][j])
	{
		min = V[i-1][j];
		x = i-1;
		y = j;
	}

	return (x == k && y == l);
}

void rec(int i, int j)
{
	C[i][j] = K;

	// daca ar fi coborat din stanga
	if (j > 1)
		if (descent(i, j-1, i, j))
			rec(i, j-1);

	// daca ar fi coborat din dreapta
	if (j < M)
		if (descent(i, j+1, i, j))
			rec(i, j+1);

	// daca ar fi coborat de sus
	if (i > 1)
		if (descent(i-1, j, i, j))
			rec(i-1, j);

	// daca ar fi coborat de jos
	if (i < N)
		if (descent(i+1, j, i, j))
			rec(i+1, j);
}

int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);

	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		// citesc matricea
		scanf("%d%d", &N, &M);
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= M; ++j)
				scanf("%d", &V[i][j]);

		// bordez matricea
		for (int i = 0; i <= N+1; V[i][0] = V[i][M+1] = infinit, ++i);
		for (int j = 0; j <= M+1; V[0][j] = V[N+1][j] = infinit, ++j);

		// identific sink-urile
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= M; ++j)
				if (minim(V[i][j+1], V[i][j-1], V[i-1][j], V[i+1][j]) >= V[i][j])
				{
					rec(i, j);
					++K;
				}

		// sortez caracterele
		char c = 'a';
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= M; ++j)
				if (!Q[C[i][j]])
					Q[C[i][j]] = c++;

		// scriu rezultatul
		printf("Case #%d:\n", t);
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= M; ++j)
			{
				printf("%c", Q[C[i][j]]);
				printf("%c", (j < M? ' ': '\n'));
			}
		}

	return 0;
}