#include <stdio.h>
#include <vector>
#include <queue>
#include <limits.h>
#define MN 100
using namespace std;
int n, m, c;
int d[MN][MN], r[MN][MN];
vector<pair<int,int> > l[MN][MN];
int dx[4]={-1,0,0,1},dy[4]={0,-1,1,0};
int f(int x, int y)
{return 0<=x&&x<n&&0<=y&&y<m?d[x][y]:INT_MAX;}
void sub(pair<int,int> f)
{
	queue<pair<int,int> > qu;
	pair<int,int> p, q;
	int i;

	qu.push(f); r[f.first][f.second] = c;
	while (!qu.empty()) {
		p = qu.front(); qu.pop();
		for (i = 0; i < l[p.first][p.second].size(); i++) {
			q = l[p.first][p.second][i];
			if (r[q.first][q.second] < 0) {
				qu.push(q); r[q.first][q.second] = c;
			}
		}
	}
}
void process()
{
	int i, j, k, x, y;

	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) l[i][j].clear();
	}
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			x = i; y = j;
			for (k = 0; k < 4; k++) {
				if (f(x,y) > f(i+dx[k],j+dy[k])) {x = i+dx[k]; y = j+dy[k];}
			}
			l[i][j].push_back(make_pair(x,y));
			l[x][y].push_back(make_pair(i,j));
		}
	}
	memset(r,255,sizeof(r)); c = 0;
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			if (r[i][j] < 0) {
				sub(make_pair(i,j)); c++;
			}
			printf("%c ", r[i][j]+'a');
		}
		printf("\n");
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T, t, i, j;

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		scanf("%d%d",&n,&m);
		for (i = 0; i < n; i++) {
			for (j = 0; j < m; j++)
				scanf("%d",&d[i][j]);
		}
		printf("Case #%d:\n", t);
		process();
	}
	return 0;
}