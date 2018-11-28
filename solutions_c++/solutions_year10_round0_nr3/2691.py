#include<stdio.h>

int arr[10000000];

int main(){
 int i,test, R,k,N,j,coast,l,cos,x;
 
 scanf("%d",&test);
 for(i=1;i<=test;i++){
     scanf("%d %d %d",&R,&k,&N);
     for(j=1;j<=N;j++){
         scanf("%d",&arr[j]);
        }
        coast=0;
        l=1;
     for(j=1;j<=R;j++){
         cos=0;
         x=l;
         int z=1;
         while(cos+arr[l]<=k && z==1){
             coast+=arr[l];
             cos+=arr[l];   
             l++;
             if(l>N) l=1;
             if(x==l) z++;
            }
        }
     printf("Case #%d: %d\n",i,coast);
    }
 
 
 
 while(getchar()!=EOF);
 return 0;   
}
