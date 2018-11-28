#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

struct seg{
    int b,e,w;
    bool flag;
    double save;
};
int n,x;
double T,s,r;
seg walk[3000];
int nseg;
double ans;
bool cmp(const seg &x,const seg &y)
{
    return x.b<y.b;
}
bool cmp2(const seg &x,const seg &y)
{
    int v1=x.w;
    if(!x.flag) v1+=s;
    int v2=y.w;
    if(!y.flag) v2+=s;
    return v1<v2;
}
void build_all()
{
            nseg=n;
        int last=0;
        for(int i=0;i<n;i++)
        {            
            if(walk[i].b>last){
                walk[nseg].b=last;
                walk[nseg].e=walk[i].b;
                walk[nseg].w=s;
                walk[nseg].flag=true;
                walk[nseg].save=1.0*(walk[i].b-last)/s-1.0*(walk[i].b-last)/r;
               nseg++;            
            }
            last=walk[i].e;
        }
        if(x>last){
            walk[nseg].b=last;
            walk[nseg].e=x;
            walk[nseg].w=s;
             walk[nseg].flag=true;
             walk[nseg].save=1.0*(x-last)/s-1.0*(x-last)/r;
            nseg++;
        }
}
void solve()
{
    double maxuse;
    ans=0;
    for(int i=0;i<nseg;i++)
    {
            // printf("%d %d\n",walk[i].b,walk[i].e);
          if(walk[i].flag){
               maxuse=1.0*(walk[i].e-walk[i].b)/r;
                if(T>=maxuse){
                    ans+=maxuse;
                }else{
                    maxuse=T;
                    ans+=maxuse;
                    ans+=((walk[i].e-walk[i].b)-maxuse*r)/s;
                }
                T-=maxuse;
            }else{
              maxuse=1.0*(walk[i].e-walk[i].b)/(r+walk[i].w);
                if(T>=maxuse){
                    ans+=maxuse;
                }else{
                    maxuse=T;
                    ans+=maxuse;
                    ans+=((walk[i].e-walk[i].b)-maxuse*(r+walk[i].w))/(walk[i].w+s);
                }
                T-=maxuse;
            }
              //     printf("ans=%lf\n",ans);
    }
}
int main()
{
    int cs;
         freopen("A.out","w",stdout);
    scanf("%d",&cs);
    for(int t=1;t<=cs;t++)
    {
        printf("Case #%d: ",t);
        scanf("%d%lf%lf%lf%d",&x,&s,&r,&T,&n);
        for(int i=0;i<n;i++) {
            scanf("%d%d%d",&walk[i].b,&walk[i].e,&walk[i].w);
            walk[i].save=1.0*(walk[i].e-walk[i].b)/(walk[i].w+s)
                -1.0*(walk[i].e-walk[i].b)/(walk[i].w+r);
            walk[i].flag=false;
        }
        sort(walk,walk+n,cmp);
        build_all();
        sort(walk,walk+nseg,cmp2);
            //
            //for(int i=0;i<nseg;i++)
            //printf("%d %d\n",walk[i].b,walk[i].e);
            //
        ans=0;
        solve();
        printf("%.8lf\n",ans);
    }    
    return 0;
}
