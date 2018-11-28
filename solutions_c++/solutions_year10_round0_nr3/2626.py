#include <stdio.h>

int main () {
    
    int t, r, k, n, g[1005],c,tot,po,co,st;
    
    scanf("%d",&t);
    c = 1;
    while(t>0) {
        tot = 0;
        scanf("%d %d %d",&r,&k,&n);
        for(int i=0;i<n;i++) {
            scanf("%d",&g[i]);
        }
        po = 0;
        for(int i=0;i<r;i++) {
            st = po;
            co = 0;
            while (co + g[po] <= k) {
                co += g[po];
                po++;
                if(po >= n) po = 0;
                if(st == po) break;
            }
            tot += co;
        }        
        
        printf("Case #%d: %d\n",c,tot);
        
        c++;
        t--;
    }
    
    while(getchar()!=EOF);
    return 0;
}
