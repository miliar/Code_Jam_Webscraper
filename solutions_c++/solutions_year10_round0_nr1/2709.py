#include <stdio.h>

int main () 
{
    int nyala[35];
    int t,n,k,c,de;
    nyala[0] = 0;
    nyala[1] = 1;
    for(int i=2;i<31;i++) {
        nyala[i] = nyala[i-1]*2 + 1;
    }
    c=1;
    scanf("%d",&t);
    while (t>0) {
        scanf("%d %d",&n,&k);
        de = nyala[n];
        k = k-de;
        if(k%(de+1) == 0) {
            printf("Case #%d: ON\n",c);
        } else {
            printf("Case #%d: OFF\n",c);
        }     
        
        c++;
        t--;
    }
    
    while(getchar()!=EOF);
    return 0;
}
