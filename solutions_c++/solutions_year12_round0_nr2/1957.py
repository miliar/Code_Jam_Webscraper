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

#define maxn (1 << 7)

int score[maxn];
int tbl[maxn][maxn];

inline void relax(int& a, int b) {
    if(a < b)
        a = b;
}

int main() {
	int t = 1, tc;
	for(scanf("%d", &tc); t <= tc; t++) {
		printf("Case #%d: ", t);
        int n, p, s, i, j;
        scanf("%d%d%d", &n, &s, &p);

        for(i = 0; i < n; i++)
            scanf("%d", &score[i]);

        memset(tbl, 0, sizeof(tbl));

        for(i = 0; i < n; i++)
            for(j = 0; j <= s; j++) {
                relax(tbl[i+1][j], tbl[i][j]);
                if(score[i] >= p + 2*std::max(p-1, 0))
                    relax(tbl[i+1][j], tbl[i][j] + 1);
                else if(j < s && score[i] >= p + 2*std::max(p-2, 0))
                    relax(tbl[i+1][j+1], tbl[i][j] + 1);
            }

        int ans = 0;
        for(j = 0; j <= s; j++)
            relax(ans, tbl[n][j]);

        printf("%d\n", ans);

	}
	return 0;
}
