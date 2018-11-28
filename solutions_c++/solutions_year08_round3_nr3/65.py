#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

FILE * in=fopen("in3.txt","r");
FILE * out=fopen("out3.txt","w");

const int MAXN=500010, MOD=1000000007;
int T;
int A[101], speed[500010];
typedef long long ll;


int main() {

    fscanf(in,"%d",&T);
    for( int test=1; test<=T; test++ ) {
        ll n, m, X, Y, Z;
        fscanf(in,"%I64d %I64d %I64d %I64d %I64d",&n,&m,&X,&Y,&Z);
        for( int i=0; i<m; i++ ) fscanf(in,"%d",&A[i]);
        for( int i=0; i<=n-1; i++ ) {
            speed[i]=A[i%m];
            A[i%m] = (X*A[i%m]+Y*(1+i))%Z;
        }

        int ans=0;
        int dp[MAXN];
        for( int i=0; i<n; i++ ) {
            dp[i]=1;
            for( int j=0; j<i; j++ )
                if( speed[i]>speed[j] ) dp[i]+=dp[j], dp[i]%=MOD;
            ans+=dp[i], ans%=MOD;
        }

        fprintf(out,"Case #%d: %d\n",test,ans);

    }

    return 0;
}
