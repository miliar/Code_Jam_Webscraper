#include <iostream>
using namespace std;

#define ll long long
#define MaxN 50

ll n,k,b,t;

struct chick {
  ll v,p;
} a[MaxN];
bool mark[MaxN];
int test;

int main()
{
    
    freopen("google.in","r",stdin);
    freopen("google2.out","w",stdout);
    
    scanf("%d",&test);
    for (int T = 0; T < test; T++) {
        scanf("%lld%lld%lld%lld",&n,&k,&b,&t);
        for (int i = 0; i < n; i++) {
            scanf("%lld",&a[n-i-1].p);
            a[n-i-1].p = b - a[n-i-1].p;
        }
        for (int i = 0; i < n; i++)
            scanf("%lld",&a[n-i-1].v);
            
        memset(mark, 0, sizeof(mark));
        int pre = 0;
        int ret = 0;
        for (int i = 0; i < n; i++) {
            if ( pre == k ) break;
            if ( a[i].v*t < a[i].p ) continue;
            
            mark[i] = true;
            pre++;
            for (int j = i-1; j >= 0; j--) {
                if ( !mark[j] ) ret++; 
            }
        }
        
        printf("Case #%d: ",T+1);
        if ( pre < k ) printf("IMPOSSIBLE\n");
        else           printf("%d\n",ret);
            
    }
    
    fclose(stdin);
    fclose(stdout);
    
    return 0;
    
}
