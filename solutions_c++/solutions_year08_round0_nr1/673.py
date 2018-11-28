#include<iostream>
#include<string> 
using namespace std;
int main()
{
    int dp[1005][105]; 
    int ss[1005]; 
    char name[105][105],st[105];
    int casen,s,q;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout); 
    scanf("%d",&casen);
    for (int casei=1;casei<=casen;casei++)
    {
        scanf("%d\n",&s);
        for (int i=1;i<=s;i++)
          gets(name[i]);
        scanf("%d\n",&q);
        for (int i=1;i<=q;i++)
        {
            gets(st);
            for (int j=1;j<=s;j++)
              if (strcmp(st,name[j])==0)ss[i]=j;
        }
//        for (int i=1;i<=s;i++)
  //        printf("%d ",ss[i]); 
        memset(dp,0,sizeof(dp));
        for (int i=1;i<=s;i++)
          dp[0][i]=1; 
        for (int i=1;i<=q;i++)
          for (int j=1;j<=s;j++)
            if (dp[i-1][j]!=0) 
              for (int k=1;k<=s;k++)
                if (k!=ss[i])
                {
                             if (k==j&&(dp[i-1][j]<dp[i][k]||dp[i][k]==0))dp[i][k]=dp[i-1][j];
                             if (k!=j&&(dp[i-1][j]+1<dp[i][k]||dp[i][k]==0))dp[i][k]=dp[i-1][j]+1;
                }
        int min=10000;
        for (int i=1;i<=s;i++)
          if (dp[q][i]<min&&dp[q][i]!=0)min=dp[q][i];
        printf("Case #%d: %d\n",casei,min-1);
    }
    return 0;
}
