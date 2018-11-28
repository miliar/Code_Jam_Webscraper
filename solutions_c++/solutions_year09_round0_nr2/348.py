#include <cstdio>
#include <queue>
#include <utility>
#include <map>

using namespace std;

int R, C;
int data[101][101];
const int ways[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int flow[101][101];
int remap[101][101];
map<int, char> did;

void go(int r, int c, int v)
{
	queue< pair<int, int> > que;
	que.push(make_pair(r, c));
	remap[r][c] = v;

	for (;!que.empty();)
	{
		pair<int, int> pl = que.front();
		que.pop();
		int i;
		for (i = 0;i < 4;i++)
		{
			int nr, nc;
			nr = pl.first + ways[i][0];
			nc = pl.second + ways[i][1];

			if (nr < 0 || nr >= R || nc < 0 || nc >= C)
				continue;
			if (flow[nr][nc] == -1)
				continue;

			int xr, xc;
			xr = nr + ways[flow[nr][nc]][0];
			xc = nc + ways[flow[nr][nc]][1];
			if (xr == pl.first && xc == pl.second)
			{
				remap[nr][nc] = v;
				que.push(make_pair(nr, nc));
			}
		}
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	int ti;
	for (ti = 0;ti < t;ti++)
	{
		scanf("%d %d", &R, &C);
		int i, j, k;
		for (i = 0;i < R;i++)
			for (j = 0;j < C;j++)
				scanf("%d", &data[i][j]);
	
		for (i = 0;i < R;i++)
		{
			for (j = 0;j < C;j++)
			{
				int mv = data[i][j];
				int md = -1;
				for (k = 0;k < 4;k++)
				{
					int nr = i + ways[k][0];
					int nc = j + ways[k][1];
					if (nr < 0 || nr >= R || nc < 0 || nc >= C)
						continue;
					if (mv > data[nr][nc])
					{
						mv = data[nr][nc];
						md = k;
					}
				}
				flow[i][j] = md;
			}
		}

		int bc = 0;
		for (i = 0;i < R;i++)
			for (j = 0;j < C;j++)
				if (flow[i][j] == -1)
					go(i, j, bc++);


		printf("Case #%d:\n", ti + 1);
		did.clear();
		for (i = 0;i < R;i++)
		{
			for (j = 0;j < C;j++)
			{
				if (did.find(remap[i][j]) == did.end())
					did.insert(make_pair(remap[i][j], 'a' + did.size()));
				printf("%c ", did[remap[i][j]]);
			}
			printf("\n");
		}
	}
	return 0;
}
