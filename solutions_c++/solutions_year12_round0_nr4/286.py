#include <cstdio>
#include <set>
#include <algorithm>
using namespace std;
int tt,T,n,m,d,i,j,x,y,stx,sty,dd,r;
char s[33];
set <pair <int, int> > st;
int gcd(int x, int y) { return y?gcd(y,x%y):x; }
int main() {
  freopen("Ds.in","r",stdin);
  freopen("Ds.out","w",stdout);
  scanf("%d",&tt);
  for (T=1; T<=tt; T++) {
    st.clear();
    scanf("%d%d%d",&n,&m,&d);
    for (r=i=0; i<n; i++) {
      scanf("%s",s);
      for (j=0; j<m; j++) if (s[j]=='X') { x=i; y=j; }
    }
    n-=2;
    m-=2;
    for (i=-d-2; i<=d+2; i++) for (j=-d-2; j<=d+2; j++) {
      stx=i*n+(i%2==0?x:(n-x+1))-x;
      sty=j*m+(j%2==0?y:(m-y+1))-y;
      if ((stx!=0 || sty!=0) && stx*stx+sty*sty<=d*d) {
        if (stx==0) {
          sty/=abs(sty);
        } else if (sty==0) {
          stx/=abs(stx);
        } else {
          dd=gcd(abs(stx),abs(sty));
          stx/=dd;
          sty/=dd;
        }
        if (st.count(make_pair(stx,sty))==0) {
          st.insert(make_pair(stx,sty));
          r++;
        }
      }
    }
    printf("Case #%d: %d\n",T,r);
  }
  return 0;
}
