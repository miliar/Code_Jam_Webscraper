#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;
int a[1010],Max;
int main(){
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attempt2.txt","w",stdout);
    int t,k,numa,numb,suma,sumb,c,n,i,j;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
     scanf("%d",&n);
     for(i=0;i<n;i++)
      scanf("%d",&a[i]);
     c=0,Max=0;
     for(i=1;i<(1<<n)-1;i++)
     {
      numa=numb=suma=sumb=0;
      for(j=0;j<n;j++)
       if((i&(1<<j))==0)
        numa = numa xor a[j] , suma+=a[j];
       else
        numb = numb xor a[j] , sumb+=a[j];

      if(numa==numb){ c=1; Max=max(Max,max(suma,sumb)); }
     }
     printf("Case #%d: ",k);
     if(c) printf("%d\n",Max);
     else printf("NO\n");
    }
}

