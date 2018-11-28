#include <iostream>
#include <algorithm>

using namespace std;

int T;
long long dis,n;
long long di[10100],len[10100],dp[10100];
int f[10100];


int cacul()
{
    int i,j,ff;
    f[0] = di[0];
    j = 1;
    for (i = 0;i < n && i < j;i++)
    {
        while (di[j]-di[i]<=f[i] && j<n)
        {
              f[j] = (len[j] <= di[j]-di[i])?len[j]:di[j]-di[i];
              j++;
        }
    }
    ff = 0;
    for (i = 0;i < j;i++)
        if (di[i]+f[i]>=dis)
        {
            ff = 1;break;
        }
    return ff;    
}

int main()
{     
     freopen("A-small.in","r",stdin);
     freopen("x.out","w",stdout);
     scanf("%d",&T);
     int i;
     for (i = 0;i < T;i++)
     {
         scanf("%d",&n);
         int j;
         for (j = 0;j < n;j++)
             scanf("%d%d",di+j,len+j);
         scanf("%d",&dis);
         di[n] = dis;
         for (j = 0;j <= n;j++)
         {
             f[j] = 0;
             dp[j] = 0;
         }
         int ans = 0;
         ans = cacul();
         if (ans)
             printf("Case #%d: YES\n",i+1);
         else 
             printf("Case #%d: NO\n",i+1);
     }
     
     fclose(stdin);
     return 0;
}
