#include <cstdio>
using namespace std;
int t,tt,w,n,m,k,i,ax[111],ay[111],bx[111],by[111];
double l,r,h,c,d,s;
double area(double r) {
  int i;
  double s=0,x,y,z;
  for (i=0; i<n-1; i++) {
    x=ax[i+1]-ax[i];
    y=ay[i+1]+ay[i];
    if (r<=ax[i+1]) {
      z=ay[i]+((r-ax[i])/x)*(ay[i+1]-ay[i]);
      s-=(r-ax[i])*(ay[i]+z);
      break;
    } else s-=x*y;
  }
  for (i=0; i<m; i++) {
    x=bx[i+1]-bx[i];
    y=by[i+1]+by[i];
    if (r<=bx[i+1]) {
      z=by[i]+((r-bx[i])/x)*(by[i+1]-by[i]);
      s+=(r-bx[i])*(by[i]+z);
      break;
    } else s+=x*y;
  }
  return 0.5*s;
}
int main() {
  freopen("Al.in","r",stdin);
  freopen("Al.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d%d%d",&w,&n,&m,&k);
    for (i=0; i<n; i++) scanf("%d%d",&ax[i],&ay[i]);
    for (i=0; i<m; i++) scanf("%d%d",&bx[i],&by[i]);
    s=area(double(w))/k;
    printf("Case #%d:\n",t);
    for (i=1; i<k; i++) {
      l=0; r=w; d=s*i;
      while (l<r-1e-8) {
        h=(l+r)*0.5;
        c=area(h);
        if (c<d) l=h; else r=h;
      }
      printf("%.8lf\n",(l+r)*0.5);
    }
  }
  return 0;
}
