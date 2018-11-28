#include <stdio.h>
#include <string.h>
#include <algorithm>
#define inf 1000000000000LL
using namespace std;

typedef long long ll;

ll num[10000010];
int t,tt,m,p;
ll n;
ll prime[1000010];
int isgo[1000010];

void getprime()
{
    p  = 0;
    for(int i=2;i<=1000000;i++){
        if(isgo[i] == 0){
            prime[++p] = i;
            for(int j=i+i;j<=1000000;j+=i)
                isgo[j] = 1;
        }
    }
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    getprime();
    m = 1;
    num[1] = 1;
    for(ll i = 1; i <= p; i ++){
        ll base = prime[i];
        while(base <= inf / prime[i]){
            num[++m] = base * prime[i];
            base *= prime[i];
        }
    }
    sort(num + 1, num + 1 + m);
    scanf("%d",&t);
    while(t --){
        scanf("%I64d",&n);
        int ans = 0;
        for(int i=1;i<=m;i++){
            if(num[i] <= n)
                ans = i;
            else
                break;
        }
        if(n == 1){
            printf("Case #%d: 0\n", ++tt);
            continue;
        }
        printf("Case #%d: %d\n",++tt,ans);
    }
    return 0;
}
