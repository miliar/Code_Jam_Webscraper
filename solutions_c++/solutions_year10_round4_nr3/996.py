#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("Cout.txt","w",stdout);
    int c,r,sum;
    int x[300][300];
    int xx[300][300];
    int ccnt=0;
    scanf("%d",&c);
    while (c--)
    {
          ccnt++;
          int x1,y1,x2,y2;
          memset(x,0,sizeof(x));
          memset(xx,0,sizeof(xx));
          scanf("%d",&r);
          sum=0;
          while (r--)
          {
                scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
                for (int i=x1;i<=x2;i++)
                   for (int j=y1;j<=y2;j++)
                   {
                      xx[j][i]=x[j][i]=1;
                   }
           }
           for (int i=0;i<300;i++)
                   {
                      for (int j=0;j<300;j++)
                      {
                         if (x[i][j]) sum++;
                      }
                   }
                int cnt=0;
                while (sum!=0){
                cnt++;
                for (int i=0;i<300;i++)
                   for (int j=0;j<300;j++)
                   {
                       if (x[i][j]==1)
                          if ((i==0||x[i-1][j]==0)&&(j==0||x[i][j-1]==0))
                             xx[i][j]=0;
                       if (x[i][j]==0)
                          if (i!=0&&x[i-1][j]==1&&j!=0&&x[i][j-1]==1)
                             xx[i][j]=1;
                   }
                   sum=0;
                   for (int i=0;i<300;i++)
                   {
                      for (int j=0;j<300;j++)
                      {
                         x[i][j]=xx[i][j];
                         if (x[i][j]) sum++;
                      }
                   }
                }
                printf("Case #%d: %d\n",ccnt,cnt);
    }
    return 0;
}
                
                       
