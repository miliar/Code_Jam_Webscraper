#include<cstdio>
#include<iostream>
#include<string>
#include<map>
#define INF 999888
using namespace std;

int main()
{
  int tt,nn;
  scanf("%d\n",&nn);
  for(tt=1;tt<=nn;tt++)
  {
    int s,q,a[2000],dp[1005][105];
    map<string,int> m;
    scanf("%d\n",&s);
    for(int i=0;i<s;i++)
    {
      string ss;
      getline(cin,ss);
      m[ss]=i;
    }    
    scanf("%d\n",&q);
    for(int i=1;i<=q;i++)
    {
      string ss;
      getline(cin,ss);
      a[i]=m[ss];
    }
//for(int i=1;i<=q;i++) printf("%d ",a[i]); printf("\n");
    for(int i=0;i<s;i++) dp[0][i]=0;
    for(int t=1;t<=q;t++)
      for(int i=0;i<s;i++)
      {
        dp[t][i]=INF;
        if(i!=a[t])
        {
          int b=INF;
          for(int j=0;j<s;j++) b<?=dp[t-1][j]+((j!=i)?1:0);
          dp[t][i]=b;
        }
//        printf("dp[%d][%d]=%d\n",t,i,dp[t][i]);
      }
    int b=INF;
    for(int i=0;i<s;i++) b<?=dp[q][i];
    printf("Case #%d: %d\n",tt,b);
  }

  return 0;
}
