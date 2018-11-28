#include <iostream>
#include <cmath>

using namespace std;

int dp[105][300][2],T,a[105];

int cal(int a,int b)
{
    if (b==0)
       if (a==0) return 0;
       else return 100000;
    else if (a%b==0) 
            if (a==0) return 0;
            else return a/b-1;
         else return a/b;
}

int main(){
    freopen("Smooth.in","r",stdin);
    freopen("Smooth.out","w",stdout);
    cin>>T;
    for (int t=1;t<=T;t++)
    {
        int D,I,M,N;
        scanf("%d%d%d%d",&D,&I,&M,&N);
        memset(dp,0,sizeof(dp));
        for (int i=1;i<=N;i++)
            for (int j=0;j<=255;j++) {dp[i][j][0]=100000;dp[i][j][1]=100000;}
        for (int i=1;i<=N;i++)
            scanf("%d",&a[i]);
        //cout<<D<<" "<<I<<" "<<M<<" "<<N<<endl;
        for (int i=1;i<=N;i++)
            for (int j=0;j<=255;j++)
            {
                for (int k=0;k<=255;k++) dp[i][j][0]<?=min(dp[i-1][k][0]+D,dp[i-1][k][1]+D);
                dp[i][j][1]<?=D*(i-1)+abs(j-a[i]);
                for (int k=2;k<=i;k++) 
                    for (int l=0;l<=255;l++)
                        if (cal(abs(l-j),M)<10000) dp[i][j][1]<?=dp[k-1][l][1]+I*cal(abs(l-j),M)+abs(j-a[i])+D*(i-k);
                //cout<<i<<" "<<j<<" "<<dp[i][j]<<endl;
            }
        int minn=100000;
        for (int i=0;i<=255;i++) minn<?=min(dp[N][i][0],dp[N][i][1]);
        cout<<"Case #"<<t<<": "<<minn<<"\n";
    }
    return 0;
}
