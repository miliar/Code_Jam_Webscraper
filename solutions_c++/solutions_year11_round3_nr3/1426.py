#include<stdio.h>

int main(){
    int i,j,k,T,N,L,H,cant;
    int arr[1000];
    scanf("%d",&T);
    for(i=0;i<T;i++){
                     scanf("%d %d %d",&N,&L,&H);
                     for(j=0;j<N;j++){
                                      scanf("%d",&arr[j]);
                     }
                     
                     for(j=L;j<=H;j++){
                                       cant=0;
                                       for(k=0;k<N;k++){
                                                        if(arr[k]%j==0 || j%arr[k]==0){
                                                        }
                                                        else{
                                                             cant=1;
                                                             break;
                                                        }
                                       }
                                       if(cant==0)break;                                       
                     }
                     printf("Case #%d: ",i+1);
                     if(cant==0)printf("%d\n",j);
                     else printf("NO\n");
                     
                    
    }
}
