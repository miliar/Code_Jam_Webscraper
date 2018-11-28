#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    ifstream in("A.in");
    ofstream out("A.out");

    int tests;
    in >> tests;
    for (int t = 1; t <= tests; ++t) {
        int teams;
        in >> teams;

        vector<string> schedules(teams);
        for (int i = 0; i < teams; ++i)
            in >> schedules[i];

        vector<double> wp(teams), owp(teams), oowp(teams);

        for (int i = 0 ; i < teams; ++i) {
            int total = 0;
            int wins  = 0;
            for (int j = 0; j < teams; ++j) {
                total += (schedules[i][j] != '.');
                wins  += (schedules[i][j] == '1');
            }
            wp[i] = (double)wins / (double)total;
        }

        for (int i = 0 ; i < teams; ++i) {
            int opps    = 0;
            double towp = 0;
            for (int j = 0; j < teams; ++j) {
                if (schedules[i][j] != '.') {
                    int total = 0;
                    int wins  = 0;
                    for (int k = 0; k < teams; ++k) {
                        if (i != k) {
                            total += (schedules[j][k] != '.');
                            wins  += (schedules[j][k] == '1');
                        }
                    }
                    towp += (double)wins / (double)total;
                    opps++;
                }
            }
            owp[i] = towp / (double)opps;
        }

        for (int i = 0 ; i < teams; ++i) {
            int opps    = 0;
            double towp = 0;
            for (int j = 0; j < teams; ++j) {
                if (schedules[i][j] != '.') {
                    towp += owp[j];
                    opps++;
                }
            }
            oowp[i] = towp / (double)opps;
        }

        out << "Case #" << t << ":" << endl;
        for (int i = 0; i < teams; ++i) {
            out.precision(12);
            out << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl;
        }

    }
    return 0;
}
