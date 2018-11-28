#include <cstdio>
#include <algorithm>
using namespace std;
int t,tt,x,s,r,ee,n,i,v[1010],k[1010];
double a,e,w,b[1010];
bool cmp(int i, int j) { return v[i]<v[j]; }
int main() {
  freopen("Al.in","r",stdin);
  freopen("Al.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d%d%lf%d",&x,&s,&r,&w,&n); b[n]=x; v[n]=0; k[n]=n;
    for (i=0; i<n; i++) { scanf("%lf%d%d",&b[i],&ee,&v[i]); b[i]=ee-b[i]; b[n]-=b[i]; k[i]=i; }
    sort(k,k+n+1,cmp);
    for (a=i=0; i<=n; i++) {
      if (w>0) {
        e=min(double(w),b[k[i]]/double(r+v[k[i]]));
        w-=e; b[k[i]]-=e*(r+v[k[i]]); a+=e;
      }
      if (b[k[i]]>0) a+=b[k[i]]/double(s+v[k[i]]);
    }
    printf("Case #%d: %.9lf\n",t,a);
  }
  return 0;
}
