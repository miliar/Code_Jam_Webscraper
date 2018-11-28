#include <stdio.h>
#include <string.h>

int t,d,I,m,n;
int dp[100][256],a[100];
int mark[256];
int abs(int x)
{
    if(x>0) return x;
    return -x;
}
void check(int o)
{
     int que[256];
     int h,t;
     h=t=0;
     memset(mark,0,sizeof(mark));
     for(int i=0;i<256;i++)
       for(int j=-m;j<=m;j++)
       if(i+j>=0&&i+j<256)
       if(dp[o][i]+I<dp[o][i+j])
       {
                                dp[o][i+j]=dp[o][i]+I;
                                if(mark[i+j]==0)
                                {
                                                que[t]=i+j;
                                                t=(t+1)%256 ;
                                                mark[i+j]=1;
                                }
       }
       while(h!=t)
       {
                   for(int j=-m;j<=m;j++)
                         if(que[h]+j>=0&&que[h]+j<256)
                         if(dp[o][que[h]]+I<dp[o][que[h]+j])
                          {
                                dp[o][que[h]+j]=dp[o][que[h]]+I;
                                if(mark[que[h]+j]==0)
                                {
                                                que[t]=que[h]+j;
                                                mark[que[h]+j]=1;
                                                t=(t+1)%256;
                                }
                          }
                    mark[que[h]]=0;
                    h=(h+1)%256;
       }
     //  printf("y\n");
} 
                          
                                
                          
     
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("b.out","w",stdout); 
    scanf("%d",&t);
    for(int ca = 1; ca <= t; ca++)
    {
            scanf("%d%d%d%d",&d,&I,&m,&n);
            for(int i=0;i<n;i++)
            scanf("%d",&a[i]);
            memset(dp,-1,sizeof(dp));
            for(int i=0;i<256;i++)
            dp[0][i]=abs(i-a[0]);
            check(0); 
            for(int i=1;i<n;i++)
                {
                    for(int j=0;j<256;j++)
                    {
                        for(int k=-m;k<=m;k++)
                        if(j+k>=0&&j+k<256)
                        {
                                           if(dp[i][j]==-1||dp[i][j]>dp[i-1][j+k]+abs(j-a[i]))
                                           dp[i][j]=dp[i-1][j+k]+ abs(j-a[i]);
                        }
                        if(dp[i][j]>dp[i-1][j]+d)
                        dp[i][j]=dp[i-1][j]+d;
                     }
                     check(i);
                    // printf("y\n");
                }
               int ans=-1;
               for(int i=0;i<256;i++)
              if(ans==-1||ans>dp[n-1][i])
                ans=dp[n-1][i];
               printf("Case #%d: %d\n",ca,ans);
              
    }
    return 0;
} 
                        
                                           
                 
            
