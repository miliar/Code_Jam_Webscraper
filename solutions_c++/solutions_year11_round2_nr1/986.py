#include<stdio.h>
#include<string>
#include<math.h>
#include<algorithm>
#include<vector>
#include<stdlib.h>

using namespace std;

int n;
char game[200][200];
double wp[200], owp[200], oowp[200], rpi[200];

void solve()
{
    int i, j, k;
    int win, count;
    double wpcount, teamcount;

    //wp
    for (i = 0; i < n; i ++) {
        win = count = 0;

        for (j = 0; j < n; j ++) {
            if (game[i][j] == '1') {
                win ++;
                count ++;
            }
            else if (game[i][j] == '0') {
                count ++;
            }
        }
        wp[i] = (double)win / count;
    }

    //owp
    for (i = 0; i < n; i ++) {
        wpcount = teamcount = 0;
        for (j = 0; j < n; j ++) {
            if (game[i][j] == '.') continue;

            win = count = 0;
            for (k = 0; k < n; k ++) {
                if (k == i) continue;
                if (game[j][k] == '1') {
                    win ++;
                    count ++;
                }
                else if (game[j][k] == '0') {
                    count ++;
                }
            }
            wpcount += (double)win / count;
            teamcount ++;
        }
        owp[i] = (double)wpcount / teamcount;
    }

    //oowp
    for (i = 0; i < n; i ++) {
        wpcount = teamcount = 0;

        for (j = 0; j < n; j ++) {
            if (game[i][j] == '.') continue;

            wpcount += owp[j];
            teamcount ++;
        }

        oowp[i] = (double)wpcount / teamcount;
    }

    //rpi
    for (i = 0; i < n; i ++) {
        rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
    }
}

int main()
{
    int i, j, k;
    int t, nowt;

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d", &t);
    nowt = 0;
    while (t --) {
        nowt ++;
        scanf("%d", &n);
        for (i = 0; i < n; i ++) {
            scanf("%s", game[i]);
        }

        solve();

        printf("Case #%d:\n", nowt);
        for (i = 0; i < n; i ++) {
            printf("%.20lf\n", rpi[i]);
        }
    }

    return 0;
}