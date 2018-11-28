#include <stdio.h>

int vet[101];

int main()
{
    int t, n, l, h,i,j,teste,maior,menor;
    
    scanf("%d",&t);
    for(teste=1;teste<=t;teste++){
        scanf("%d %d %d",&n,&l,&h);
        
        for(i=0;i<n;i++) scanf("%d",&vet[i]);
        
        for(i=l;i<=h;i++) {
            for(j=0;j<n;j++){
                if(vet[j]>i) maior = vet[j], menor = i;
                else         menor = vet[j], maior = i;
                
                maior = maior -(maior/menor)*menor;
                if(maior!=0) break;
            }
            if(j==n) {printf("Case #%d: %d\n",teste,i); break;}
        }
        
        if(i>h) printf("Case #%d: NO\n",teste);
    }
    return 0;
}