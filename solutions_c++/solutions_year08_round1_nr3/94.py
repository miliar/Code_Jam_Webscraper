#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

const int MOD=1000;
typedef long long LL;
int n;

void mult(int ai[2][2],int bi[2][2]){
    int a[2][2],b[2][2];
    memcpy(a,ai,sizeof(a));
    memcpy(b,bi,sizeof(b));
    ai[0][0]=(a[0][0]*b[0][0]+a[0][1]*b[1][0])%MOD;
    ai[0][1]=(a[0][0]*b[0][1]+a[0][1]*b[1][1])%MOD;
    ai[1][0]=(a[1][0]*b[0][0]+a[1][1]*b[1][0])%MOD;
    ai[1][1]=(a[1][0]*b[0][1]+a[1][1]*b[1][1])%MOD;
}
void pw(int a[2][2],int n){
    int b[2][2];
    memcpy(b,a,sizeof(b));
    a[0][0]=a[1][1]=1;
    a[0][1]=a[1][0]=0;
    while(n){
        if(n&1) mult(a,b);
        mult(b,b);
        n>>=1;
    }
}
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int cas,ic;
    scanf("%d",&cas);
    for(ic=1;ic<=cas;ic++){
        scanf("%d",&n);
        int a[2][2];
        a[0][0]=6;
        a[0][1]=-4;
        a[1][0]=1;
        a[1][1]=0;
        pw(a,n-1);
        int ans=(a[0][0]*6+a[0][1]*2-1)%MOD;
        if(ans<0) ans+=MOD;
        printf("Case #%d: %03d\n",ic,ans);
    }
    return 0;
}
