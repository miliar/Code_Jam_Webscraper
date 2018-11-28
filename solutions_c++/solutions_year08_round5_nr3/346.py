#include<iostream>
#include<string> 
using namespace std;
int dp[20][3000]; 
int bit[20];
char st[100][100];
int casen,m,n;
int kk; 
void work(int i,int j,int k,int ss)
{
     if (j>=m)
     {
              if (dp[i-1][kk]+ss>dp[i][k])dp[i][k]=dp[i-1][kk]+ss;
     }
     else
     {
         if (st[j][i-1]=='x'||((kk & bit[j])>0)||((kk & bit[j+1])>0)||(j!=0&&(kk & bit[j-1])>0))work(i,j+1,k,ss);
         else
         {
             work(i,j+1,k,ss);
             work(i,j+1,k+bit[j],ss+1);
         }
     }
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout); 
    scanf("%d",&casen);
    for (int casei=1;casei<=casen;casei++)
    {
        scanf("%d%d",&m,&n);
        for (int i=0;i<m;i++)
          scanf("%s",st[i]);
        bit[0]=1; 
        for (int i=1;i<=m;i++)
          bit[i]=bit[i-1]*2;
        memset(dp,0,sizeof(dp)); 
        dp[0][0]=1;
        for (int i=1;i<=n;i++)
          for (int j=0;j<bit[m];j++)
            if (dp[i-1][j]>0)
            {
                             kk=j; 
              work(i,0,0,0);
              }
        int max=0;
//        for (int i=0;i<=n;i++)
  //      {
    //        for (int j=0;j<bit[m];j++)
      //        printf("%d ",dp[i][j]);
        //    printf("\n");
          //  } 
        for (int i=0;i<bit[m];i++)
          if (dp[n][i]>max)max=dp[n][i]; 
        printf("Case #%d: %d\n",casei,max-1);
    }
    return 0;
}
