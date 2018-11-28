#include <stdio.h>
int main(){
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, N, L, H, i, j;
    scanf("%d", &T);
    for(int k=1; k<=T; k++){
        int h[200];
        scanf("%d %d %d", &N, &L, &H);
        for(i=0; i<N; i++) scanf("%d", &h[i]);
        for(i=L; i<=H; i++){
            for(j=0; j<N; j++)
                if(i%h[j]!=0 && h[j]%i!=0) break;
            if(j==N) break;
        }
        if(i<=H) printf("Case #%d: %d\n", k, i);
        else printf("Case #%d: NO\n", k);
    }
    return 0;
}
