#include<iostream>
using namespace std;
#include<cstdlib>

int main(){
    int i,k,kase,T, L, H, N, flag;
    freopen("C-small2.in","r",stdin);
    freopen("C-small2.out","w",stdout);
    int num[10000];
    
    scanf("%d",&T);
    for(kase=1;kase<=T;kase++){
       scanf("%d %d %d",&N, &L, &H);
       for(i=0;i<N;i++)
          scanf("%d",&num[i]);
       //qsort(num, N, sizeof(LL), comp);
       flag=0;
       printf("Case #%d: ",kase); 
       for(i=L;i<=H;i++){
          int flag2=0;
          for(k=0;k<N;k++)
             if(num[k] %i != 0 && i%num[k] !=0){
                flag2=1;
                break;
             }
          if(flag2 == 0 ){
             flag = 1;
             printf("%d\n",i);
             break;
          }
       }
       if(flag == 0)
               printf("NO\n");
    }
    return 0;
}
             
             
                
