#include <iostream>
#include <string>
#include <cstdio>
using namespace std;
const int maxn = 100 + 10;
const int debug = 0;

int n;
string match[maxn];
double wp[maxn], owp[maxn], oowp[maxn];
int win[maxn], lose[maxn];

int main(void)
{
    int T;
    cin >> T;
    for (int loop = 1; loop <= T; loop++) {
        cin >> n;
        for (int i = 0; i < n; i++)
            cin >> match[i];
        
        for (int i = 0; i < n; i++) {
            win[i] = lose[i] = 0;
            for (int j = 0; j < n; j++)
                if (match[i][j] == '1')
                    ++win[i];
                else if (match[i][j] == '0')
                    ++lose[i];
        }

        for (int i = 0; i < n; i++) {
            wp[i] = double(win[i]) / double(win[i] + lose[i]);
            owp[i] = 0.0;
            for (int j = 0; j < n; j++)
                if (match[i][j] != '.') {
                    if (match[i][j] == '1')
                        owp[i] += double(win[j]) / double(win[j] + lose[j] - 1);
                    else
                        owp[i] += double(win[j] - 1) / double(win[j] + lose[j] - 1);
                }
            owp[i] /= double(win[i] + lose[i]);
        }

        for (int i = 0; i < n; i++) {
            oowp[i] = 0.0;
            for (int j = 0; j < n; j++)
                oowp[i] += (match[i][j] == '.' ? 0.0 : owp[j]);
            oowp[i] /= double(win[i] + lose[i]);
        }

        cout << "Case #" << loop << ':' << endl;
        for (int i = 0; i < n; i++)
            if (!debug)
                printf("%.10f\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
            else
                cout << wp[i] << ' ' << owp[i] << ' ' << oowp[i] << endl;
    }
    return 0;
}
