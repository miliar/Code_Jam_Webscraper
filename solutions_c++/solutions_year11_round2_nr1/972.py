#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

#define rep(i, n) for (int i = 0; i < n; i++)
#define sz(v) (int) ((v).size())

int N;
char field[120][120];
double WP[100], OWP[100], OOWP[100];

double calcWP(int team)
{
    int nWin = 0, nPlay = 0;
    rep(i, N)
    {
        if (field[team][i] != '.')
        {
            nPlay++;
            if (field[team][i] == '1')
                nWin++;
        }
    }

    return (double) nWin / (double) nPlay;
}

double calcOWP(int team)
{
    double sum = 0;
    int nOpp = 0;

    rep(i, N)
    {
        if (i == team)
            continue;
        if (field[team][i] == '.')
            continue;

        nOpp++;

        int nPlay = 0, nWin = 0;
        rep(j, N)
        {
            if (j == team)
                continue;
            if (field[i][j] != '.')
            {
                nPlay++;
                if (field[i][j] == '1')
                    nWin++;
            }
        }

        sum += (double) nWin / (double) nPlay;
    }

    sum /= nOpp;
    return sum;
}

double calcOOWP(int team)
{
    double sum = 0;
    int nOpp = 0;
    rep(i, N)
    {
        if (i == team)
            continue;
        if (field[team][i] == '.')
            continue;

        nOpp++;
        sum += OWP[i];
    }

    return sum / nOpp;
}

int main()
{
    freopen("../DefaultProject/A-large.in", "r", stdin);
    freopen("../DefaultProject/A-large.out", "w", stdout);

    int T;
    scanf("%d", &T);
    rep(tc, T)
    {
        printf("Case #%d:\n", tc + 1);

        scanf("%d", &N);
        gets(field[0]);
        rep(i, N)
        {
            gets(field[i]);
        }

        rep(i, N)
        {
            WP[i] = calcWP(i);
        }
        rep(i, N)
        {
            OWP[i] = calcOWP(i);
        }
        rep(i, N)
        {
            OOWP[i] = calcOOWP(i);
        }

        rep(i, N)
        {
            printf("%.12lf\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
        }
    }

    return 0;
}
