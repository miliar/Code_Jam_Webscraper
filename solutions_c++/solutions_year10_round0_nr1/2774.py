#include<stdio.h>

int main(){
    int n, steker,i,arr[31], K;
    
    arr[0]=0;
    arr[1]=1;
    
    for(i=2;i<=31;i++){
        arr[i]=2*arr[i-1]+1;               
        }
        
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        scanf("%d %d",&steker,&K);
        if((K-arr[steker])%(arr[steker]+1)==0) printf("Case #%d: ON\n",i);
        else printf("Case #%d: OFF\n",i);
    }
    
    
    
 while(getchar()!=EOF);
 return 0;   
}
