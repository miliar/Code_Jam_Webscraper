#include <cstdio>
#include <algorithm>
using namespace std;

int cnt, n, m, mp[128][128];
char lb[128][128];

char dfs(int, int);

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++) {
		memset(lb, 0, sizeof(lb));
		cnt = 0;
		scanf("%d %d", &n, &m);
		for(int i = 0; i < n; i++) for(int j = 0; j < m; j++) scanf("%d", &mp[i][j]);
		printf("Case #%d:\n", t+1);
		for(int i = 0; i < n; i++) for(int j = 0; j < m; j++) {
			if(lb[i][j] == 0) dfs(i, j);
			printf("%c%c", lb[i][j], j == m-1 ? '\n' : ' ');
		}
	}
	return 0;
}

char dfs(int x, int y)
{
	if(lb[x][y] != 0) return lb[x][y];
	const int DIR[][2] = { { -1, 0 }, { 0, -1 }, { 0, 1 }, { 1, 0 } };
	int p = -1, h = 1<<20;
	for(int i = 0; i < 4; i++) {
		int px = x+DIR[i][0], py = y+DIR[i][1];
		if(px < 0 || px >= n || py < 0 || py >= m || mp[px][py] >= mp[x][y]) continue;
		if(mp[px][py] < h) { p = i; h = mp[px][py]; }
	}
	if(p == -1) { lb[x][y] = cnt+'a'; cnt++; return lb[x][y]; }
	int px = x+DIR[p][0], py = y+DIR[p][1];
	return lb[x][y] = dfs(px, py);	
}

