#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int T,n,a,b,p,D;
double ans;
int start[10000001];

bool can(double mid)
{
     double now=start[1]-mid;
     for (int i=2;i<=p;i++){
         if (start[i]+mid<now+D) return 0;else 
         if (start[i]-mid<now+D) now+=D;else
         now=start[i]-mid;
     }
     return 1;
}

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&T);
    for (int Case=1;Case<=T;Case++){
        scanf("%d%d",&n,&D);
        p=0;
        for (int i=1;i<=n;i++) {scanf("%d%d",&a,&b);for (int j=1;j<=b;j++) start[++p]=a;}
        sort(start+1,start+p+1);
        double st=0,ed=10000000000000LL;
        while (st+0.001<ed){
              double mid=(st+ed)/2;
              if (can(mid)) ed=mid;else st=mid+0.001;
        }
        if (can(st)) ans=st;else ans=ed; 
        printf("Case #%d: %.2lf0000\n",Case,ans);
    }
}
