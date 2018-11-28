#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

struct node{double b,e,s;};

node d[1000000];
int T,n;
double t,x,total,s,r;

bool cmp(node a,node b){return a.s<b.s?1:0;}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    for (int Case=1;Case<=T;Case++){
        total=0;
        scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
        for (int i=1;i<=n;i++) {scanf("%lf%lf%lf",&d[i].b,&d[i].e,&d[i].s);total+=d[i].e-d[i].b;}
        sort(d+1,d+n+1,cmp);
        double rest=x-total;
        double ans=0;
        if (rest*1.0/r<t){t-=rest*1.0/r;ans+=rest*1.0/r;}else{ans+=t;rest-=t*r;t=0;ans+=rest*1.0/s;}
        for (int i=1;i<=n;i++){
            double len=d[i].e-d[i].b;
            if (len*1.0/(r+d[i].s)<t){
               t-=len*1.0/(r+d[i].s);
               ans+=len*1.0/(r+d[i].s);
            }else{
              ans+=t;len-=t*(r+d[i].s);t=0;ans+=len*1.0/(s+d[i].s);
            }
        }
        printf("Case #%d: %lf\n",Case,ans);
    }
}
