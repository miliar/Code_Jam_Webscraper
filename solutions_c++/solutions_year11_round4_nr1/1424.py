#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
#include<vector>
#include<stack>
#include<map>
using namespace std;
int x,s,r,t,n,str[1001],end;
struct point
{
   int len,c;
}p[1002];
bool cmp(point x,point y)
{
    return x.c<y.c;
}
void rw();
void init()
{
    scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
    int a,b,c,len=0,aa,bb;
    for(int g=0;g<n;g++)
    {
        scanf("%d%d%d",&aa,&bb,&p[g].c);
        p[g].len=bb-aa;
        len+=bb-aa;
    }
    p[n].len=x-len;p[n].c=0;
    sort(p,p+n+1,cmp);
    double tt=t;
    double ans=0;
    for(int i=0;i<=n;i++)
    {
        if(p[i].len<tt*(r+p[i].c))
        {
            ans+=p[i].len/(1.0*r+p[i].c);
            tt-=p[i].len/(1.0*r+p[i].c);
        }
        else if(tt>0)
        {
            ans+=tt+(p[i].len-tt*(r+p[i].c))/(1.0*p[i].c+s);
            tt=-1;
        }
        else
        {
            ans+=p[i].len/(1.0*p[i].c+s);
        }
    }
    printf("%.9lf\n",ans);
}
void solve(){}
int main()
{
    rw();
    int Case;
    scanf("%d",&Case);
    for(int i=1;i<=Case;i++)
    {
        printf("Case #%d: ",i);
        init();
    }
return 0;
}

void rw()
{
freopen("E:\\A-large.in","r",stdin);
freopen("E:\\kk.out","w",stdout);
}
