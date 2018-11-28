#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int gao[1 << 7][1 << 7][2];
int gd[0x20][2];
int main()
{
    int T;
    for (int i = 2; i <= 28; ++i){
        gd[i][0] = i/3 + (i % 3 != 0);
        gd[i][1] = i/3 + 1 + (i % 3 == 2);
        //printf("%d:%d %d\n", i, gd[i][0], gd[i][1]);
    }
    gd[1][0] = 1;
    gd[29][0] = gd[30][0] = 10;
    scanf("%d", &T);
    for (int CT = 1; CT <= T; ){
        printf("Case #%d: ", CT++);
        int n, s, p, ai, ans;
        ans = 0;
        scanf("%d%d%d", &n, &s, &p);
        memset(gao, 0, sizeof 0);
        for (int i = 1; i <= n; ++i){
            scanf("%d", &ai);
            if (ai >= 2 && ai <= 28){
                for (int j = 0; j <= s; ++j){
                    gao[i][j][0] = max(gao[i-1][j][0], gao[i-1][j][1]) + (gd[ai][0] >= p);
                    if (j >= 1)
                        gao[i][j][1] = max(gao[i-1][j-1][0], gao[i-1][j-1][1]) + (gd[ai][1] >= p);
                    //printf("%d %d %d %d\n", i, j, );
                }
            }else{
                for (int j = 0; j <= s; ++j){
                    gao[i][j][0] = gao[i-1][j][0];
                    gao[i][j][1] = gao[i-1][j][1];
                }
                ans += gd[ai][0] >= p;
            }
        }
        printf("%d\n", ans + max(gao[n][s][0], gao[n][s][1]));
    }
}