#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
struct NODE
{
    double x,y,r;
}vv[100];
int main()
{
    freopen("c:\\D-small-attempt0.in","r",stdin);
    freopen("c:\\d.out","w",stdout);
    int test;
    scanf("%d",&test);
    for(int p=1;p<=test;p++){
        int n;
		scanf("%d",&n);
        for(int i=1;i<=n;i++){
            scanf("%lf%lf%lf",&vv[i].x,&vv[i].y,&vv[i].r);
        }
        if(n==1){
            printf("Case #%d: %lf\n",p,vv[1].r);
        }
        else if(n==2)
        {
            double tt=max(vv[1].r,vv[2].r);
            printf("Case #%d: %lf\n",p,tt);
        }
        else{
            double ret=1e20;
            for(int i=1;i<=n;i++){
                for(int j=i+1;j<=n;j++){

                    double tt=vv[i].r+vv[j].r+sqrt((vv[i].x-vv[j].x)*(vv[i].x-vv[j].x)+(vv[i].y-vv[j].y)*(vv[i].y-vv[j].y));
                    ret=min(tt/2,ret);
                }
            }
            double maxr=-1;
            for(int i=1;i<=n;i++){
                 maxr=max(vv[i].r,maxr);
            }
            maxr=max(maxr,ret);
            printf("Case #%d: %lf\n",p,maxr);
        }
    }
}
