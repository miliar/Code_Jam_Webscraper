#include <iostream>

using namespace std;

const int MAXN = 110, MAXM = MAXN * MAXN;
int n, m, tot, now, p, x, y, t1, t2, kases, kase;
int a[MAXN][MAXN], q[MAXM], head[MAXM], adj[MAXM * 4], next[MAXM * 4], v[MAXM];
int px[4] = {-1, 0, 0, 1}, py[4] = {0, -1, 1, 0};

void add_edge(int x, int y)
{
    adj[tot] = y;
    next[tot] = head[x];
    head[x] = tot;
    ++tot;
}

void bfs(int x)
{
    int qs, qe, temp;
    qs = 0;
    qe = 0;
    q[qs] = x;
    v[q[qs]] = now;
    while (qs <= qe)
    {
        temp = head[q[qs]];
        while (temp != -1)
        {
            if (!v[adj[temp]])
            {
                v[adj[temp]] = now;
                ++qe;
                q[qe] = adj[temp];
            }
            temp = next[temp];
        }
        ++qs;
    }
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%d", &kases);
    for (int kase = 0; kase != kases; ++kase)
    {
    printf("Case #%d:\n", kase + 1);

    scanf("%d%d", &n, &m);
    for (int i = 0; i != n; ++i)
        for (int j = 0; j != m; ++j)
            scanf("%d", &a[i][j]);

    tot = 0;
    for (int i = 0; i != n * m; ++i)
        head[i] = -1;
    memset(next, 0, sizeof(next));
    memset(adj, 0, sizeof(adj));

    for (int i = 0; i != n; ++i)
        for (int j = 0; j != m; ++j)
        {
            p = 4;
            for (int k = 0; k != 4; ++k)
            {
                x = i + px[k];
                y = j + py[k];
                if (x < 0 || x >= n || y < 0 || y >= m) continue;
                if (a[x][y] >= a[i][j]) continue;
                if (p == 4 || a[x][y] < a[i + px[p]][j + py[p]]) p = k;
            }
            if (p != 4)
            {
                x = i + px[p];
                y = j + py[p];
                t1 = i * m + j;
                t2 = x * m + y;
                add_edge(t1, t2);
                add_edge(t2, t1);
            }
        }

    memset(v, 0, sizeof(v));
    now = 0;
    for (int i = 0; i != n * m; ++i)
    {
        if (!v[i])
        {
            ++now;
            bfs(i);
        }
    }
    for (int i = 0; i != n; ++i)
    {
        for (int j = 0; j != m; ++j)
        {
            if (j != 0) printf(" ");
            printf("%c", char('a'+v[i*m+j]-1));
        }
        printf("\n");
    }

    }
    return 0;
}
