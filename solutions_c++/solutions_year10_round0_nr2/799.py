#include<iostream>
using namespace std;
#include<stdlib.h>
int fuct(int a,int b)
{
    int t;
    if(b>a)
    {
       t=a;a=b;b=t;
    }
    if(b==0){ return a;}
    else
    {
    while(a%b)
    {
       t=a%b;
       a=b;
       b=t;
    }
    return b;
    }
}
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T,i,a,m,k,j;
    int b[3],sum;
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
      scanf("%d",&a);
      for(j=0;j<a;j++)
      {
          scanf("%d",&b[j]);
      }
      if(a==3)
      {
      sort(b,b+3);
      m=b[1]-b[0];
      k=b[2]-b[1];
      sum=fuct(m,k);
      }
      else 
      {
           sort(b,b+2);
      sum=b[1]-b[0];
      }
      for(j=1;;j++)
      {
          if(j*sum>=b[0])
          break;
      }
      printf("Case #%d: %d\n",i,sum*j-b[0]);
    }
    return 0;
}
