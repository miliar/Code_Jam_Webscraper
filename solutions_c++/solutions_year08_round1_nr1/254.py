#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

typedef long long ll;
const int maxn=1024;
int a[maxn],b[maxn];
int n;

void input()
{
    int i;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++){
        scanf("%d",&b[i]);
    }
}

ll solve()
{
    int i,t1,t2;
    ll ans=0;
    sort(a,a+n);
    sort(b,b+n);
    for(i=0;i<n;i++) if(a[i]>0) break;
    t1=i;
    for(i=0;i<n;i++) if(b[i]>0) break;
    t2=i;
    for(i=0;i<n;i++){
        ans+=a[i]*b[n-1-i];
    }
    return ans;
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a.out","w",stdout);
    int i,cas;
    scanf("%d",&cas);
    for(i=1;i<=cas;i++){
        input();
        printf("Case #%d: %lld\n",i,solve());
    }
    return 0;
}
