#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <map>
#include <set>

using namespace std;

char c[105];
int p[105];

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int nt;
    scanf("%d", &nt); 
    for (int t = 1; t <= nt; ++t) {
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i)
            cin >> c[i] >> p[i];
        for (int k = 0, to = 0, tb = 0, po = 1, pb = 1; k < n; ++k) {
            if (c[k] == 'O') {
                to = max(tb + 1, to + abs(po - p[k]) + 1);
                po = p[k];
            } else {
                tb = max(to + 1, tb + abs(pb - p[k]) + 1);
                pb = p[k];
            }
            if (k == n - 1) printf("Case #%d: %d\n", t, max(to, tb));
        }
    }
}
