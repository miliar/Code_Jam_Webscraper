#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <sstream>
#include <fstream>
using namespace std;

vector<string> games;
int wins[1000];
int matches[1000];
double wp[1000];
double owp[1000];
double oowp[1000];

void solve_test(int test) {
    int n;
    cin >> n;
    games.resize(n);
    for (int i = 0; i < n; ++i) {
        wins[i] = 0;
        matches[i] = 0;
    }
    for (int i = 0; i < n; ++i) {
        cin >> games[i];
        for (int j = i + 1; j < n; ++j) {
            if (games[i][j] == '.') continue;
            else {
                matches[i]++;
                matches[j]++;
                if (games[i][j] == '1') wins[i]++;
                else wins[j]++;
            }
        }
    }
    cout << "Case #" << test << ":" << endl;
    for (int i = 0; i < n; ++i) {
        wp[i] = (double)wins[i]/(double)matches[i];
        owp[i] = 0.0;
        int ops = 0;
        for (int j = 0; j < n; ++j) if (games[i][j] != '.'){
            ++ops;
            if (games[i][j] == '1') {
                owp[i] += wins[j]/(double)(matches[j] - 1);
            }
            else {
                owp[i] += (wins[j]-1)/(double)(matches[j] - 1);
            }
        }
        owp[i] = owp[i] / (double)ops;
    }
    for (int i = 0; i < n; ++i) {
        oowp[i] = 0.0;
        int ops = 0;
        for (int j = 0; j < n; ++j) if (games[i][j]!='.') {
            ++ops;
            oowp[i] += owp[j];
        }
        oowp[i] /= (double)ops;
    }
    cout.setf(ios::fixed);
    cout.precision(8);
    for (int i = 0; i < n; ++i) {
        cout << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
    }
}

int main() {
    int n_tests;
    cin >> n_tests;
    for (int test = 1; test <= n_tests; ++test) {
        solve_test(test);
    }
    return 0;
}
