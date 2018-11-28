#include <cstdio>
#include <cstring>
#include <cassert>
#include <utility>
#include <set>
#include <algorithm>
using namespace std;

#ifdef mahou_shoujo_madoka
    #define LLF "I64d"
    #define ASSERT(x) assert(x)
#else
    #define LLF "lld"
    #define ASSERT(x)
#endif

class Vec{
public:
    long long r,c;
    Vec():r(0),c(0){}
    Vec(int r, int c):r(r),c(c){}
    const Vec operator +(const Vec& rhs) const{
        return Vec(r+rhs.r,c+rhs.c);
    }
    const Vec operator -(const Vec& rhs) const{
        return Vec(r-rhs.r,c-rhs.c);
    }
};

int r,c;
long long a[501][501];
long long s[501][501];
Vec m[501][501];
Vec w[501][501];

int main(){
    int cs;
    scanf("%d",&cs);
    for(int t=1;t<=cs;t++){
        printf("Case #%d: ",t);
        scanf("%d%d%*d",&r,&c);
        int ans=2;
        for(int i=1;i<=r;i++) for(int j=1;j<=c;j++){
            scanf("%1"LLF,&a[i][j]);
            s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+a[i][j];
            m[i][j]=Vec(a[i][j]*i*2,a[i][j]*j*2);
            w[i][j]=w[i-1][j]+w[i][j-1]-w[i-1][j-1]+m[i][j];
            for(int k=ans+1;k<=min(i,j);k++){
                long long cnt=s[i][j]-s[i-k][j]-s[i][j-k]+s[i-k][j-k]
                             -a[i][j]-a[i-k+1][j]-a[i][j-k+1]-a[i-k+1][j-k+1];
                Vec sum=w[i][j]-w[i-k][j]-w[i][j-k]+w[i-k][j-k]
                       -m[i][j]-m[i-k+1][j]-m[i][j-k+1]-m[i-k+1][j-k+1]
                       -Vec(cnt*(2*i-k+1),cnt*(2*j-k+1));
                //printf("w[%d][%d][%d] = (%"LLF",%"LLF"), cnt = %"LLF"\n",i,j,k,sum.r,sum.c,cnt);
                if(!sum.r && !sum.c) ans=max(ans,k);
            }
        }
        if(ans==2) puts("IMPOSSIBLE"); else printf("%d\n",ans);
    }
}