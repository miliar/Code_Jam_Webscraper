#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

#define ll long long

const double eps=1E-9;

struct way{
    int b,e;
    int w;
    int num;
    double r,q;
};

int T;
int x,s,r,t,n;
way w[2000];
double tim,ans;
int len;

bool less0(const way & a,const way & b)
{
    if (abs(a.q-b.q)>eps) return a.q-b.q>eps;
    return a.num<b.num;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int k=1;k<=T;k++){
        scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
        len=x;
        for (int i=0;i<n;i++){
            scanf("%d%d%d",&w[i].b,&w[i].e,&w[i].w);
            len-=w[i].e-w[i].b;
            w[i].num=i;
            w[i].r=1.0/(r+w[i].w)*(w[i].e-w[i].b);
            w[i].q=1.0/(s+w[i].w)-1.0/(r+w[i].w);
        }
        w[n].e=len;w[n].b=0;
        w[n].num=n;w[n].w=0;
        w[n].r=len*1.0/r;w[n].q=1.0/s-1.0/r;
        sort(w,w+n+1,less0);
        tim=t;
        ans=0;
        for (int i=0;i<=n;i++){
            if (tim-w[i].r>eps){
                tim-=w[i].r;
                ans+=w[i].r;
            }else{
                ans+=tim+((w[i].e-w[i].b)-tim*(r+w[i].w))/(s+w[i].w);
                tim=0;
            }
        }
        printf("Case #%d: %.10lf\n",k,ans);
    }
    return 0;
}
