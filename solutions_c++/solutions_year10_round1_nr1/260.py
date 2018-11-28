#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

const int	MAXN	=	50 + 10;
const int	dx[]	=	{0, 1, 1, 1};
const int	dy[]	=	{1, 0, -1, 1};

char	grids[MAXN][MAXN];
int		N, K;
int		T;

void Init ()
{
	scanf ("%d%d", &N, &K);
	for (int i = 0; i < N; ++i)
		scanf ("%s", grids[i]);
}

void Rotate ()
{
	char bak[MAXN][MAXN];
	memcpy (bak, grids, sizeof (bak));

	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
		{
			grids[j][N - 1 - i] = bak[i][j];
		}
}

void Fall ()
{
	for (int i = N - 1; i >= 0; --i)
		for (int j = 0; j < N; ++j)
			if (grids[i][j] != '.')
			{
				for (int k = i + 1; k < N && grids[k][j] == '.'; ++k)
				{
					grids[k][j] = grids[k - 1][j];
					grids[k - 1][j] = '.';
				}
			}
}

int Count (char c)
{
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
			for (int d = 0; d < 4; ++d)
			{
				int px = i, py = j;
				int sum = 0;
				while (px < N && py >= 0 && py < N && grids[px][py] == c)
				{
					sum ++;
					px += dx[d];
					py += dy[d];
				}

				if (sum >= K)
					return 1;
			}
		
	return 0;
}

void Solve ()
{
	Rotate ();
	Fall ();

	int a = Count ('R');
	int b = Count ('B');

	if (a && b)
		printf ("Both\n");
	else
	if (!a && !b)
		printf ("Neither\n");
	else
	if (a && !b)
		printf ("Red\n");
	else
	if (!a && b)
		printf ("Blue\n");	
}

int main()
{
	freopen ("A-large.in", "r", stdin);
	freopen ("out.txt", "w", stdout);

	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf ("Case #%d: ", i);
		Init ();
		Solve ();
	}
	
	return 0;
}
