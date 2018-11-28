#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
     freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int ca=0;
    int m;
    scanf("%d",&m);
    int v[300],p[300];
    while(m--)
    {
        printf("Case #%d: ",++ca);
        int c,d;
        int tot=0;
        scanf("%d %d",&c,&d);
        double ans=0;
        for(int i=0;i<c;++i){
            scanf("%d %d",&p[i],&v[i]);
            tot+=v[i];
            ans=max(ans,0.5*(v[i]-1)*d );
        }
        for(int i=0;i<c;i++){
            tot=v[i];
            for(int j=i+1;j<c;j++){
                tot+=v[j];
                ans=max(ans,0.5*((tot-1)*d-(p[j]-p[i])));
            }
        }

        printf("%lf\n",ans);
    }
    return 0;
}
