#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<short> vs;
typedef vector<vs> vvs;
typedef vector<char> vc;
typedef vector<vc> vvc;

void out (vi & v) {
    for (int i = 0; i < v.size(); ++i)
        cerr << v[i] << " ";
    cerr << endl;
}

void out (vvi & v) {
    cerr << endl;
    for (int i = 0; i < v.size(); ++i)
        out(v[i]);
    cerr << endl;
}

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        int n, m;
        cin >> n >> m;
        vector<string> dict(n);
        vvi hash(n, vi(26));
        for (int i = 0; i < n; ++i) {
            cin >> dict[i];
            for (int j = 0; j < dict[i].size(); ++j) {
                hash[i][dict[i][j] - 'a'] += 1 << j;
            }
        }
        vector<string> L(m);
        for (int i = 0; i < m; ++i)
            cin >> L[i];
        cout << "Case #" << test << ":";
        for (int l = 0; l < m; ++l) {
            vvi curhash(n, vi(28));
            for (int i = 0; i < n; ++i) {
                for (int w = 0; w < 26; ++w) {
                    curhash[i][w + 1] = hash[i][L[l][w] - 'a'];
                }
                curhash[i][0] = dict[i].size();
                curhash[i].back() = i;
            }
            sort(curhash.begin(), curhash.end());
//            out(curhash);
            vvi res(n, vi(27, 0));
            int best = curhash.back().back();
            char ma = 0;
            for (int it = n - 2; it >= 0; --it) {
                char cnt = 0;
                if (curhash[it][0] != curhash[it + 1][0]) {
                    res[it] = res.back();
                } else {
                    res[it] = res[it + 1];
                    for (int w = 1; w < 27; ++w) {
                        if (curhash[it][w] != curhash[it + 1][w]) {
                            if (!curhash[it][w])
                                res[it][w] = 1;
                            else res[it][w] = 0;
                            for (int w1 = w + 1; w1 < 27; ++w1)
                                res[it][w1] = 0;
                            break;
                        }
                    }
                    for (int w = 1; w < 27; ++w)
                        cnt += res[it][w];
                }
                if (cnt > ma || cnt == ma && best > curhash[it].back()) {
                    ma = cnt;
                    best = curhash[it].back();
                }
            }
//            out(res);
//            cerr << (int)ma << endl;
            cout << " " << dict[best];
        }
        cout << endl;
    }
    return 0;
}
