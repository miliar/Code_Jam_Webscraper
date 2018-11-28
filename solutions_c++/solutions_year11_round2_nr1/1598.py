#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define PI 3.1415926535897932384626433832795

const int size = 200;
char matches[size][size];
double wp[size], owp[size], oowp[size];
int cop[size];

int main()
{
    int t, i, tc, j, n, call, cw;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cout.precision(20);

    scanf("%d", &tc);
    for (t = 0; t < tc; t++)
    {
        scanf("%d", &n);
        for (i = 0; i < n; i++)
            scanf("%s", matches[i]);
        for (i = 0; i < n; i++)
        {
            cw = 0;
            call = 0;
            for (j = 0; j < n; j++)
            {
                cw += (matches[i][j] == '1');
                call += (matches[i][j] != '.');
            }
            wp[i] = cw / (call * 1.0);
            cop[i] = call;
        }
        for (i = 0; i < n; i++)
        {
            owp[i] = 0;
            for (j = 0; j < n; j++)
                owp[i] += (wp[j] * cop[j] - (matches[j][i] == '1')) / (cop[j] - 1) * (matches[i][j] != '.');
            owp[i] /= cop[i];
        }
        for (i = 0; i < n; i++)
        {
            oowp[i] = 0;
            for (j = 0; j < n; j++)
                oowp[i] += owp[j] * (matches[i][j] != '.');
            oowp[i] /= cop[i];
        }
        cout << "Case #" << t + 1 << ":" << endl;
        for (i = 0; i < n; i++)
        {
            cout << wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25 << endl;
           //cerr << wp[i] << ' ' << owp[i] << ' ' << oowp[i] << endl;
        }
    }

    return 0;
}
