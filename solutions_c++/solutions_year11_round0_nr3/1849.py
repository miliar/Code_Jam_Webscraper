#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

#define Eo(x) { std::cerr << #x " = " << x << std::endl; }

#define maxn (1 << 10)
#define maxs (1 << 20)

int a[maxn], n;

inline int _xor(int a, int b) { return a ^ b; }

int main() {
    int t, tc;
    for(scanf("%d", &tc), t = 1; t <= tc; ++t) {
        printf("Case #%d:", t);

        scanf("%d", &n);
        for(int i = 0; i < n; i++)
            scanf("%d", a + i);
        std::sort(a, a+n);
        if(std::accumulate(a, a+n, 0, _xor)) printf(" NO\n");
        else printf(" %d\n", std::accumulate(a+1, a+n, 0));
    }
    return 0;
}
