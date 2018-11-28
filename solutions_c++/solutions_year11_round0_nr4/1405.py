#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){
   int t,n,arr[1000],arr2[1000],c,i,k;
   scanf("%d",&t);
   for(k=1;k<=t;k++){
                     c=0;
       scanf("%d",&n);
       for(i=0;i<n;i++)
       {
          scanf("%d",&arr[i]);
          arr2[i]=arr[i];                
       }
       sort(arr2,arr2+n);
       for(i=0;i<n;i++)
          if(arr[i]!=arr2[i])
             c++;
                              
       printf("Case #%d: %d.000000\n",k,c); 
    
   }
    return 0;
}
