#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

const int MAXN = 110;

int Win[MAXN], Op[MAXN];
double WP[MAXN], OWP[MAXN], OOWP[MAXN];
string s[MAXN];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int casT, n;

    cin >> casT;
    for (int cases = 1; cases <= casT; ++cases)
    {
        cin >> n;
        for (int i = 0; i < n; ++i)
        {
            cin >> s[i];
        }
        for (int i = 0; i < n; ++i)
        {
            Win[i] = 0;
            Op[i] = 0;
        }
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (s[i][j] == '1') {
                    Win[i]++;
                }
                if (s[i][j] != '.') {
                    Op[i]++;
                }
            }
        }
        for (int i = 0; i < n; ++i)
        {
            WP[i] = (double)Win[i] / Op[i];
        }
        for (int i = 0; i < n; ++i)
        {
            OWP[i] = 0.0;
            for (int j = 0; j < n; ++j)
            {
                if (s[i][j] == '1')
                {
                    OWP[i] += (double)Win[j] / (Op[j] - 1);
                }
                else if (s[i][j] == '0')
                {
                    OWP[i] += (double)(Win[j] - 1) / (Op[j] - 1);
                }
            }
            OWP[i] /= Op[i];
        }
        for (int i = 0; i < n; ++i)
        {
            OOWP[i] = 0.0;
            for (int j = 0; j < n; ++j)
            {
                if (s[i][j] != '.')
                {
                    OOWP[i] += OWP[j];
                }
            }
            OOWP[i] /= Op[i];
        }
        cout << "Case #" << cases << ":" << endl;
        for (int i = 0; i < n; ++i)
        {
            printf("%.8f\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
            //cout << setprecision(8) << 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i] << endl;
        }
    }
    return 0;
}
