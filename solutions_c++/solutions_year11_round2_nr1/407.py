#include <string.h>
#include <iostream>
#include <cstdio>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <cmath>
#include <string>
#include <map>
#include <cassert>
#include <queue>

using namespace std;

#define forn(i, n)  for (int i = 0; i < int(n); i++)

string r[2000];
int n;

vector<double> wp, owp, oowp;
vector<int> tots, wins;

void read()
{
    cin >> n;
    forn(i, n)
        cin >> r[i];
}

void process()
{
    wp = owp = oowp = vector<double>(n, 0);
    tots = wins = vector<int>(n, 0);

    forn(i, n)
    {
        int tot = 0;
        int win = 0;
        forn(j, n)
            if (r[i][j] != '.')
            {
                tot++;
                win += (r[i][j] == '1');
            }
        wp[i] = (tot == 0 ? 0 : double(win) / tot);
        tots[i] = tot;
        wins[i] = win;
    }

    forn(i, n)
    {
        double sum = 0, tot = 0;
        forn(j, n)
            if (r[i][j] != '.')
            {
                tot++;
                if (tots[j] > 1)
                {
                    if (r[j][i] == '1')
                    {
                        sum += double(wins[j] - 1) / (tots[j] - 1);
                    }
                    else
                    {
                        sum += double(wins[j]) / (tots[j] - 1);
                    }
                }
            }
        owp[i] += (tot == 0 ? 0 : sum / tot);
    }

    forn(i, n)
    {
        double sum = 0;
        int tot = 0;
        forn(j, n)
            if (r[i][j] != '.')
            {
                tot++;
                sum += owp[j];
            }
        oowp[i] = (tot == 0 ? 0 : sum / tot);
    }
    printf("\n");
    forn(i, n)
        printf("%.10lf\n", wp[i] / 4 + owp[i] / 2 + oowp[i] / 4);
}

int main(int argc, char* argv[])
{
    freopen("input.txt", "rt", stdin);
    
    int cases;
    scanf("%d", &cases);

    int from = (argc > 1 ? atoi(argv[1]) : 1);
    int to = (argc > 2 ? atoi(argv[2]) : cases);

    for (int i = 1; i <= cases; i++)
    {
        read();
        if (from <= i && i <= to)
        {
            printf("Case #%d:", i);
            process();
        }
    }

    return 0;
}

