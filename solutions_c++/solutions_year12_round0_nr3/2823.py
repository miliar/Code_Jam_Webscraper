#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <cstdio>
#include <set>

using namespace std;
const int N = 2000000;
set<int> g[N + 1];
int ten[10];

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
//    freopen("in", "r", stdin);
//    freopen("out", "w", stdout);

    int T, A, B;
    int testcases = 0;
    // init

    ten[0] = 1;
    for (int i = 1; i < 10; ++ i) ten[i] = 10 * ten[i - 1];

    for (int i = 1; i <= N; ++ i) {
        int digits[10];
        int len = 0, ti = i;
        while (ti) digits[len++] = ti % 10, ti /= 10;
        for (int j = 0; j < len; ++ j) {
            int sum = 0;
            for (int k = 0; k < len; ++ k) {
                sum += digits[(k + j) % len] * ten[k];
            }
//            cout << sum << endl;
            if (sum > i) g[i].insert(sum);
        }
    }
//    for (int i = 1; i <= 200; ++ i) if (g[i].size()) {
//        for (int j = 0; j < g[i].size(); ++ j)
//            cout << i << " " << g[i][j] << endl;
//    }
    cin >> T;

    while (T --) {
//        cout << "--------------------------------" << endl;
        cin >> A >> B;
        int cnt = 0;
        for (int i = A; i <= B; ++ i)
            for (set<int>::iterator j = g[i].begin(); j != g[i].end(); ++ j)
                if (*j <= B) {
                    ++ cnt;
//                    cout << i << " " << g[i][j] << endl;
                }
        cout << "Case #" << ++ testcases << ": " << cnt << endl;
    }
    return 0;
}
