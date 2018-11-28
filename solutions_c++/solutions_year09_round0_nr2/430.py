#include <cstdio>
#include <cstring>

const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

int n, m;
int tot;
int a[105][105];
int p[10005];
char res[10005];

inline void Init()
{
    for (int i = 0; i < tot; i++)
        p[i] = i;
}

inline int findp(int k)
{
    if (p[k] == k)
        return k;
    else
        return p[k] = findp(p[k]);
}

inline bool isFriend(int i, int j)
{
    return findp(i) == findp(j);
}

inline void setFriend(int i, int j)
{
    p[findp(i)] = findp(j);
}

inline int trans(int i, int j)
{
    return i * m + j;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        scanf("%d%d", &n, &m);
        tot = n * m;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                scanf("%d", &a[i][j]);
        Init();
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                int x = -1, y = -1;
                for (int k = 0; k < 4; k++)
                {
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                        continue;
                    if ((x == -1 || a[nx][ny] < a[x][y]) && a[nx][ny] < a[i][j])
                    {
                        x = nx; y = ny;
                    }
                }
                if (x != -1)
                    setFriend(trans(i, j), trans(x, y));
            }
        }
        memset(res, 0, sizeof(res));
        char ch = 'a';
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
            {
                int curr = trans(i, j);
                if (res[findp(curr)] == 0)
                {
                    res[curr] = res[findp(curr)] = ch++;
                } else res[curr] = res[findp(curr)];
            }
        printf("Case #%d:\n", cas);
        for (int i = 0; i < tot; i++)
        {
            if (i % m != 0)
                putchar(' ');
            if (i % m == 0 && i > 0)
                putchar('\n');
            printf("%c", res[i]);
        }
        putchar('\n');
    }
    return 0;
}
