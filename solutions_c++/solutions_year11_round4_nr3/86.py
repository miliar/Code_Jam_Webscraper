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
int casN;
LL n,ans;
#define MAX 1000010
char mul[MAX],pri[MAX];
int main(){
    scanf("%d",&casN);
    memset(pri,1,sizeof(pri));
    memset(mul,1,sizeof(mul));
    mul[0]=mul[1]=0;
    pri[0]=pri[1]=0;
    for(int i=2;i<MAX;i++){
        if(!pri[i])continue;
        for(int j=i+i;j<MAX;j+=i){
            pri[j]=0;
            mul[j]=-mul[j];
        }
        LL i2=(LL)i*i;
        for(LL j=i2;j<MAX;j+=i2){
            mul[j]=0;
        }
    }
    for(int III=0;III<casN;III++){
        scanf("%I64d",&n);
        ans=0;
        for(LL i=1;i*i<=n;i++){
            if(pri[i]){
                LL ii=i;
                while(ii<=n){
                    ii*=i;
                    ans++;
                }
                ans--;
            }
        }
        printf("Case #%d: %I64d\n",III+1,ans+(n>1?1:0));
    }
    scanf(" ");
    return 0;
}

