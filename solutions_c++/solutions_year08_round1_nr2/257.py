#include <iostream>
using namespace std;
int main() {
    int kase;
    freopen("b.out", "w", stdout);
    scanf("%d", &kase);
    for (int ii = 1; ii <= kase; ++ii){
        printf("Case #%d:", ii);
        int n, m;
        scanf("%d", &n);
        scanf("%d", &m);
        int fav[110][20];
        memset(fav, -1, sizeof(fav));
        for (int i = 1; i <= m; ++i){
            int cnt;
            scanf("%d", &cnt);
            for (int j = 0; j < cnt; ++j){
                int a, b;
                scanf("%d%d", &a, &b);
                fav[i][a - 1] = b;
            }
        }
        int cou[20];
        int len = 1 << n;
        int malt = 100;
        for (int i = 0; i < len; ++i){
            int cmp[20];
            int sum = 0;
            for (int j = 0; j < n; ++j){
                cmp[j] = (i >> j) & 1;
                sum += cmp[j];
            }
            int cnt = 0;
            for (int j = 1; j <= m; ++j){
                int like = 0;
                for (int k = 0; k < n; ++k){
                    if (cmp[k] == fav[j][k]) like = 1;
                }
                if (like)
                    cnt++;
            }
            if (cnt == m){
                if (sum < malt){
                    malt = sum;
                    for (int j = 0; j < n; ++j)
                        cou[j] = cmp[j];
                }
            } 
        }
        if (malt < 100){
            for (int i = 0; i < n; ++i){
                printf(" %d", cou[i]);
            }
            printf("\n");
        }
        else{
            printf(" IMPOSSIBLE\n");
        }
    }
    return 0;
}

