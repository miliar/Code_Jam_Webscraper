#include<stdio.h>
#include<string.h>
long long Co[41][41];
double dp[41];
main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T,N,C,t=0,i,j;
    Co[0][0]=1;
    for(i=1;i<=40;i++){
        Co[i][0]=1;
        for(j=1;j<=i;j++)Co[i][j]=Co[i-1][j-1]+Co[i-1][j];
    }
    scanf("%d",&T);
    double r,s,q;
    while(T--){
        memset(dp,0,sizeof(dp));
        scanf("%d %d",&C,&N);
        q=Co[C][N];
        dp[C]=0;
        for(i=C-1;i>=0;i--){
            r=Co[i][N]/q;
            s=0;
            for(j=1;j<=N&&j<=C-i;j++){
                s+=(Co[C-i][j]*Co[i][N-j])/q*(dp[i+j]+1);
            }
            dp[i]=(r+s)/(1-r);
        }
        printf("Case #%d: %lf\n",++t,dp[0]);
    }
}
