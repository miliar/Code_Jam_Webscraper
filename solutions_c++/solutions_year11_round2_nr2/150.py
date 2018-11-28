#include <cstdio>
#include <cmath>
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
typedef long double real;

#define maxn (1 << 8)
#define eps 3e-8L

int n, d;
int p[maxn], v[maxn];

int main() {
	int t = 1, tc;
	for(scanf("%d", &tc); t <= tc; t++) {
		printf("Case #%d: ", t);
        scanf("%d %d", &n, &d);
        for(int i = 0; i < n; i++)
            scanf("%d%d", p+i, v+i);

        real l = 0, r = 5e11;
        while(r-l > eps) {
            real m = (l+r) * 0.5;
            real lpos = -1e30;
            int i;
            for(i = 0; i < n; i++) {
                if(lpos < p[i] - m)
                    lpos = p[i] - m;
                real npos = lpos + d * (v[i] - 1.0);
                if(npos - p[i] > m) break;
                lpos = npos + d;
            }
            if(i < n) l = m;
            else r = m;
        }

        printf("%.9Lf\n", r);
	}
	return 0;
}
