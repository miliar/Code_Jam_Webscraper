#include <vector>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
using namespace std;

#define N 10005

int n, tar;
int d[N], l[N];
set < int > v[N];

bool solve() {
    v[0].insert(d[0]);
    d[n++] = tar;
    for (int i = 0; i < n; ++i)
        for (set < int >::iterator it = v[i].begin(); it != v[i].end(); ++it) {
            for (int j = i + 1; j < n && d[j] - d[i] <= *it; ++j) {
                if (j == n - 1) return true;
                v[j].insert(min(d[j] - d[i], l[j]));
            }
        }
    return false;
}

int main() {
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d %d", &d[i], &l[i]);
            v[i].clear();
        }
        scanf("%d", &tar);
        printf("Case #%d: %s\n", ++cas, solve() ? "YES" : "NO");
    }
    return 0;
}
