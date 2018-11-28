#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <map>
#include <set>

using namespace std;


int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int nt;
    scanf("%d", &nt); 
    for (int t = 1; t <= nt; ++t) {
        int n, minv = 1000000000;
        cin >> n;
        int sum = 0, s = 0;
        for (int i = 0; i < n; ++i) {
            int add;
            cin >> add;
            sum ^= add;
            s += add;
            minv = min(minv, add);
        }
        printf(sum ? "Case #%d: NO\n"  : "Case #%d: %d\n", t, s - minv);
    }
}
