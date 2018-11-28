#include <cstdio>
#include <cstring>


int     n;
char    mat[200][200];

void init()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i ++)
        scanf("%s", mat[i]);
}

int     win[200];
int     lose[200];

double  owp [200];


void solve()
{
    memset(win, 0, sizeof(win));
    memset(lose, 0, sizeof(lose));
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < n; j ++)
            if (mat[i][j] == '1') win[i] ++;
            else if (mat[i][j] == '0') lose[i] ++;

    for (int i = 0; i < n; i ++)
    {
        owp[i] = 0;
        int cc = 0;
        for (int j = 0; j < n; j ++)
        {
            if (mat[i][j] != '.')
            {
                ++ cc;
                int tot = win[j] + lose[j] - 1;
                if (tot)
                {
                    owp[i] += (win[j] - int(mat[j][i] == '1'))/ (double)tot;
                }
            }
        }
        owp[i] /= (double)cc;
    }

    for (int i = 0; i < n; i ++)
    {
        double rpi = 0;
        if (win[i] + lose[i])
            rpi = (double)win[i] / (win[i] + lose[i]) * 0.25;
        rpi += owp[i] * 0.5;
        int op = 0;
        double s = 0.0;
        for (int j = 0; j < n; j ++)
            if (mat[i][j] != '.')
            {
                op ++;
                s += owp[j];
            }
        rpi += s / op * 0.25;
        printf("%.12lf\n", rpi);
    }
}

int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small.out", "w", stdout);

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t ++)
    {
        init();

        printf("Case #%d:\n" , t);
        solve();
    }

    return 0;
}