#include <cstdio>
#include <cstring>

const int limitSize = 220;


int n;
int mat[limitSize][limitSize];

int mx, my;

void update(int x, int y)
{
    if (x > mx) mx = x;
    if (y > my) my = y;
}

void init()
{
    scanf("%d", &n);
    memset(mat, 0, sizeof(mat));
    mx = my = 0;
    while (n --)
    {
        int x1, x2, y1, y2;
        scanf("%d%d%d%d", &y1, &x1, &y2, &x2);
        for (int i = x1; i <= x2; i ++)
            for (int j = y1; j <= y2; j ++)
                mat[i][j] = 1;

        update(x2, y2);
    }
}

void solve()
{
    bool has = 1;

    int round = 0;
    int i,j;
    while (has)
    {
        ++ round;

        int lmx = mx;
        int lmy = my;
        mx = my = 0;
        has = 0;

        for (i = lmx; i > 0; i --)
            for (j = lmy; j > 0; j --)
            {
                if (mat[i][j] && ! mat[i][j-1] && ! mat[i-1][j])
                    mat[i][j] = 0;
                if (!mat[i][j] && mat[i][j-1] && mat[i-1][j])
                    mat[i][j] = 1;

                if (mat[i][j])
                {
                    update(i, j);
                    has = 1;
                }
            }
    }

    printf("%d\n", round);
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("c-small.out", "w", stdout);

    int T, t;
    scanf("%d", &T);

    for (t = 1; t <= T; t ++)
    {
        init();
        printf("Case #%d: ", t);

        solve();
    }

    return 0;
}
