#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int T, t;
    int R, C, D;
    vector<vector<int> > w;
    vector<vector<long long int> > cs_m;
    vector<vector<long long int> > cs_mx;
    vector<vector<long long int> > cs_my;
    long long int sigma_m;
    long long int sigma_mx;
    long long int sigma_my;
    int i, j, k;
    int ans;
    char c;

    cin >> T;
    for (t = 1; t <= T; t++)
    {
        cin >> R >> C >> D;
        w = vector<vector<int> >(R + 1, vector<int>(C + 1, 0));
        for (i = 1; i <= R; i++)
        {
            for (j = 1; j <= C; j++)
            {
                cin >> c;
                w[i][j] = D + (c - '0');
            }
        }

        // precalculate cumulative sums
        cs_m = vector<vector<long long int> >(R + 1, vector<long long int>(C + 1, 0));
        cs_mx = vector<vector<long long int> >(R + 1, vector<long long int>(C + 1, 0));
        cs_my = vector<vector<long long int> >(R + 1, vector<long long int>(C + 1, 0));
        for (i = 1; i <= R; i++)
        {
            for (j = 1; j <= C; j++)
            {
                cs_m[i][j] = cs_m[i][j-1] + (w[i][j]);
                cs_mx[i][j] = cs_mx[i][j-1] + j * (w[i][j]);
                cs_my[i][j] = cs_my[i][j-1] + i * (w[i][j]);
            }
        }
        for (j = 1; j <= C; j++)
        {
            for (i = 1; i <= R; i++)
            {
                cs_m[i][j] += cs_m[i-1][j];
                cs_mx[i][j] += cs_mx[i-1][j];
                cs_my[i][j] += cs_my[i-1][j];
            }
        }

        ans = 0;
        // try all possible blades
        for (i = 1; i <= R - 2; i++)
        {
            for (j = 1; j <= C - 2; j++)
            {
                for (k = 3; k <= min(R + 1 - i, C + 1 - j); k++)
                {
                    sigma_m = cs_m[i+k-1][j+k-1] - cs_m[i+k-1][j-1] - cs_m[i-1][j+k-1] + cs_m[i-1][j-1];
                    sigma_m -= (w[i][j]) + (w[i+k-1][j]) + (w[i][j+k-1]) + (w[i+k-1][j+k-1]);
                    sigma_mx = cs_mx[i+k-1][j+k-1] - cs_mx[i+k-1][j-1] - cs_mx[i-1][j+k-1] + cs_mx[i-1][j-1];
                    sigma_mx -= (w[i][j]) * (j) + (w[i+k-1][j]) * (j) + (w[i][j+k-1]) * (j+k-1) + (w[i+k-1][j+k-1]) * (j+k-1);
                    sigma_my = cs_my[i+k-1][j+k-1] - cs_my[i+k-1][j-1] - cs_my[i-1][j+k-1] + cs_my[i-1][j-1];
                    sigma_my -= (w[i][j]) * (i) + (w[i+k-1][j]) * (i+k-1) + (w[i][j+k-1]) * (i) + (w[i+k-1][j+k-1]) * (i+k-1);
                    if ((2 * sigma_mx == sigma_m * (2 * j + k - 1)) && (2 * sigma_my == sigma_m * (2 * i + k -1)) && (k > ans))
                    {
                        ans = k;
                    }
                }
            }
        }

        cout << "Case #" << t << ": ";
        if (ans < 3)
        {
            cout << "IMPOSSIBLE" << endl;
        }
        else
        {
            cout << ans << endl;
        }
    }

    return 0;
}

