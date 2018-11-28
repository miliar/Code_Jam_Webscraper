#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int i, j, n, m, t, h, b[200][200];
bool f;
string s[200];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> t;
    for (h = 1; h <= t; ++h) {
        cin >> n >> m;
        for (i = 1; i <= n; ++i)
            cin >> s[i];
        f = true;
        memset(b, 0, sizeof(b));
        for (i = 1; i <= n; ++i)
            for (j = 0; j < m; ++j)
                if (s[i][j] == '#') {
                    if (i + 1 <= n && j + 1 < m &&
                    s[i + 1][j] == '#' && s[i][j + 1] == '#' && s[i + 1][j + 1] == '#') {
                        s[i][j] = '/';
                        s[i + 1][j + 1] = '/';
                        s[i][j] = '/';
                        b[i][j + 1] = 1;
                        s[i + 1][j] = '\\';
                        b[i + 1][j] = 1;
                        s[i][j + 1] = '\\';
                    } else f = false;
                }
        cout << "Case #" << h << ":" << endl;
        if (f) {
            for (i = 1; i <= n; ++i) {
                for (j = 0; j < m; ++j)
                    if (b[i][j] == '1') cout << "\"";
                    else cout << s[i][j];
                cout << endl;
            }
                
        } else
            cout << "Impossible" << endl;
    }

    return 0;
}
