#include <cstdio>

#define INF 100000

int h, w, m[120][120], visit[120][120], f[120][120], ans[12000];

int t, i, j, k, p, q;

FILE * fp;

int v[4][2] =
    {
        {
        -1, 0
        },
        {
        0, -1
        },
        {
        0, 1
        },
        {
        1, 0
        }
    };

void search(int i, int j)
    {
    if (visit[i][j])
        return;
    visit[i][j] = true;
    int k, x, y, mini = INF, idx = -1;
    for (k = 0; k < 4; k++)
        {
        x = i + v[k][0];
        y = j + v[k][1];
        if (x > -1 && x < h && y > -1 && y < w && m[x][y] < m[i][j]
                && m[x][y] < mini)
            {
            idx = k;
            mini = m[x][y];
            }
        }
    if (idx != -1)
        {
        x = i + v[idx][0];
        y = j + v[idx][1];
        search(x, y);
        f[i][j] = f[x][y];
        }
    }
int main()
    {
    fp = fopen("b.out", "wt");
    scanf("%d", &t);
    for (i = 0; i < t; i++)
        {
        fprintf(fp, "Case #%d:\n", i + 1);
        scanf("%d%d", &h, &w);
        for (j = 0; j < h; j++)
            for (k = 0; k < w; k++)
                scanf("%d", &m[j][k]);
        for (j = 0; j < h; j++)
            for (k = 0; k < w; k++)
                {
                visit[j][k] = false;
                f[j][k] = j * w + k;
                ans[f[j][k]] = -1;
                }
        for (j = 0; j < h; j++)
            for (k = 0; k < w; k++)
                search(j, k);
        p = 0, q = 0;
        for (j = 0; j < h; j++)
            {
            for (k = 0; k < w; k++)
                {
                q = f[j][k];
                if (ans[q] == -1)
                    ans[q] = p++;
                fprintf(fp, "%c ", ans[q] + 'a');
                }
            fprintf(fp, "\n");
            }
        }
    return 0;
    }
