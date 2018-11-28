#include<iostream>
using namespace std;

typedef long long lli;
struct point { lli x,y; point (lli a,lli b) { x=a, y=b; } };
lli cross(point a,point b) { return a.x*b.y-a.y*b.x; }
lli across(point a,point b) { return abs(cross(a,b)); }
lli m,n,a;

int main()
{
  int ci,cn;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  {
    cin>>n>>m>>a;
    lli i,j,k,l;
    for(i=0;i<=n;++i) for(j=0;j<=m;++j)
      for(k=0;k<=n;++k) for(l=0;l<=m;++l)
      { lli ar=across(point(i,-j),point(k,l-j));
        if(ar==a) goto fullbreak;
      }
fullbreak:
    if(i<=n) cout<<"Case #"<<ci<<": "<<i<<" 0 0 "<<j<<' '<<k<<' '<<l<<endl;
    else cout<<"Case #"<<ci<<": IMPOSSIBLE"<<endl;

  }
}
