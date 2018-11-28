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

int i, j, n, t, h;
double cnt, p, a1[200], a2[200], a3[200], w[200], kol[200];
string s[200];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> t;
    for (h = 1; h <= t; ++h) {
        cin >> n;
        for (i = 1; i <= n; ++i) {
            cin >> s[i];
            cnt = p = 0;
            for (j = 0; j < n; ++j) {
                if (s[i][j] != '.') ++cnt;
                if (s[i][j] == '1') ++p;
            }
            w[i] = p;
            kol[i] = cnt;
            a1[i] = p / cnt;
        }
        for (i = 1; i <= n; ++i) {
            cnt = p = 0;
            for (j = 0; j < n; ++j)
                if (i != j + 1 && s[i][j] != '.') {
                    p += (w[j + 1] - (s[i][j] == '0')) / (kol[j + 1] - 1);
                    ++cnt;
                }
            //if (i == 4) cout << "vot eto " << p << " " << cnt << " " <<  i << endl;
            a2[i] = p / cnt;
        }
        for (i = 1; i <= n; ++i) {
            cnt = p = 0;
            for (j = 0; j < n; ++j) 
                if (s[i][j] != '.') {
                    p += a2[j + 1];
                    ++cnt;
                }
            a3[i] = p / cnt;
        }     
        cout << "Case #" << h << ":" << endl;
        for (i = 1; i <= n; ++i) {
            printf("%.7f\n", 0.25 * a1[i] + 0.5 * a2[i] + 0.25 * a3[i]);
            //cout << a1[i] << " " << a2[i] << " " << a3[i] << endl << endl; 
        }     
    }

    return 0;
}
