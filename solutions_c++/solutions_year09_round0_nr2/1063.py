#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MAXA = 100000000;

int H, W;
int m[128][128];
char f[128][128];
char r[128][128];

int d[4][4] = {
    {-1, 0, 'N', 'S'}, 
    {0, -1, 'W', 'E'},
    {0,  1, 'E', 'W'},
    {1,  0, 'S', 'N'}
};

inline int g(int i, int j)
{
    if (i < 0 || i >= H)
        return MAXA;
    if (j < 0 || j >= W)
        return MAXA;
    return m[i][j];
}

inline char h(int i, int j)
{
    if (i < 0 || i >= H)
        return 0;
    if (j < 0 || j >= W)
        return 0;
    return f[i][j];
}

void color(int i, int j, char c)
{
    if (r[i][j])
        return;
    r[i][j] = c;

    for (int k = 0; k < 4; ++k)
    {
        int ii = i + d[k][0];
        int jj = j + d[k][1];
        if (h(i, j) == d[k][2] || h(ii, jj) == d[k][3]) {
            color(ii, jj, c);
        }
    }
}

int main()
{
    int nCase;
    scanf("%d", &nCase);

    for (int iCase = 1; iCase <= nCase; ++iCase)
    {
        scanf("%d%d", &H, &W);
        for (int i = 0; i < H; ++i)
        {
            for (int j = 0; j < W; ++j)
            {
                scanf("%d", &m[i][j]);
            }
        }

        memset(f, ' ', sizeof(f));

        for (int i = 0; i < H; ++i)
        {
            for (int j = 0; j < W; ++j)
            {
                int a = 100000000;
                for (int k = 0; k < 4; ++k)
                {
                    a = min(a, g(i + d[k][0], j + d[k][1]));
                }
                if (a >= g(i, j))
                    continue;
                for (int k = 0; k < 4; ++k)
                    if (g(i + d[k][0], j + d[k][1]) <= a)
                    {
                        f[i][j] = (char)d[k][2];
                        break;
                    }
            }
        }

        memset(r, 0, sizeof(r));

        char c = 'a';
        for (int i = 0; i < H; ++i)
        {
            for (int j = 0; j < W; ++j)
            {
                if (!r[i][j]) {
                    color(i, j, c++);
                }
            }
        }

        printf("Case #%d:\n", iCase);
        for (int i = 0; i < H; ++i)
        {
            for (int j = 0; j < W; ++j)
            {
                printf("%s%c", j ? " " : "", r[i][j]);
            }
            printf("\n");
        }
    }

    return 0;
}
