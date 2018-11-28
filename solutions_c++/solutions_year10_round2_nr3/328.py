#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#define MOD 100003
int dp[501][501];
int c[555][555];
void init(){
    memset(c,0,sizeof(c));
    c[0][0]=1;
    int i,j;
    for(j=1;j<=500;++j){
        c[0][j]=1;
        for(i=1;i<=j;++i){
            c[i][j]=(c[i][j-1]+c[i-1][j-1])%MOD;
        }
    }
    /*
    for(i=0;i<10;++i){
        for(j=0;j<10;++j)printf("%d ",c[i][j]);
        putchar(10);
    }
    */
}
            

int pow(long long x,int n){
    long long ans=1;
    for(;n>0;n>>=1,x=(x*x)%MOD){
        if(n&1){
            ans=(ans*x);
        }
    }
    return ans;
}
int C(int a,int b){
    return c[a][b];
}
int main(){
    
    freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
    
    init();
    memset(dp,0,sizeof(dp));
    int i,j,k;
    for(i=1;i<=500;++i){
        for(j=i+1;j<=500;++j){
            int sum=0;
            for(k=1;k<=(min(i,j)-1);++k){
                sum=(sum+(long long)dp[k][i]*C(i-k-1,j-i-1))%MOD;
            }
            dp[i][j]=sum;
            if(i==1)dp[i][j]=1;
        }
    }
    /*
    for(i=0;i<7;++i){
        for(j=0;j<7;++j)printf("%d ",dp[i][j]);
        putchar(10);
    }
    */
    int Cas,ca=0;
    scanf("%d",&Cas);
    while(Cas--){
        int n;
        scanf("%d",&n);
        int ans=0;
        for(i=1;i<=n;++i){
            ans=(ans+dp[i][n])%MOD;
        }
        printf("Case #%d: %d\n",++ca,ans);
    }
//    system("pause");
    return 0;
}
