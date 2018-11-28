#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    vector < string > dict, set, new_set;
    string L;
    for (int tc = 1; tc <= T; tc++) {
        int n, m;
        cin >> n >> m;
        dict.clear();
        for (int i = 0; i < n; i++) {
            cin >> L;
            dict.push_back(L);
        }
        cout << "Case #" << tc << ": ";
        string best, pattern;
        for (int mc = 0; mc < m; mc++) {
            cin >> L;
            int max = -1;
            for (int wc = 0; wc < dict.size(); wc++) {
                int score = 0;
                pattern = dict[wc];
                for (int i = 0; i < pattern.size(); i++) {
                    pattern[i] = '_';
                }
                set.clear();
                for (int i = 0; i < dict.size(); i++) {
                    if (dict[i].size() == dict[wc].size()) {
                        set.push_back(dict[i]);
                    }
                }
                int cur_ind = 0;
                char cur = L[cur_ind];
                while (set.size() > 1) {
                    new_set.clear();
                    
                    string old_pattern = pattern;
                    for (int i = 0; i < dict[wc].size(); i++) {
                        if (dict[wc][i] == cur) {
                            pattern[i] = cur;
                        }
                    }
                    
                    for (int i = 0; i < set.size(); i++) {
                        bool is_ok = true;
                        for (int j = 0; j < pattern.size(); j++) {
                            is_ok &= (set[i][j] == pattern[j] || pattern[j] == '_');
                            if (pattern[j] == '_' && set[i][j] == cur) is_ok = false;
                        }
                        if (is_ok) {
                            new_set.push_back(set[i]);
                        }
                    }
                    
                    if (old_pattern == pattern && new_set.size() != set.size()) score++;
                    set = new_set;
                    cur_ind++;
                    cur = L[cur_ind];
                }
                if (score > max) {
                    max = score;
                    best = dict[wc];
                }
            }
            cout << best << " ";
        }
        cout << endl;
    }
    return 0;
}
