#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
    freopen("D:\\TopCoder\\gcj2011\\QR\\B\\B.in", "r", stdin);
    freopen("D:\\TopCoder\\gcj2011\\QR\\B\\B.out", "w", stdout);
    int T;
    scanf("%d", &T);
    char comb[200][200];
    bool oppo[200][200];
    
    for (int ca = 1; ca <= T; ca++) {
        memset(comb, 0, sizeof(comb));
        memset(oppo, false, sizeof(oppo));
        int C, D, N;
        scanf("%d", &C);
        char pc[10];
        for (int i = 0; i < C; i++) {
            scanf("%s", pc);
            comb[ pc[0] ][ pc[1] ] = pc[2];
            comb[ pc[1] ][ pc[0] ] = pc[2];
        }
        scanf("%d", &D);
        for (int i = 0; i < D; i++) {
            scanf("%s", pc);
            oppo[ pc[0] ][ pc[1] ] = true;
            oppo[ pc[1] ][ pc[0] ] = true;
        }
        scanf("%d", &N);
        char base[N+10], ans[N+10];
        scanf("%s", base);
        int top = 0;
        ans[0] = base[0];
        for (int i = 1; i < N; i++) {
            //printf("== %d\n", i);
            ans[++top] = base[i];
            while (top > 0 && comb[ ans[top] ][ ans[top-1] ]) {
                ans[top-1] = comb[ ans[top] ][ ans[top-1] ];
                --top;
                //ans[top+1] = '\0'; printf("comb %s\n", ans);
            }
            for (int j = 0; j < top; j++) {
                if (oppo[ ans[top] ][ ans[j] ]) {
                    top = -1;
                    //ans[top+1] = '\0'; printf("oppo %s\n", ans);
                }
            }
            //ans[top+1] = '\0'; printf("->%s\n", ans);
        }
        
        
        printf("Case #%d: [", ca);
        for (int i = 0; i <= top; i++) {
            if (i) printf(", ");
            printf("%c", ans[i]);
        }
        printf("]\n");
    }
            
    fclose(stdin);
    fclose(stdout);
    return 0;
}


