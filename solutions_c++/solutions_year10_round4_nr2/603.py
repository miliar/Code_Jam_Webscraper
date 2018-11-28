#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int main(int argc, char **argv) {
    int tc; scanf("%d", &tc);
    for(int tci = 0; tci < tc; tci++) {
        int p; scanf("%d", &p);
        static int m[1<<10];
        static int dp0[1<<10][11],minzan0[1<<10];
        static int dp1[1<<10][11],minzan1[1<<10];
        for(int i = 0; i < (1<<p); i++) {
            scanf("%d", &minzan0[i]);
        }
        memset(dp0, 0, sizeof(dp0));
        for(int q = p-1; q >= 0; q--) {
            for(int i = 0; i < (1<<q); i++) {
                int x;
                scanf("%d", &x);
                for(int j = 0; j <= p; j++) {
                    minzan1[i] = min(minzan0[i<<1],minzan0[(i<<1)+1]);
                    dp1[i][j] = x+dp0[i<<1][j]+dp0[(i<<1)+1][j];
                    if(minzan1[i]>j) {
                        dp1[i][j] = min(dp1[i][j],
                                dp0[i<<1][j+1]+dp0[(i<<1)+1][j+1]);
                    }
                }
            }
            for(int i = 0; i < (1<<q); i++) {
                for(int j = 0; j <= p; j++) {
                    dp0[i][j]=dp1[i][j];
                }
                minzan0[i]=minzan1[i];
            }
        }
        printf("Case #%d: %d\n", tci+1, dp1[0][0]);
    }
    return 0;
}

