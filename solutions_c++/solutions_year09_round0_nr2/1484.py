#include <stdio.h>
#include <algorithm>

using namespace std;

#define PII pair<int, int>
#define x first
#define y second
#define mp make_pair

int T, M, N, mat[128][128];
int tata[128*128], rang[128*128];
PII p[128*128];
char en[128*128];

int dx[4] = {-1, 0, 0, +1};
int dy[4] = {0, -1, +1, 0};

int cmp(const PII &a, const PII &b)
{ return mat[a.x][a.y] < mat[b.x][b.y]; }

int find_set(int x)
{
	if (x != tata[x])
		tata[x] = find_set(tata[x]);
	return tata[x];
}

void unite(int x, int y)
{
	if (rang[x] < rang[y])
		tata[x] = y;
	else
	{
		tata[y] = x;
		rang[y] += (rang[x] == rang[y]);
	}
}

int main()
{
	int tst = 1, i, j, k, sx, sy, ord;
	int small, ssx = -1, ssy = -1;
	int i1, i2;
	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	for (scanf("%d", &T); tst <= T; ++tst)
	{
		scanf("%d %d", &M, &N);
		for (i = 1; i <= M; ++i)
			for (j = 1; j <= N; ++j)
				scanf("%d", &mat[i][j]);

		int el = 0;
		for (i = 1; i <= M; ++i)
			for (j = 1; j <= N; ++j)
				p[el++] = mp(i, j);
		sort(p, p+el, cmp);
				
		for (i = 0; i < M * N; ++i)
			tata[i] = i,
			rang[i] = 1;
			
		for (i = 0; i < el; ++i)
		{
			small = 10001;
			for (k = 0; k < 4; ++k)
			{
				sx = p[i].x + dx[k];
				sy = p[i].y + dy[k];
				if (sx >= 1 && sy >= 1 && sx <= M && sy <= N)
					if (mat[sx][sy] < small)
						small = mat[sx][sy],
						ssx = sx, ssy = sy;
			}
			if (small < mat[p[i].x][p[i].y])
			{
				ord = (p[i].x-1) * N + (p[i].y-1);
				i1 = find_set(ord);
				
				ord = (ssx-1) * N + (ssy-1);
				i2 = find_set(ord);
				
				if (i1 != i2)
					unite(i1, i2);
			}
		}
		
		printf("Case #%d:\n", tst);
		for (i = 0; i < M * N; ++i)
			en[i] = ' ';
		char let = 'a';
		for (i = 1; i <= M; ++i)
		{
			for (j = 1; j <= N; ++j)
			{
				i1 = find_set((i-1) * N + (j-1));
				if (en[i1] == ' ')
					en[i1] = let++;
				printf("%c ", en[i1]);
			}
				
			printf("\n");	
		}			
	}
	
	return 0;
}
