#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <utility>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <map>

const int maxn = 510;

int a[maxn][maxn], s[maxn][maxn], best = 0;
char c[maxn][maxn];

int get(int y1, int x1, int y2, int x2) {
    --x1;
    --y1;
    return s[y2][x2] - s[y1][x2] - s[y2][x1] + s[y1][x1];
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int t;
    
    std::cin >> t;
    std::memset(a, 0, sizeof(a));
    for (int ti = 1; ti <= t; ++ti) {
        best = 0;
        int n, m, spam;
        std::cin >> n >> m >> spam;
        for (int i = 1; i <= n; ++i) {
            scanf("%s", c[i]);
        }
        std::memset(a, 0, sizeof(a));
        std::memset(s, 0, sizeof(s));
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= m; ++j) {
                a[i][j] = c[i][j-1]-'0';
            }
        
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                s[i][j] = a[i][j] + s[i-1][j] + s[i][j-1] - s[i-1][j-1];
            }
        }
        
        for (int k = 3; k <= std::min(n, m); ++k) {
            for (int i = 1; i+k-1 <= n; ++i) {
                for (int j = 1; j+k-1 <= m; ++j) {
                    int s1 = get(i, j, i+k-1, j+(k-1)/2) - a[i][j] - a[i+k-1][j];
                    int s2 = get(i, j+k/2, i+k-1, j+k-1) - a[i+k-1][j+k-1] - a[i][j+k-1];
                    int s3 = get(i, j, i+(k-1)/2, j+k-1) - a[i][j]-a[i][j+k-1];
                    int s4 = get(i+k/2, j, i+k-1, j+k-1) - a[i+k-1][j] - a[i+k-1][j+k-1];
                    if (s1 == s2 && s3 == s4) {
                        best = k;
                    }
                }
            }
        }
        if (best > 0)
            std::printf("Case #%d: %d\n", ti, best);
        else 
            std::printf("Case #%d: IMPOSSIBLE\n", ti);
    }


    return 0;
}