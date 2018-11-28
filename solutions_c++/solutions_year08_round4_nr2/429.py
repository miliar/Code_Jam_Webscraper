#include <stdio.h>
#include <math.h>

int main(){
    int ntc,ttc=0;
    scanf("%d", &ntc);
    while (ntc--){
        int found = 0;
        int n,m,a;
        scanf("%d%d%d", &n,&m,&a);
        
        printf("Case #%d: ", ++ttc);

        for (int ix=0;ix<=n;ix++)
        for (int iy=0;iy<=m;iy++)
        for (int jx=0;jx<=n;jx++)    
        for (int jy=0;jy<=m;jy++){
            int area = ix*jy-iy*jx;
            if (area<0) area = -area;
            if (area==a){
                found=1;
                printf("%d %d %d %d %d %d\n", 0,0,ix,iy,jx,jy);
                goto ffd;
            }
        }
        ffd:        
        if (!found) puts("IMPOSSIBLE");
    }
    
    return 0;
}
