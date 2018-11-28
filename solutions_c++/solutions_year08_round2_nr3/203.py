
#include <stdio.h>

int nprob, prob;
int K, n, d[100];
int lst[1000000];
int ans[1000000];


int main() {
//    freopen("c.in", "r", stdin);
//    freopen("c.out", "w", stdout);
    
    scanf("%d", &nprob);
    for (prob = 1; prob <= nprob; prob++) {
        scanf("%d", &K);
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%d", &d[i]);
        
        for (int i = 0; i < K; i++) {
            int x = K-1-i;
            for (int j = i+1; j >= 1; j--)
                x = (x + j) % (K + 1 - j);
                
            lst[i] = x;
        }
        
        for (int i = 0; i < K; i++)
            ans[lst[i]] = i + 1;
            
        printf("Case #%d:", prob);
        for (int i = 0; i < n; i++)
            printf(" %d", ans[d[i]-1]);
            
        printf("\n");
    }
    
    return 0;
}
