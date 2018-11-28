#include<cstdio>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
#include<cmath>
#include<iostream>
using namespace std;

int a[101];
int dp[101][257];

int main()
{
    int t,dd,ii,mm,nn,i,j,k,temp,T=1;
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d%d",&dd,&ii,&mm,&nn);
        for(i=0;i<nn;i++) scanf("%d",&a[i]);
        
        for(i=0;i<256;i++) dp[0][i]=abs(i-a[0]);
        dp[0][256]=dd;
        
        for(i=1;i<nn;i++)
        {
            for(j=0;j<256;j++)
            {
                dp[i][j]=dp[i-1][j]+dd+abs(a[i]-j);
                //if(i==1&&j==4) printf("%d\n",dp[i][j]);
                for(k=0;k<256;k++)
                {
                    if(mm==0) 
                    {
                        if(j==k) dp[i][j]=min(dp[i][j],dp[i-1][k]+abs(a[i]-j));
                        continue;
                    }
                    if(j>k)
                    {
                        temp=(j-k)/mm;
                        if((j-k)%mm==0) temp--;
                        temp*=ii;
                        
                        
                        dp[i][j]=min(dp[i][j],dp[i-1][k]+temp+abs(a[i]-j));
                        //if(i==2&&j==4) printf("%d %d %d\n",k,dp[i-1][k],dp[i][j]);
                    }
                    else if(j==k) dp[i][j]=min(dp[i][j],dp[i-1][k]+abs(a[i]-j));
                    else
                    {
                        temp=(k-j)/mm;
                        if((k-j)%mm==0) temp--;
                        temp*=ii;
                        
                        
                        dp[i][j]=min(dp[i][j],dp[i-1][k]+temp+abs(a[i]-j));
                        //if(i==2&&j==4) printf("%d %d\n",k,dp[i-1][k],dp[i][j]);
                    }
                }
                dp[i][j]=min(dp[i][j],dp[i-1][256]+abs(j-a[i]));
                //if(i==2&&j==4) printf("%d %d\n",256,dp[i-1][256],dp[i][j]);
                ////if(i==1) printf("%d %d\n",j,dp[i][j]);
            }
            
            dp[i][256]=dp[i-1][256]+dd;
            //printf("256 %d\n",dp[i][256]);
        }
        
        int ans=0x7fffffff;
        
        for(i=0;i<257;i++) 
        {
            ans=min(ans,dp[nn-1][i]);
        }
        
        printf("Case #%d: %d\n",T++,ans);
    }
    return 0;
    
}





