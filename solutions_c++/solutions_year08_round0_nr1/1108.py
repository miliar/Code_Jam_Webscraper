#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
using namespace std;

const int inf = 1000000000;
int cases, cas = 1;
int n, m;
string names[128];
int mem[1024][128];
string line;

int main() {
    for (cin >> cases; cases--; ) {
        cin >> n; getline(cin, names[0]);
        for (int i = 0; i < n; ++i) {
            getline(cin, names[i]);
        }
        memset(mem, 0xff, sizeof(mem));
        cin >> m; getline(cin, line);
        if (m == 0) {
            printf("Case #%d: 0\n", cas++);
            continue;
        }
        getline(cin, line);
        for (int i = 0; i < n; ++i) if (line != names[i]) {
            mem[0][i] = 0;
        }
        for (int i = 1; i < m; ++i) {
            getline(cin, line);
            for (int j = 0; j < n; ++j) if (mem[i - 1][j] >= 0) for (int k = 0; k < n; ++k) if (line != names[k]) {
                int tmp = mem[i - 1][j] + (j == k ? 0 : 1);
                if (mem[i][k] < 0 || tmp < mem[i][k]) {
                    mem[i][k] = tmp;
                }
            }
        }
        int ans = inf;
        for (int i = 0; i < n; ++i) if (mem[m - 1][i] >= 0) {
            ans = min(ans, mem[m - 1][i]);
        }
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
