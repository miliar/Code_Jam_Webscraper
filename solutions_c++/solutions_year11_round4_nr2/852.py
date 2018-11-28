#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int w[600][600];
int r, c, d;


int check(int i, int j) {
    int ans = 0;
    for (int k = 2; i + k < r && j + k < c; k++) {
            double px = (double)i + (double)k / 2;
            double py = (double)j + (double)k / 2;
            //printf("%lf %lf\n", px, py);
            double sumx = 0.0;
            double sumy = 0.0;
            for (int i1 = 0; i1 <= k; i1++) {
                for (int j1 = 0; j1 <= k; j1++) {
                    sumx = sumx + (double)w[i + i1][j + j1] * ((double)i + (double)i1 - px);
                    sumy = sumy + (double)w[i + i1][j + j1] * ((double)j + (double)j1 - py);
                }
            }
            sumx = sumx - (double)w[i][j] * ((double)i - px);
            sumx = sumx - (double)w[i + k][j] * ((double)i + (double)k - px);
            sumx = sumx - (double)w[i][j + k] * ((double)i - px);
            sumx = sumx - (double)w[i + k][j + k] * ((double)i + (double)k - px);
            
            sumy = sumy - (double)w[i][j] * ((double)j - py);
            sumy = sumy - (double)w[i + k][j] * ((double)j - py);
            sumy = sumy - (double)w[i][j + k] * ((double)j + (double)k - py);
            sumy = sumy - (double)w[i + k][j + k] * ((double)j + (double)k - py);
            
            if (sumx == 0.0 && sumy == 0.0) {
                ans = max(ans, k);
            }
    }
    //printf("%d %d %d\n", i, j, ans);
    return ans + 1;
}

void solve()
{
    int ans = 0;
    scanf("%d %d %d", &r, &c, &d);
    char cc;
    getchar();
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cc = getchar();
            w[i][j] = cc - '0';
        }
        getchar();
    }
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            ans = max(ans, check(i, j));
        }
    }
    if (ans >= 3)printf("%d\n", ans);
    else printf("IMPOSSIBLE\n");
}
 
int main() {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B.out3", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int i = 1; i <= T; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
