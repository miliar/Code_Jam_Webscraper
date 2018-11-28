#include<stdio.h>
#define SIZE 110
#define MAX 1000000000
using namespace std;
int t,D,I,M,N,a[SIZE],dp[SIZE][256];
int Abs(int x){return x<0?-x:x;}
int Min(int x,int y){
    return x<y?x:y;
}
main(){
    freopen("B-small-attempt3.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int i,j,k,T,an  ;
    scanf("%d",&T);
    while(T--){
        t++;
        scanf("%d %d %d %d",&D,&I,&M,&N);
        for(i=1;i<=N;i++)scanf("%d",&a[i]);
        for(i=0;i<256;i++){
            dp[1][i]=Abs(a[1]-i);
            if(M&&a[1]!=i)dp[1][i]=Min(dp[1][i],((Abs(a[1]-i)-1)/M+1)*I);
            dp[1][i]=Min(dp[1][i],D+I);
        }
        for(i=2;i<=N;i++){
            for(j=0;j<256;j++){
                dp[i][j]=MAX;
                dp[i][j]=Min(dp[i][j],dp[i-1][j]+D);
                for(k=0;k<256;k++){
                    if(j!=k){
                        if(M)dp[i][j]=Min(dp[i][j],dp[i-1][k]+(Abs(j-k)-1)/M*I+Min(Abs(a[i]-j),D+I));
                    }
                    else dp[i][j]=Min(dp[i][j],dp[i-1][k]+Abs(a[i]-j));
                }
            }
        }
        an=MAX;
        for(i=0;i<256;i++)an=Min(an,dp[N][i]);
        printf("Case #%d: %d\n",t,an);
    }
}
