#include <iostream>
#include <vector>
#include <string>
#include <iomanip>


using namespace std;


int main()
{

    int T;
    cin >> T;
    for (int k = 1; k <= T; ++k)
    {
        int n;
        cin >> n;
        vector<string> a(n);
        for (int i = 0; i < n; ++i)
        {
            cin >> a[i];
        }
        vector<double> wp(n);
        for (int i = 0; i < n; ++i)
        {
            int won = 0;
            int total = 0;
            for (int j = 0; j < n; ++j)
            {
                switch (a[i][j])
                {
                    case '1': 
                        ++won;
                    case '0':
                        ++total;
                }
            }
            wp[i] = static_cast<double>(won) / total;
        }

        vector<double> owp(n);

        // cerr << "owps:\n";
        for (int i = 0; i < n; ++i)
        {
            int ops_num = 0;
            for (int j = 0; j < n; ++j)
            {
                if (a[i][j] == '.')
                    continue;
                ++ops_num;
                int won = 0;
                int total = 0;
                for (int g = 0; g < n; ++g)
                {
                    if (g == i)
                        continue;
                    switch (a[j][g])
                    {
                        case '1': 
                            ++won;
                        case '0':
                            ++total;
                    }
                }
                owp[i] += static_cast<double>(won) / total;
            }
            owp[i] /= ops_num;
            // cerr << owp[i] << "\n";
        }

        // cerr << "\n";

        vector<double> oowp(n);

        cout << setprecision(18);
        cout << "Case #" << k << ":\n";

        for (int i = 0; i < n; ++i)
        {
            int ops_num = 0;
            for (int j = 0; j < n; ++j)
            {
                if (a[i][j] == '.')
                    continue;
                ++ops_num;
                oowp[i] += owp[j];
            }
            oowp[i] /= ops_num;
            cout << (0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]) << "\n";
        }
    }
    return 0;
}
