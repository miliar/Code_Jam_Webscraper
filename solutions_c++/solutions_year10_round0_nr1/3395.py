#include<stdio.h>
int k,n,t;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for (int i=0;i<t;i++){
        scanf("%d%d",&n,&k);
        if ((k%(1<<(n)))==((1<<n)-1)) 
          printf("Case #%d: ON\n",i+1);
          else 
          printf("Case #%d: OFF\n",i+1);
        }
    return 0;
}
          
          
