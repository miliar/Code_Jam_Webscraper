#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<map>
#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define CLR(x) memset((x), 0, sizeof(x))
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FEACH(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define F first
#define S second
//using namespace std;
typedef long long LL;
inline LL Min(LL a,LL b){
    return a<b?a:b;
}
inline LL Max(LL a,LL b){
    return a>b?a:b;
}
inline LL Abs(LL a){
    return a>0?a:-a;
}
bool cmp(LL a,LL b){
    return a<b;
}
int casN,n,m,ans;
LL sum[510][510],xsu[510][510],ysu[510][510];
char inp[510][510];
inline LL getV(LL cal[][510],int is,int js,int il,int jl,int opt){
    LL ret=cal[il][jl]-cal[is][jl]-cal[il][js]+cal[is][js];
    if(opt==1)ret-=inp[is][js]+inp[is][jl-1]+inp[il-1][js]+inp[il-1][jl-1];
    else if(opt==2)ret-=(inp[is][js]+inp[is][jl-1])*(is+1)+(inp[il-1][js]+inp[il-1][jl-1])*(il);
    else if(opt==3)ret-=(inp[is][js]+inp[il-1][js])*(js+1)+(inp[is][jl-1]+inp[il-1][jl-1])*(jl);
    return ret;
}
int main(){
    scanf("%d",&casN);
    for(int III=0;III<casN;III++){
        scanf("%d%d%*d",&n,&m);
        for(int i=0;i<n;i++){
            scanf("%s",inp[i]);
        }
        for(int i=1;i<=n;i++){
            for(int j=1;j<=m;j++){
                inp[i-1][j-1]-='0';
                sum[i][j]=sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1]+inp[i-1][j-1];
                
                xsu[i][j]=xsu[i-1][j]+xsu[i][j-1]-xsu[i-1][j-1]+inp[i-1][j-1]*i;
                ysu[i][j]=ysu[i-1][j]+ysu[i][j-1]-ysu[i-1][j-1]+inp[i-1][j-1]*j;
            }
        }
        ans=0;
        for(int k=3;k<=n;k++){
            for(int i=0;i<=n-k;i++){
                for(int j=0;j<=m-k;j++){
                    LL s=getV(sum,i,j,i+k,j+k,1),x=getV(xsu,i,j,i+k,j+k,2),y=getV(ysu,i,j,i+k,j+k,3);
                    if(x*2==s*(2*i+k+1)&&y*2==s*(2*j+k+1)){ans=k;}
                }
            }
        }
        if(!ans)printf("Case #%d: IMPOSSIBLE\n",III+1);
        else printf("Case #%d: %d\n",III+1,ans);
    }
    scanf(" ");
    return 0;
}

