#include<iostream>
int T,x,s,r,t,n;
int c[111],cc[111];
bool h[111];
using namespace std;

struct node{int b,e,w;}a[111];
bool cmp(node a1,node a2){return a1.b<a2.b;}

int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    for (int p=1; p<=T; p++)
      {
        scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
        memset(c,0,sizeof c);
        memset(cc,0,sizeof cc);
        memset(h,0,sizeof h);
        for (int i=1; i<=n; i++)
            scanf("%d%d%d",&a[i].b,&a[i].e,&a[i].w);
        sort(a+1,a+n+1,cmp);
        int num=1;
        c[1]=0;
        for (int i=1; i<=n; i++)
          {
            if (a[i].b!=c[num]) {c[++num]=a[i].b; cc[num]=0;}
            c[++num]=a[i].e; cc[num]=a[i].w;
          }
        if (c[num]!=x) c[++num]=x;
        double tt=double(t);
        double ans=0.0;
        while (tt>0)
          {
            bool ok=false;
            double jt=0,rt=0;
            int k;
            for (int i=2; i<=num; i++)
                if (h[i]==false) 
                  {
                    ok=true;
                    if (double(c[i]-c[i-1])/double(r+cc[i])<=tt)
                     {
                       double pt=double(c[i]-c[i-1])/double(s+cc[i])-double(c[i]-c[i-1])/double(r+cc[i]);
                       if (pt>jt) {jt=pt; rt=double(c[i]-c[i-1])/double(r+cc[i]);k=i;}
                     }
                    else
                     {
                       double pt=double(c[i]-c[i-1])/double(s+cc[i])-tt-double(c[i]-c[i-1]-tt*double(r+cc[i]))/double(s+cc[i]);
                       if (pt>jt) {jt=pt; rt=tt+double(c[i]-c[i-1]-tt*double(r+cc[i]))/double(s+cc[i]);k=i;}
                     }
                  }          
            if (ok==false) break;
            tt-=rt; h[k]=true; ans+=rt;     
          }
        for (int i=2; i<=num; i++)
            if (h[i]==false) ans+=double(c[i]-c[i-1])/double(s+cc[i]);
        printf("Case #%d: %.9lf\n",p,ans);
      }
}
