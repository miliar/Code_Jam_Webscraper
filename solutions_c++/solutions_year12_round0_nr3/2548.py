#include <stdio.h>
int tt,T,x,y,z,a,b,c,i,it,u[2000002];
long long r;
int main() {
  freopen("Cs.in","r",stdin);
  freopen("Cs.out","w",stdout);
  scanf("%d",&tt);
  for (T=1; T<=tt; T++) {
    scanf("%d%d",&a,&b);
    r=0;
    for (x=1; x*10<=a; x*=10);
    for (i=a; i<b; i++) {
      ++it;
      for (z=x, y=10; z>=10; z/=10, y*=10) {
        c=i%y*z+i/y;
        if (c>i && c<=b && u[c]!=it) {
          u[c]=++it;
          r++;
        }
      }
    }
    printf("Case #%d: %I64d\n",T,r);
  }
  return 0;
}
