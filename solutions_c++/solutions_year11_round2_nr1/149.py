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
typedef double real;

#define maxn (1 << 7)
int n;
char table[maxn][maxn];
real wp[maxn], owp_x[maxn][maxn], owp[maxn], oowp[maxn];

int main() {
	int t = 1, tc;
	for(scanf("%d", &tc); t <= tc; t++) {
		printf("Case #%d:\n", t);
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
            scanf(" %s", table[i]);

        memset(wp, 0, sizeof(wp));
        memset(owp, 0, sizeof(owp));
        memset(owp_x, 0, sizeof(owp_x));
        memset(oowp, 0, sizeof(oowp));

        for(int i = 0; i < n; i++) {
            int cnt = 0;
            for(int j = 0; j < n; j++) {
                if(table[i][j] == '1')
                    wp[i] += 1;
                if(table[i][j] != '.')
                    cnt++;
            }
            if(cnt > 0) wp[i] /= cnt;

            for(int j = 0; j < n; j++) if(i != j && table[i][j] != '.') {
                cnt = 0;
                for(int k = 0; k < n; k++) if(k != i) {
                    if(table[j][k] == '1')
                        owp_x[i][j] += 1;
                    if(table[j][k] != '.')
                        cnt++;
                }
                if(cnt > 0) owp_x[i][j] /= cnt;
            }
            cnt = 0;
            for(int j = 0; j < n; j++) if(i != j && table[i][j] != '.') {
                owp[i] += owp_x[i][j];
                cnt ++;
            }
            if(cnt > 0) owp[i] /= cnt;
        }

        for(int i = 0; i < n; i++) {
            int cnt = 0;
            for(int j = 0; j < n; j++) if(i != j && table[i][j] != '.') {
                oowp[i] += owp[j];
                cnt ++;
            }
            if(cnt > 0) oowp[i] /= cnt;
        }

        for(int i = 0; i < n; i++)
            printf("%.9lf\n", (0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]));
	}
	return 0;
}
