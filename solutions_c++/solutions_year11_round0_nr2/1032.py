#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int g[26][26];
int o[26][26];
char c[26][26];

int cnt[26];

int C;
int D;
int N;
string str;

string res;

int main() {
    freopen("magicka.in", "r", stdin);
    freopen("magicka.out", "w", stdout);
    int tests; cin >> tests;
    for (int testID = 1; testID <= tests; ++testID) {
        memset(g, 0, sizeof(g));
        memset(o, 0, sizeof(o));
        memset(cnt, 0, sizeof(cnt));
        res = "";
        cin >> C;
        for (int i = 0; i < C; ++i) {
            cin >> str;
            g[str[0] - 'A'][str[1] - 'A'] = 1;
            g[str[1] - 'A'][str[0] - 'A'] = 1;
            c[str[0] - 'A'][str[1] - 'A'] = str[2];
            c[str[1] - 'A'][str[0] - 'A'] = str[2];
        }
        cin >> D;
        for (int i = 0; i < D; ++i) {
            cin >> str;
            o[str[0] - 'A'][str[1] - 'A'] = 1;
            o[str[1] - 'A'][str[0] - 'A'] = 1;
        }
        cin >> N;
        cin >> str;
        char last = 'B';
        for (int i = 0; i < N; ++i) {
            if (g[last - 'A'][str[i] - 'A']) {
                cnt[last - 'A']--;
                last = c[last - 'A'][str[i] - 'A'];
                res[res.size() - 1] = last;
                cnt[last - 'A']++;
            } else {
                int found = 0;
                for (int j = 0; j < 26; ++j)
                    if (o[str[i] - 'A'][j] && cnt[j])
                        found = 1;
                if (found) {
                    res = "";
                    last = 'B';
                    memset(cnt, 0, sizeof(cnt));
                } else {
                    cnt[str[i] - 'A']++;
                    last = str[i];
                    res += last;
                }
            }
        }
        cout << "Case #" << testID << ": [";
        for (int i = 0; i < res.size(); ++i) {
            cout << res[i];
            if (i < res.size() - 1) cout << ", ";
        }
        cout << "]" << endl;
    }
    return 0;
}
