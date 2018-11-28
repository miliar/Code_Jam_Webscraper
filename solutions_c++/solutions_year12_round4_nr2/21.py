#include <cstdio>
#include <algorithm>
using namespace std;
int t,tt,n,A,B,down,i,j,xn,yn,dn,x[1010],y[1010],d[1010],xr[1010],yr[1010];
pair <int, int> a[1010];
int main() {
  freopen("Bl.in","r",stdin);
  freopen("Bl.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d%d",&n,&A,&B);
    for (i=0; i<n; i++) {
      scanf("%d",&a[i].first);
      a[i].second=i;
      d[i]=0;
    }
    sort(a,a+n);
    reverse(a,a+n);
    xr[a[0].second]=0;
    yr[a[0].second]=0;
    down=a[0].first;
    for (i=1; i<n; i++) {
      //printf("st %d\n",a[i].second);
      for (j=i-1; j>=0; j--) {
        yn=y[j]+a[j].first+a[i].first;
        //printf("after %d : %d\n",a[j].second,yn);
        if (yn>B) continue;
        //puts("oky");
        if (x[j]==0) {
          if (d[j]==0) {
            xn=0;
            dn=a[i].first;
          } else {
            xn=d[j]+a[i].first;
            dn=2*a[i].first;
          }
        } else {
          xn=x[j]-a[j].first+d[j]+a[i].first;
          dn=2*a[i].first;
        }
        //printf("%d\n",xn);
        if (xn>A || xn+a[i].first>x[j]+a[j].first) continue;
        //puts("okx");
        x[i]=xn; y[i]=yn; d[j]+=dn;
        break;
      }
      if (j<0) {
        down+=a[i].first;
        if (down<=A) {
          x[i]=down; y[i]=0;
        } else printf("!");
        down+=a[i].first;
      }
      xr[a[i].second]=x[i];
      yr[a[i].second]=y[i];
    }
    printf("Case #%d: ",t);
    for (i=0; i<n; i++) printf("%d %d%c",xr[i],yr[i],(i<n-1)?' ':'\n');
  }
  return 0;
}
