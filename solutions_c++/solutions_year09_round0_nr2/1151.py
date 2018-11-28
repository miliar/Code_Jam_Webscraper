#include <cstdio>
#include <queue>

using namespace std;

int n, m, color;
int alt[105][105];
int chk[105][105];
pair<int, int> flow[105][105];

const int dx[] = {0, -1, 1, 0};
const int dy[] = {-1, 0, 0, 1};

void getFlow(int r, int c, int &fr, int &fc)
{
	fr = fc = -1;

	int minv = alt[r][c];
	for(int i = 0; i < 4; ++i)
	{
		int nr = r + dy[i];
		int nc = c + dx[i];
		if( nr < 1 || nr > n || nc < 1 || nc > m ) continue;
		if( alt[nr][nc] < minv )
		{
			minv = alt[nr][nc];
			fr = nr; fc = nc;
		}
	}
}

void bfs(pair<int, int> sink, int color)
{
	queue< pair<int, int> > q;
	pair<int, int> tmp;
	
	chk[sink.first][sink.second] = color;
	q.push(sink);

	while( !q.empty() )
	{
		tmp = q.front(); q.pop();
		for(int i = 0; i < 4; ++i)
		{
			pair<int, int> tmp2;
			tmp2.first = tmp.first + dy[i];
			tmp2.second = tmp.second + dx[i];

			if( tmp2.first < 1 || tmp2.first > n || tmp2.second < 1 || tmp2.second > m ) continue;
			
			if( flow[tmp2.first][tmp2.second] == tmp )
			{
				chk[tmp2.first][tmp2.second] = color;
				q.push(tmp2);
			}
		}
	}
}

int main()
{
	int r;
	scanf("%d", &r);
	for(int t = 1; t <= r; ++t)
	{
		int i, j;
		scanf("%d %d", &n, &m);
		for(i = 1; i <= n; ++i)
			for(j = 1; j <= m; ++j)
				scanf("%d", &alt[i][j]);

		printf("Case #%d:\n", t);	

		memset(chk, 0, sizeof(chk));
		color = 0;

		for(i = 1; i <= n; ++i)
			for(j = 1; j <= m; ++j)
				getFlow( i, j, flow[i][j].first, flow[i][j].second );
				

		for(i = 1; i <= n; ++i)
			for(j = 1; j <= m; ++j)
				if( !chk[i][j] && flow[i][j].first == -1 )
				{
					bfs(make_pair(i, j), ++color);
				}

		color = 0;
		int part[27] = {0, };
		for(i = 1; i <= n; ++i)
		{
			for(j = 1; j <= m; ++j)
			{
				if( !part[chk[i][j]] ) part[chk[i][j]] = ++color;
				printf("%c%c", part[chk[i][j]] + 'a' - 1, (j == m) ? '\n' : ' ');
			}
		}

	}

	return 0;
}
