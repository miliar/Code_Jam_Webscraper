#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
    freopen("D:\\TopCoder\\gcj2011\\QR\\A.in", "r", stdin);
    freopen("D:\\TopCoder\\gcj2011\\QR\\A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    
    for (int ca = 1; ca <= T; ca++) {
        int n;
        scanf("%d", &n);
        char cc[10];
        int color[n], pos[n];
        for (int i = 0; i < n; i++) {
            scanf("%s %d", cc, &pos[i]);
            if (cc[0] == 'O') color[i] = 0;
            else if (cc[0] == 'B') color[i] = 1;
            else printf("Error\n");
        }
        
        int at[2], t[2];
        at[0] = at[1] = 1; t[0] = t[1] = 0;
        int ans = 0;
        
        for (int i = 0; i < n; i++) {
            t[ color[i] ] += abs(pos[i] - at[ color[i] ])+1;
            at[ color[i] ] = pos[i];
            //printf("= %d : at %d  time=%d\n", color[i], at[ color[i] ], t[ color[i] ]);
            if (t[ color[i] ] <= ans) t[ color[i] ] = ans+1;
            ans = t[ color[i] ];
            //printf("==== %d\n", ans);
        }
        
        printf("Case #%d: %d\n", ca, ans);
    }
            
    fclose(stdin);
    fclose(stdout);
    return 0;
}

