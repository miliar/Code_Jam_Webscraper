#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;

int main()
{
    int i, j, t, n, m, pd, pg;
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cin >> n;
        vector<double> wp(n, 0.0), owp(n, 0.0), oowp(n, 0.0), num(n, 0.0);
        vector<string> games(n, "");
        for (i = 0; i < n; i++) cin >> games[i];

        for (i = 0; i < n; i++) {
            double tot = 0, win = 0;
            for (j = 0; j < n; j++)
                if (games[i][j] != '.') tot++, win += games[i][j] == '1';

            if (tot) wp[i] = win / tot;

            if (tot > 1)
            for (j = 0; j < n; j++)
                if (games[i][j] != '.') {
                    if (games[i][j] == '0') owp[j] += win / (tot - 1);
                    if (games[i][j] == '1') owp[j] += (win - 1) / (tot - 1);
                    num[j]++;
                }
        }

        for (i = 0; i < n; i++) if (num[i]) owp[i] /= num[i];
        for (i = 0; i < n; i++) {
            double opp = 0;
            for (j = 0; j < n; j++)
                if (games[i][j] != '.') oowp[i] += owp[j], opp++;
            oowp[i] /= opp;
        }
        cout.precision(9);
        cout.setf(ios::fixed,ios::floatfield);
        cout << "Case #" << test << ":" << endl;
        for (i = 0; i < n; i++) cout << .25 * wp[i] + .5 * owp[i] + .25 * oowp[i] << endl;
    }
    return 0;
}
