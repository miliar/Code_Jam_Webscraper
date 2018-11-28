#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int num[1111],numt[1111];
bool b[1234];
int main()
{
    int i,j,k,n,m,cs,q=0;
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C.out","w",stdout);
    memset(b,true,sizeof(b));
    for (i=2;i<=1000;i++)
    {
        if (b[i])
        {
           for (j=2;i*j<=1000;j++)
           b[j*i]=false;
        }
    }
    scanf("%d",&cs);
    while (cs--)
    {
          scanf("%d",&n);
          int sum1=1,sum2=0;
          if (n==1) sum2=1;
          memset(num,0,sizeof(num));
          for (i=2;i<=n;i++)
          {
              memset(numt,0,sizeof(numt));
              k=i;
              for (j=2;j<=i;j++)
              {
                  while (k%j==0)
                  {
                      numt[j]++;
                      k/=j;
                  }
              }
              bool f=false;
              for (j=1;j<=i;j++)
              {
                  if (num[j]<numt[j])
                  {
                     num[j]=numt[j];
                     f=true;
                  }
              }
              if (f)
              sum1++;
          }
          for (j=2;j<=n;j++)
          if (b[j])
          sum2++;
          printf("Case #%d: %d\n",++q,sum1-sum2);
    }
}
