#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;
int a1,a2,b1,b2;
int sg[100];
bool dp[100];
int main()
{
    int i,j,k,cas,tcas=0;
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&cas);
    while (cas--)
    {
          int sum=0;
          
          scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
          for (i=a1;i<=a2;i++)
          {
              for (j=b1;j<=b2;j++)
              {
                  int m=0;
                  int smj=j,smi=i;
                  if (smj>smi) swap(smj,smi);
                  int now=0;
                  while (smj)
                  {
                     sg[++now]=((smi-1)/smj);
                     int tmp=smj;
                     smj=smi%smj;
                     smi=tmp;
                  }
                  if(now==0) continue;
                  if (sg[now]==0) dp[now]=false;
                  else dp[now]=true;
                  for (int qq=now-1;qq;qq--)
                  if (!dp[qq+1])
                  dp[qq]=true;
                  else if (sg[qq]>1)
                  dp[qq]=true;
                  else dp[qq]=false;
                  if (dp[1]) sum++;
              }
          }    
          printf("Case #%d: %d\n",++tcas,sum);
    }
}
