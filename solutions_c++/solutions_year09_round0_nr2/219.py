#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

const int inf = 1 << 30;
const int N = 110;
const int dir[5][2] = {{-1,0},{0,-1},{0,1},{1,0}};

int n, m;
int maps[N][N];
int res[N][N];

struct node
{
    vector<pair<int, int> > r;
}p[N][N];

void check(int x, int y)
{
    int pla, Min = inf;
    for(int i = 0; i <= 3; i++)
    {
        int xx = x + dir[i][0];
        int yy = y + dir[i][1];
        if(maps[xx][yy] == -1) continue;

        if(maps[xx][yy] < Min) Min = maps[xx][yy], pla = i;
    }

    if(Min >= maps[x][y]) return ;

    int xx = x + dir[pla][0];
    int yy = y + dir[pla][1];

    p[x][y].r.push_back(make_pair(xx, yy));
    p[xx][yy].r.push_back(make_pair(x, y));
}

void init()
{
    memset(res, -1, sizeof(res));
    memset(maps, -1, sizeof(maps));

    cin>>n>>m;

    for(int i = 1; i <= n; i++)
    {
        for(int  j = 1; j <= m; j++)
        {
            p[i][j].r.clear();
            scanf("%d", &maps[i][j]);
        }
    }

    for(int i = 1; i <= n; i++)
    {
        for(int j = 1; j <= m; j++)
        {
            check(i, j);
        }
    }
}

void bfs(int x, int y, int step)
{
    queue<pair<int, int> > que;
    que.push(make_pair(x, y));

    while(!que.empty())
    {
        int x = que.front().first;
        int y = que.front().second;
        que.pop();

        res[x][y] = step;

        int s = p[x][y].r.size();

        for(int i = 0; i < s; i++)
        {
            int xx = p[x][y].r[i].first;
            int yy = p[x][y].r[i].second;

            if(res[xx][yy] != -1) continue;
            que.push(make_pair(xx, yy));
        }
    }
}

void solve(int tcase)
{
    int cnt = 0;
    for(int i = 1; i <= n; i++)
    {
        for(int j = 1; j <= m; j++)
        {
            if(res[i][j] != -1) continue;
            bfs(i, j, cnt);
            cnt++;
        }
    }

    printf("Case #%d:\n", tcase);

    for(int i = 1; i <= n; i++)
    {
        for(int j = 1; j < m; j++)
        {
            printf("%c ",res[i][j] + 'a');
        }
        printf("%c\n", res[i][m] + 'a');
    }
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin>>T;
    for(int i = 1; i <= T; i++)
    {
        init();
        solve(i);
    }
}
