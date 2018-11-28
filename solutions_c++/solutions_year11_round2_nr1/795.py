#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;

int N;
vector<string> games;

void solve() {
    vector<double> wp(N, 0.0), owp(N, 0.0), oowp(N, 0.0);
    vector<pii> stats(N);

    for (int i = 0; i < N; ++i) {
        int total = 0, wins = 0;

        for (int j = 0; j < N; ++j)
            if (games[i][j] != '.') {
                total++;
                wins += (games[i][j] == '1');
            }

        stats[i] = make_pair(wins, total);
        wp[i] = total == 0 ? 0.0 : static_cast<double>(wins) / total;
    }

    for (int i = 0; i < N; ++i) {
        owp[i] = 0.0;
        int n = 0;

        for (int j = 0; j < N; ++j)
            if (games[i][j] != '.') {
                int wins = stats[j].first;
                int total = stats[j].second-1;

                wins -= (games[j][i] == '1');

                owp[i] += total == 0 ? 0.0 : static_cast<double>(wins) / total;
                n++;
            }

        if (n > 0)
            owp[i] /= n;
    }

    for (int i = 0; i < N; ++i) {
        oowp[i] = 0.0;
        int cnt = 0;

        for (int j = 0; j < N; ++j)
            if (games[i][j] != '.')
                oowp[i] += owp[j], cnt++;

        if (cnt > 0)
            oowp[i] /= cnt;
    }

    for (int i = 0; i < N; ++i)
        printf("%.8lf\n", 
               0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i) {
        cin >> N;
        games.clear();
  
        for (int j = 0; j < N; ++j) {
            string s;
            cin >> s;

            games.push_back(s);
        }

        cout << "Case #" << i+1 << ":\n";
        solve();
    }

    return 0;
}
