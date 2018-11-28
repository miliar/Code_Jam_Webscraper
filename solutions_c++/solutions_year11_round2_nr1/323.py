#include <iostream>
#include <iomanip>
#include <cstdio>
using namespace std;

const int Maxn = 105;

typedef long double ld;

int t, n, won[Maxn], played[Maxn];
char info[Maxn][Maxn];
ld owp[Maxn], oowp[Maxn], rpi[Maxn];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        cin >> n;
        for (int i = 0; i < n; i++)
           for (int j = 0; j < n; j++) cin >> info[i][j];
        for (int i = 0; i < n; i++) {
            played[i] = 0; won[i] = 0;
            for (int j = 0; j < n; j++) {
                if (info[i][j] != '.') played[i]++;
                if (info[i][j] == '1') won[i]++;
            }
        }
        for (int i = 0; i < n; i++) {
            ld sum = 0;
            for (int j = 0; j < n; j++)
               if (info[i][j] != '.')
                  sum += ld(won[j] - (info[j][i] == '1')) / ld(played[j] - 1);
            owp[i] = sum / ld(played[i]);
        }
        for (int i = 0; i < n; i++) {
            ld sum = 0;
            for (int j = 0; j < n; j++)
               if (info[i][j] != '.') sum += owp[j];
            oowp[i] = sum / ld(played[i]);
        }
        cout << "Case #" << tc << ":\n";
        for (int i = 0; i < n; i++)
           cout << fixed << setprecision(12) << 0.25 * ld(won[i]) / ld(played[i]) + 0.5 * owp[i] + 0.25 * oowp[i] << endl;
    }
    return 0;
}
