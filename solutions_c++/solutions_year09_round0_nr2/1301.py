#define LOCAL

#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>

#include <algorithm>
#include <memory>
#include <string>
#include <vector>
#include <map>
#include <iostream>

#define TASK "b"
#define PB(x) push_back(x)
#define MP(x, y) make_pair(x, y)

using namespace std;

#define MAXN 500

int T, H, W;
int a[MAXN][MAXN];
pair<int, int> p[MAXN][MAXN];
char color[MAXN][MAXN];
const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

pair<int, int> get_p(pair<int, int> v)
{
	int i = v.first;
	int j = v.second;

	if (p[i][j] == v)
		return MP(i, j);
	p[i][j] = get_p(p[i][j]);                    
	return p[i][j];
}

void link(pair<int, int> u, pair<int, int> v)
{
	u = get_p(u);
	v = get_p(v);

	if (rand() % 2)			
		p[u.first][u.second] = v;
	else
		p[v.first][v.second] = u;
}

bool ok(int x, int y)
{
	if (x >= 0 && x < H && y >= 0 && y < W)
		return true;
	else
		return false;
}

int main()
{
	#ifdef LOCAL
		freopen(TASK ".in", "rt", stdin);
		freopen(TASK ".out", "wt", stdout);
	#endif
	srand(time(0));

	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d%d", &H, &W);
		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++)
				scanf("%d", &a[i][j]);
		
		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++)
				p[i][j] = MP(i, j);

		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++)
			{
				int mmin = a[i][j];
				for (int k = 0; k < 4; k++)
					if (ok(i + dx[k], j + dy[k]))
						mmin = min(mmin, a[i + dx[k]][j + dy[k]]);

				if (mmin >= a[i][j])
					continue;
				for (int k = 0; k < 4; k++)
					if (ok(i + dx[k], j + dy[k]) && a[i + dx[k]][j + dy[k]] == mmin)
					{
						link(MP(i, j), MP(i + dx[k], j + dy[k]));
						break;
					}
			}

		char counter = 'a';

		memset(color, 0, sizeof(color));
		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++)
			{
				pair<int, int> pp = get_p(MP(i, j));
				if (color[pp.first][pp.second] == 0)
					color[pp.first][pp.second] = counter++;
				color[i][j] = color[pp.first][pp.second];
			}
		printf("Case #%d:\n", t);	
		for (int i = 0; i < H; i++)			
			for (int j = 0; j < W; j++)
				printf("%c%c", color[i][j], " \n"[j == W - 1]);
	}

	return 0;
}
