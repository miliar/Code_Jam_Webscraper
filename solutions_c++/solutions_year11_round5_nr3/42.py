#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
using namespace std;

int     n, m;
char    mat [120][120];

int     nx  [120][120][2];
int     ny  [120][120][2];

//- | \ /
int     dx  [] = {0, 0, 1, -1, 1, -1, 1, -1};
int     dy  [] = {1, -1, 0, 0, 1, -1, -1, 1};

int getId(char ch)
{
    if (ch == '-') return 0;
    if (ch == '|') return 2;
    if (ch == '\\') return 4;
    if (ch == '/') return 6;
    return 0;
}

int fix(int x, int n)
{
    if (x < 0) x += n;
    return x % n;
}

void init()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i ++)
        scanf("%s", mat[i]);
}


int     list    [20000][2];
int     indeg   [20000];

set<int>    rev [20000];

int encode(int x, int y)
{
    return x * m + y;
}

int     cnt;
bool    mark    [20000];
bool    use    [20000];
int     queue   [20000];
int     head, tail;

void dfs (int u)
{
    use[u] = 1;
    int v = list[u][0];
    if (! mark[v])
    {
        mark[v] = 1;
        for (set<int>::iterator it = rev[v].begin(); it != rev[v].end(); ++ it)
            dfs( *it );
    }
     v = list[u][1];
    if (! mark[v])
    {
        mark[v] = 1;
        for (set<int>::iterator it = rev[v].begin(); it != rev[v].end(); ++ it)
            dfs( *it );
    }
}

void solve()
{
    memset(indeg, 0, sizeof(indeg));
    cnt = n * m;
    for (int i = 0; i < cnt; i ++)
        rev[i].clear();
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++)
        {
            int l, r;

            l = encode(i, j);

            int d = getId(mat[i][j]);
            nx[i][j][0] = fix(i + dx[d], n);
            ny[i][j][0] = fix(j + dy[d], m);

            r = encode(nx[i][j][0],ny[i][j][0]);
            list[l][0] = r;            
            indeg[ r ] ++;
            rev[r].insert( l );

            d ++;
            nx[i][j][1] = fix(i + dx[d], n);
            ny[i][j][1] = fix(j + dy[d], m); 

            r = encode(nx[i][j][1],ny[i][j][1]);
            list[l][1] = r;
            indeg[r] ++;
            rev[r].insert( l );
        }
    
    head = 0; tail = -1;
    for (int i = 0; i < cnt; i ++)
    {
        if (indeg[i] == 0)
        {
            printf("0\n"); return;
        }
        else if (indeg[i] == 1)
        {
            queue[ ++ tail ] = i;
        }
    }
    
    memset(mark, 0, sizeof(mark));
    memset(use, 0, sizeof(use));
    while (head <= tail)
    {
        int u = queue[head ++];
        int x = * rev[u].begin();
        use[x] = 1; mark[u] = 1;
        rev[ list[x][0] ].erase( x );
        rev[ list[x][1] ].erase( x );
        
        if (rev [ list[x][0] ].size() == 0 && ! mark[  list[x][0] ])
        {
            printf("0\n"); return;
        }
        if (rev [ list[x][1] ].size() == 0 && ! mark[  list[x][1] ])
        {
            printf("0\n"); return;
        }
        if (rev [ list[x][0] ].size() == 1 && ! mark[  list[x][0] ])
            queue[ ++ tail ] = list[x][0];
        if (rev [ list[x][1] ].size() == 1 && ! mark[  list[x][1] ])
            queue[ ++ tail ] = list[x][1];
    }

    int ans = 1;
    for (int i = 0; i < cnt; i ++)
        if (! use[i]) {
            dfs( i );
            ans = ans * 2 % 1000003;
        }

    printf("%d\n", ans);
}

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t ++)
    {
        printf("Case #%d: ", t);

        init();
        solve();
    }

    return 0;
}