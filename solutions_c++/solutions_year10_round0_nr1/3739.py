#include<stdio.h>

int main(){
    int nt;
    int n,k;
      
    scanf("%d",&nt);
    for(int t=1;t<=nt;t++){
        scanf("%d %d",&n,&k);
        
        k%=(1<<n);
        if(k==(1<<(n))-1) printf("Case #%d: ON\n",t);
        else printf("Case #%d: OFF\n",t);
    }
    return 0;   
}
