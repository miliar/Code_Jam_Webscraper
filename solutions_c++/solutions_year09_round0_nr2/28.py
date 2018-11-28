#include <cstdio>
#include <cstring>

const int MaxN = 100 + 10;
const int Dx[] = {-1, 0, 0, 1};
const int Dy[] = {0, -1, 1, 0};

int N, M;
int Map[MaxN][MaxN];
int Fa[MaxN * MaxN];
char Char[MaxN * MaxN];

int GetRoot(int i)
{
	return (Fa[i] == i) ? Fa[i] : (Fa[i] = GetRoot(Fa[i]));
}

void Union(int i, int j)
{
	i = GetRoot(i);
	j = GetRoot(j);
	Fa[i] = j;
}

void Work()
{
	scanf("%d%d", &N, &M);
	for (int i = 0; i < N; i ++)
		for (int j = 0; j < M; j ++)
			scanf("%d", &Map[i][j]);
	for (int i = 0; i < N * M; i ++)
		Fa[i] = i;
	for (int i = 0; i < N; i ++)
		for (int j = 0; j < M; j ++)
		{
			int ii = -1, jj = -1, Min = Map[i][j];
			for (int k = 0; k < 4; k ++)
			{
				int ni = i + Dx[k];
				int nj = j + Dy[k];
				if (ni < 0 || ni >= N || nj < 0 || nj >= M)
					continue;
				if (Map[ni][nj] < Min)
				{
					ii = ni;
					jj = nj;
					Min = Map[ni][nj];
				}
			}
			if (ii == -1)
				continue;
			Union(i * M + j, ii * M + jj);
		}
	memset(Char, -1, sizeof(Char));
	char Cur = 'a';
	for (int i = 0; i < N * M; i ++)
		if (Char[GetRoot(i)] == -1)
			Char[i] = Char[GetRoot(i)] = Cur ++;
		else
			Char[i] = Char[GetRoot(i)];
	for (int i = 0; i < N; i ++)
	{
		for (int j = 0; j < M - 1; j ++)
			printf("%c ", Char[i * M + j]);
		printf("%c\n", Char[i * M + M - 1]);
	}
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d:\n", Case);
		Work();
	}
	
	return 0;
}
