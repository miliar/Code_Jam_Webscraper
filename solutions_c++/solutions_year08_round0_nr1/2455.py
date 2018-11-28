# include <stdio.h>
# include <string.h>
//# include <conio.h>
using namespace std;
int n,x,y,s,k,q,i,j,me,dp[1002][1002];
char b[1010][103],p[10004][1003],c;
int main()
{
//    freopen("output.txt","w",stdout);
    scanf("%d",&n);
    for(x=1;x<=n;x++)
    {
         memset(dp,0,sizeof(dp));
         scanf("%d\n",&s);
         for(y=0;y<s;y++)
         {
              k=0;
              scanf(" %c",&c);             
              while(c!='\n')
              {
                   b[y][k]=c;
                   k++;
                   scanf("%c",&c);
              }
              b[y][k]='\0';
         }
         scanf("%d\n",&q);         
         for(y=0;y<q;y++)
         {
              k=0;
              scanf(" %c",&c);             
              while(c!='\n')
              {
                   p[y][k]=c;
                   k++;
                   scanf("%c",&c);
              }
              p[y][k]='\0';
         }             
         for(i=q-1;i>=0;i--)
         {
              for(j=0;j<s;j++)
              {
                   if(strcmp(b[j],p[i])==0)
                   {                        
                        me=-1;
                        for(y=0;y<s;y++)
                             if((me==-1||dp[i+1][y]<me)&&y!=j)
                             {
                                  me=dp[i+1][y];
                                  k=y;
                             }
                        dp[i][j]=dp[i+1][k]+1;
                   }
                   else
                   {
                        dp[i][j]=dp[i+1][j];
                   }
//                   printf("%d ",dp[i][j]);
              }
//              printf("\n");
         }
         me=-1;
         for(y=0;y<s;y++)
              if(dp[0][y]<me||me==-1)
                   me=dp[0][y];
         printf("Case #%d: %d\n",x,me);
    }
//    getch();
    return 0;
}
