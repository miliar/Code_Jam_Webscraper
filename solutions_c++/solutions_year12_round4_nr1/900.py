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

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }

typedef long long int64;

#define maxn (1 << 14)

int d[maxn], l[maxn], D, n, tbl[maxn];

inline void relax(int& a, int b) {
    if(a < b) a = b;
}

int main() {
	int t = 1, tc;
	for(scanf("%d", &tc); t <= tc; t++) {
		printf("Case #%d: ", t);

        scanf("%d", &n);
        for(int i = 0; i < n; i++)
            scanf("%d%d", &d[i], &l[i]);
        scanf("%d", &D);
        d[n] = D;
        l[n] = D;

        memset(tbl, -1, sizeof(tbl));
        assert(d[0] <= l[0]);
        tbl[0] = d[0];

        for(int i = 0; i < n; i++)
            for(int j = i+1; j <= n; j++)
                if(tbl[i] >= d[j]-d[i])
                    relax(tbl[j], std::min(d[j]-d[i], l[j]));

        printf(tbl[n] >= 0 ? "YES\n" : "NO\n");
	}
	return 0;
}
