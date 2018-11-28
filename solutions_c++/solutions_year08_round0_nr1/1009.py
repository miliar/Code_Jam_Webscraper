#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <cassert>

using namespace std;

const int Q = 1000;
const int S = 100;
const int INF = 1000000;

int dp[Q+1][S];

int main() {
    int cases; cin >> cases;
    for (int t = 1; t <= cases; t++) {
        int s; cin >> s;
        string name; getline(cin, name);
        map<string, int> m;
        for (int i = 0; i < s; i++) {
            getline(cin, name);
            while (name[name.size()-1] == '\r') name = name.substr(0, name.size()-1);
            m[name] = i;
        }
        int q; cin >> q;
        getline(cin, name);
        vector<int> v;
        for (int i = 0; i < q; i++) {
            getline(cin, name);
            while (name[name.size()-1] == '\r') name = name.substr(0, name.size()-1);
            map<string, int>::iterator it = m.find(name);
            assert(it != m.end());
            v.push_back(it->second);
        }

        for (int i = 0; i < s; i++) dp[q][i] = 0;
        for (int i = q-1; i >= 0; i--) {
            for (int j = 0; j < s; j++) {
                int best = INF;
                if (v[i] != j) best <?= dp[i+1][j];
                for (int k = 0; k < s; k++) if (k != j) {
                    best <?= 1 + dp[i+1][k];
                }
                dp[i][j] = best;
            }
        }
        int best = INF;
        for (int i = 0; i < s; i++) best <?= dp[0][i];

        cout << "Case #" << t << ": " << best << endl;
    }

    return 0;
}

