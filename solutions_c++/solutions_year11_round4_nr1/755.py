#include <cstdio>
#include <algorithm>
using namespace std;
struct P
{
    int s,v;
}k[1020];
int s,r,x,n;
double t;
int cmp(P a,P b) { return a.v<b.v;}
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T,ca=0;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
        int sum=0;
        double ans=0;
        for(int i=0;i<n;i++){
            int a,b,c;
            scanf("%d%d%d",&a,&b,&c);
            sum+=b-a;
            k[i].s=b-a;
            k[i].v=c+s;
            ans+=(double)k[i].s/k[i].v;
        }
        k[n].s=x-sum;
        k[n].v=s;
        ans+=(double)k[n].s/k[n].v;
        n++;
        sort(k,k+n,cmp);

//        for(int i=0;i<n;i++)
//            printf("%d %d\n",k[i].s,k[i].v);

        for(int i=0;i<n;i++){
            double p=(double) k[i].s/(k[i].v+r-s);
            if(p>=t) {
                ans-=(double)(r-s)*t/k[i].v;
                break;
            }
            else {
                ans-=(double)(r-s)*p/k[i].v;
                t-=p;
            }
        }
        printf("Case #%d: %.9f\n",++ca,ans);
    }
}


