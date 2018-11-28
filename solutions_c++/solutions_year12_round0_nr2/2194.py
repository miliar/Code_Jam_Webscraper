#include<stdio.h>

int score[110];
int dp[110][110];

int max(int a,int b){
    if(a>b) return a;
    return b;
}

int abs(int a){
    if(a<0) a*=-1;
    return a;
}

int main(){
    int T,N,S,p;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        scanf("%d%d%d",&N,&S,&p);
        for(int j=0;j<N;j++)
            scanf("%d",&score[j]);
        for(int j=0;j<=S;j++) dp[N][j]=0;
        for(int j=N-1;j>=0;j--){
            bool normal=false,surprise=false;
            for(int k=p;k<=10;k++){
                int aux=score[j]-k;
                if(aux>=0){
                    for(int l=0;l<=aux&&l<=10;l++){
                        int x=aux-l; if(x>10) continue;
                        if(abs(l-k)<2&&abs(l-x)<2&&abs(k-x<2)) normal=true;
                        if(abs(l-k)<3&&abs(l-x)<3&&abs(k-x<3)) surprise=true;
                    }
                }
            }
            for(int k=0;k<=S;k++){
                dp[j][k]=dp[j+1][k];
                if(normal) dp[j][k]=max(dp[j+1][k]+1,dp[j][k]);
                if(surprise&&k<S) dp[j][k]=max(dp[j+1][k+1]+1,dp[j][k]);
            }
        }
        printf("Case #%d: %d\n",i,dp[0][0]);
    }
    return 0;
}
