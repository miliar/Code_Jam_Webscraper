#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <numeric>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <ctime>
#include <cctype>
#include <fstream>
using namespace std;

int n, d[100000], l[100000], f[100000], D;

int main() {
    int tott;
    scanf("%d", &tott);
    for (int curt = 0; curt < tott; ++curt) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d%d", &d[i], &l[i]);
        }
        scanf("%d", &D);
        memset(f, 0x3f, sizeof f);
        f[0] = 0;
        bool yes = false;
        for (int i = 0; i < n; ++i) {
            int swing = d[i] + (d[i] - f[i]);
            // printf("%d %d %d\n", i, f[i], swing);
            if (f[i] == 0x3f3f3f3f) continue;
            if (swing >= D) {
                yes = true;
            }
            for (int j = i + 1; j < n; ++j) {
                if (swing >= d[j]) {
                    int holding = max(d[j] - l[j], d[i]);
                    f[j] = min(f[j], holding);
                }
            }
        }
        printf("Case #%d: %s\n", curt + 1, yes ? "YES": "NO");
    }
    return 0;
}
