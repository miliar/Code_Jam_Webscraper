#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

typedef long long ll;

ll n,pd,pg;
int t, tt = 0;

ll gcd(ll a, ll b){
    if(b == 0)  return a;
    return gcd(b, a % b);
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    while( t -- ){
        scanf("%I64d %I64d %I64d",&n,&pd,&pg);
        ll a,b,c,d;
        if(pg == 0 && pd > 0){
            printf("Case #%d: Broken\n",++tt);
            continue;
        }
        if(pg == 100 && pd < 100){
            printf("Case #%d: Broken\n",++tt);
            continue;
        }
        ll ttemp = gcd(100, pd);
        a = 100 / ttemp, b = pd / ttemp;

        if(n < a){
            printf("Case #%d: Broken\n",++tt);
        }else{
            printf("Case #%d: Possible\n",++tt);
        }
    }
    return 0;
}
