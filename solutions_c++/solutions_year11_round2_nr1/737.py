#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <iomanip>
#include <map>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    vector<string> res;
    vector<double> wp, owp, oowp;
    int test_n;
    cin >> test_n;
    for (int test_i = 1; test_i <= test_n; ++test_i)
    {
        int n;
        cin >> n;
        res.resize(n);
        wp.resize(n);
        owp.resize(n);
        oowp.resize(n);
        for (int i = 0; i < n; ++i)
            cin >> res[i];

        //calc wp
        for (int i = 0; i < n; ++i)
        {
            int win = 0;
            int total = 0;
            for (int j = 0; j < n; ++j)
            {
                if (res[i][j] != '.')
                {
                    if (res[i][j] == '1')
                        win++;
                    total++;
                }
            }
            if (total == 0)
                wp[i] = 0;
            else
                wp[i] = 1.0 * win / total;
        }

        for (int i = 0; i < n; ++i)
        {
            double sum = 0;
            int total = 0;
            for (int j = 0; j < n; ++j)
            {
                if (res[i][j] != '.')
                {
                    int win2 = 0;
                    int total2 = 0;
                    for (int k = 0; k < n; ++k)
                    {
                        if (res[j][k] != '.' && k != i)
                        {
                            if (res[j][k] == '1')
                                win2++;
                            total2++;
                        }
                    }
                    if (total2 != 0) {
                        sum += 1.0 * win2 / total2;
                        total++;
                    }
                }

            }
            if (total == 0)
                owp[i] = 0;
            else
                owp[i] = sum / total;
        }

        for (int i = 0; i < n; ++i)
        {
            double sum = 0;
            int total = 0;
            for (int j = 0; j < n; ++j)
            {
                if (res[i][j] != '.')
                {
                    sum += owp[j];
                    total++;
                }
            }
            if (total == 0)
                oowp[i] = 0;
            else
                oowp[i] = sum / total;
        }
        
        cout << "Case #" << test_i << ":" << endl;
        for (int i = 0; i < n; ++i)
            cout << fixed << setprecision(12) << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
            



    }
    return 0;
}