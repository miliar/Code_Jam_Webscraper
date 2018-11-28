#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

#define MAXN 100

int N, M;
char map[MAXN][MAXN];
vector<int> con[MAXN * MAXN];
int l[MAXN * MAXN], r[MAXN * MAXN];
char used[MAXN * MAXN];

inline int cod(int x, int y)
{
	return x * M + y;
}

const int dx[4] = {-1, -1, 0, 0};
const int dy[4] = {-1, 1, -1, 1};

inline int pair_up(int k)
{
	if (used[k])
		return 0;
	used[k] = 1;
	vector<int> :: iterator it;

	for (it = con[k].begin(); it != con[k].end(); it++)
		if (r[*it] == -1)
		{
			l[k] = *it;
			r[*it] = k;
			return 1;
		}
	for (it = con[k].begin(); it != con[k].end(); it++)
		if (pair_up(r[*it]))
		{
			l[k] = *it;
			r[*it] = k;
			return 1;
		}
	return 0;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d %d", &N, &M);
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				scanf(" %c", map[i] + j);

		int nr_bad = 0;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				nr_bad += map[i][j] == 'x';
		/*for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
				printf("%c", map[i][j]);
			printf("\n");
		}*/
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
			{
				con[cod(i, j)].clear();
				if (map[i][j] == 'x')
					continue;

				for (int k = 0; k < 4; k++)
				{
					int _i = i + dx[k];
					int _j = j + dy[k];

					if (_i < 0 || _i >= N) continue;
					if (_j < 0 || _j >= M) continue;
					if (map[_i][_j] == 'x')
						continue;
					con[cod(i, j)].push_back(cod(_i, _j));
					con[cod(_i, _j)].push_back(cod(i, j));
					//printf("%d %d - %d -> %d %d - %d\n", i, j, cod(i, j), _i, _j, cod(_i, _j));
				}
			}

		int ok = 0;
		memset(l, -1, sizeof(l));
		memset(r, -1, sizeof(r));
		for (; !ok; )
		{
			ok = 1;

			memset(used, 0, sizeof(used));
			for (int i = 0; i < N; i++)
				for (int j = 1; j < M; j += 2)
					if (!used[cod(i, j)] && l[cod(i, j)] == -1)
						if (pair_up(cod(i, j)))
							ok = 0;
		}
		int Rez = N * M - nr_bad;
		for (int i = 0; i < N; i++)
			for (int j = 1; j < M; j += 2)
			{
				if (l[cod(i, j)] != -1)
					Rez--;
				//printf("%d %d - %d\n", i, j, l[cod(i, j)]);
			}

		printf("Case #%d: %d\n", t, Rez);
	}

	return 0;
}
