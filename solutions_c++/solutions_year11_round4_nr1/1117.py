#include<iostream>
#include<algorithm>
using namespace std;
struct ww {
int l,r;
double w;
bool operator <(const ww q) const {
return w<q.w;
}
};
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int T,tt,x,n,i,j;
double ss,rs,t,mt,z;
ww a[1005];
cin>>T;
for(tt=1;tt<=T;tt++)
{
t=0;
cin>>x>>ss>>rs>>mt>>n;
a[0].l=0;
a[0].r=x;
a[0].w=0;
for(i=1;i<=n;i++)
{
cin>>a[i].l>>a[i].r>>a[i].w;
a[0].r-=a[i].r-a[i].l;
}
sort(a,a+n+1);
for(i=0;i<=n;i++)
{
if(mt>0)
{
z=min(mt,(a[i].r-a[i].l)/(rs+a[i].w));
mt-=z;
t+=z+(a[i].r-a[i].l-(z*(rs+a[i].w)))/(ss+a[i].w);
}
else
{
t+=(a[i].r-a[i].l)/(ss+a[i].w);
}
}
printf("Case #%d: %.9f\n",tt,t);
}
return 0;
}