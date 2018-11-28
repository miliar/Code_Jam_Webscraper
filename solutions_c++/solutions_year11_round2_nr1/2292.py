#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define MAXN 128

int n;
    char a[MAXN][MAXN];
int w[MAXN], games[MAXN];
double wp[MAXN], owp[MAXN], oowp[MAXN];

int main (void)
{
    int cases;
    scanf ("%d", &cases);

    for (int caso = 1; caso <= cases; ++caso)
    {
        scanf ("%d", &n);

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                scanf (" %c", &a[i][j]);
            }
        }

        for (int i = 0; i < n; ++i)
        {
            int wins = 0, g = 0;

            for (int j = 0; j < n; ++j)
            {
                if (a[i][j] == '.') continue;
                if (a[i][j] == '0') ++g;
                else
                {
                    ++g;
                    ++wins;
                }
            }

            w[i] = wins;
            games[i] = g;

            wp[i] = ((double) w[i]) / games[i];
        }

        memset(oowp, 0, sizeof(oowp));
        for (int i = 0; i < n; ++i)
        {
            owp[i] = 0;
            int op = 0;

            for (int j = 0; j < n; ++j)
            {
                if (i == j || a[i][j] == '.') continue;

                ++op;

                if (a[i][j] == '0')
                {
                    owp[i] += (((double) w[j] - 1) / (games[j] - 1));
                }
                else if (a[i][j] == '1')
                {
                    owp[i] += (((double) w[j]) / (games[j] - 1));
                }
            }

            owp[i] /= op;

            for (int j = 0; j < n; ++j)
            {
                if (j == i || a[i][j] == '.') continue;

                oowp[j] += owp[i];
            }
        }

        for (int i = 0; i < n; ++i)
        {
            oowp[i] /= games[i];
        }

        printf ("Case #%d:\n", caso);

        for (int i = 0; i < n; ++i)
        {
            printf ("%.8f\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
        }
    }

    return 0;
}

