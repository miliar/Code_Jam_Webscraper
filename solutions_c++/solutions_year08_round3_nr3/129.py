#include <iostream>
#include <cmath>
using namespace std;

#define mset(a,x) memset(a,x,sizeof(a))
typedef long long i64;
const int INF=INT_MAX/2;

i64 n,m,X,Y,Z;
i64 A[105];
i64 B[500005];
i64 dp[500005];

int main()
{
    int T,kcase(0);
    scanf("%d",&T);
    while(T--){
        scanf("%I64d%I64d%I64d%I64d%I64d",&n,&m,&X,&Y,&Z);
        for(int i=0;i<m;i++){
            scanf("%I64d",&A[i]);
        }
        /*
for i = 0 to n-1
  print A[i mod m]
  A[i mod m] = (X * A[i mod m] + Y * (i + 1)) mod Z
        */
        for(int i=0;i<n;i++){
            B[i]=A[i%m];
            A[i%m]=(X*A[i%m]+Y*(i+1))%Z;
            //printf("%d ",B[i]);
        }
        //printf("\n");
        i64 res=0;
        for(int i=0;i<n;i++){
            dp[i]=1;
            for(int j=0;j<i;j++){
                if(B[j]<B[i]){
                    dp[i]=(dp[i]+dp[j])%1000000007ll;
                }
            }
            //printf("%d ",dp[i]);
            res=(res+dp[i])%1000000007ll;
        }
        //printf("\n");
        printf("Case #%d: %I64d\n",++kcase,res);
    }
}
