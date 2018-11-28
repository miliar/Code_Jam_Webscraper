#include<stdio.h>

int main() {
    long t,n,sum,xr,min,c;
  
  scanf("%ld",&t);
  for(int i=0;i<t;i++) {
    scanf("%ld",&n);
    sum=0;
    xr=0;
    min = 2000000;
    for(int j=0;j<n;j++) {
      scanf("%ld",&c);
      xr ^=c;
      if(c<min) min = c;
      sum+=c;
    }
    if(xr!=0)
    printf("Case #%ld: NO\n",i+1);
    else    
    printf("Case #%ld: %ld\n",i+1,sum-min);
    
        
  }    
}
