#include <cstdio>
#include <set>
using namespace std;
int t,tt,n,m,i,x,p,a,b[10101];
multiset <int> s;
int main() {
  freopen("Bl.in","r",stdin);
  freopen("Bl.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d",&n); s.clear(); m=0; x=20000;
    for (i=0; i<10101; i++) b[i]=0;
    for (i=0; i<n; i++) { scanf("%d",&a); b[a]++; }
    for (i=0; i<10101; i++) {
      for (; m>b[i]; m--) {
        p=(*s.begin());
        if (i-p<x) x=i-p;
        s.erase(s.begin());
      }
      for (; m<b[i]; m++) s.insert(i);
    }
    printf("Case #%d: %d\n",t,(x==20000)?0:x);
  }
  return 0;
}
