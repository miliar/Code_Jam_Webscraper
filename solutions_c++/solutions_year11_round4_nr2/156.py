#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
#define SIZE 512
char Map[SIZE][SIZE];
int dp[SIZE][SIZE],dp1[SIZE][SIZE],dp2[SIZE][SIZE],dp3[SIZE][SIZE];
int Sum(int n,int m,int x,int y){
    return dp1[x][y]-dp1[x-n][y]-dp1[x][y-m]+dp1[x-n][y-m];
}
int Sum(int n,int x,int y){
    return dp1[x][y]-dp1[x-n][y]-dp1[x][y-n]+dp1[x-n][y-n];
}
bool Go(int n,int R,int C){
    int i,j;
    for(i=n;i<=R;i++)
        for(j=n;j<=C;j++){
            if((dp2[i][j]-dp2[i-n][j]-dp2[i][j-n]+dp2[i-n][j-n] - n*Sum(n,j-n,i,j-n) - dp[i][j] - dp[i-n+1][j] - dp[i][j-n+1]*n -dp[i-n+1][j-n+1]*n)*2 
                != (Sum(n,i,j) - dp[i][j] - dp[i-n+1][j] - dp[i][j-n+1] - dp[i-n+1][j-n+1])*(n+1))
                continue;
            if((dp3[i][j]-dp3[i-n][j]-dp3[i][j-n]+dp3[i-n][j-n] - n*Sum(i-n,n,i-n,j) - dp[i][j] - dp[i][j-n+1] - dp[i-n+1][j]*n -dp[i-n+1][j-n+1]*n)*2
                != (Sum(n,i,j) - dp[i][j] - dp[i-n+1][j] - dp[i][j-n+1] - dp[i-n+1][j-n+1])*(n+1))
                continue;
            return 1;
        }
    return 0;
}
;
main(){
    int T,t=0,R,C,i,j;
    scanf("%d",&T);
    while(T--){
        memset(dp1,0,sizeof(dp1));
        memset(dp2,0,sizeof(dp2));
        memset(dp3,0,sizeof(dp3));
        t++;
        scanf("%d%d%*d",&R,&C);
        for(i=1;i<=R;i++)scanf("%s",Map[i]+1);
        printf("Case #%d: ",t);

        for(i=1;i<=R;i++)
            for(j=1;j<=C;j++)
                Map[i][j]-='0';

        for(i=1;i<=R;i++)
            for(j=1;j<=C;j++)dp[i][j]=Map[i][j];

        for(i=1;i<=R;i++)
            for(j=1;j<=C;j++)dp1[i][j]=dp[i][j]+dp1[i][j-1];
        for(i=1;i<=R;i++)
            for(j=1;j<=C;j++)dp1[i][j]+=dp1[i-1][j];

        for(i=1;i<=R;i++)
            for(j=1;j<=C;j++)dp2[i][j]=dp[i][j]+dp2[i][j-1];
        for(i=1;i<=R;i++)
            for(j=1;j<=C;j++)dp2[i][j]+=dp2[i][j-1];
        for(i=1;i<=R;i++)
            for(j=1;j<=C;j++)dp2[i][j]+=dp2[i-1][j];

        for(i=1;i<=C;i++)
            for(j=1;j<=R;j++)dp3[j][i]=dp[j][i]+dp3[j-1][i];
        for(i=1;i<=C;i++)
            for(j=1;j<=R;j++)dp3[j][i]+=dp3[j-1][i];
        for(i=1;i<=C;i++)
            for(j=1;j<=R;j++)dp3[j][i]+=dp3[j][i-1];
        for(i=min(R,C);i>2;i--)
            if(Go(i,R,C))break;
        if(i<=2)puts("IMPOSSIBLE");
        else printf("%d\n",i);
    }
}
