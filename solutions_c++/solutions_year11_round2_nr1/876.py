#include <vector>
#include <set>
#include <map>
#include <deque>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <iostream>

using namespace std;

int main ()
{
    int T, N;
    int amount; // counter
    vector<vector<int> > table;
    vector<double> total_wins, total_games;
    vector<double> owp; // opponent winning percentage
    vector<double> oowp; // opponent opponents winning percentage
    double RPI; // rating percentage index
    string str;

    cin >> T;

    for (int test_num = 0; test_num < T; ++test_num) {
        cout << "Case #" << (test_num + 1) << ":" << endl;

        cin >> N;
        table.assign (N, vector<int> (N, 0));
        total_wins.assign (N, 0);
        total_games.assign (N, 0);
        owp.assign (N, 0);
        oowp.assign (N, 0);
        RPI = 0;

        for (int i = 0; i < N; ++i) {
            cin >> str;

            for (int j = 0; j < N; ++j) {
                if (str[j] == '1') {
                    table[i][j] = 1;
                    ++total_wins[i];
                    ++total_games[i];
                } else if (str[j] == '0') {
                    table[i][j] = -1;
                    ++total_games[i];
                }
            }
        }

        for (int i = 0; i < N; ++i) {
            amount = 0;

            for (int j = 0; j < N; ++j) {
                if (i != j && table[i][j]) {
                    ++amount;

                    if (table[i][j] == -1) {
                        if (total_games[j] != 1)
                            owp[i] += (total_wins[j] - 1) / (total_games[j] - 1);
                    } else {
                        if (total_games[j] != 1)
                            owp[i] += total_wins[j] / (total_games[j] - 1);
                    }
                }
            }

            if (amount != 0)
                owp[i] /= amount;
        }

        for (int i = 0; i < N; ++i) {
            amount =  0;

            for (int j = 0; j < N; ++j) {
                if (i != j && table[i][j]) {
                    ++amount;
                    oowp[i] += owp[j];
                }
            }

            if (amount != 0)
                oowp[i] /= amount;

            if (total_games[i] != 0)
                RPI = 0.25 * (total_wins[i] / total_games[i]);

            RPI += 0.5 * owp[i] + 0.25 * oowp[i];
            printf ("%.9lf\n", RPI);
        }


    }
    return 0;
}
