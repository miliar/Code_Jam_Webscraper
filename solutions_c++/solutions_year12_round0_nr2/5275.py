#include<iostream>
#include<cstdio>
using namespace std;

int main() {
    //freopen("B-small-attempt1.in", "r", stdin);
    //freopen("B-small.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int tests;
    cin >> tests;
    for(int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        int n, s, p;
        cin >> n >> s >> p;
        int res = 0;
        for(int i = 0; i < n; ++i) {
            int t;
            cin >> t;
            bool found = 0;
            for(int j = 0; j <= min(4, 3 * p); ++j) {
                if (j < 3 && 3*p - j <= t) {
                    ++res;
                    break;
                }
                else if (j >= 3 && s > 0 && t >= 3 * max(0, p-2) + 2) {
                    --s;
                    ++res;
                    break;
                }
            }
        }
        cout << res << endl;
    }
    return 0;
}
