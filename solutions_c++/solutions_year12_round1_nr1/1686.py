#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    int t,ch=0;
    scanf("%d",&t);
    while(t--)
    {
              ch++;
              int n,m;
              scanf("%d%d",&n,&m);
              double p[n],pro=1,s=0,num,min,a,b;
              int i;
              for(i=0;i<n;i++)
              {
                              scanf("%lf",&num);
                              p[i]=num;
                              pro*=num;
              }
              a=pro*(m-n+1)+(1-pro)*(2*m-n+2);
              b=(m+2);
              min=(a<b)?a:b;
              for(i=1;i<=n;i++)
              {
              pro=pro/p[n-i];
              a=pro*(m-(n-i)+i+1)+(1-pro)*(m-(n-i)+i+1+m+1);
              if(a<min)
              min=a;
              }
              printf("Case #%d: %0.6lf\n",ch,min);
              }
              return 0;
              }
              
              
              
