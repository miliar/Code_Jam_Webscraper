#include <cstdio>
#define LL long long

LL n, m, A;
LL x1,y1,x2,y2,x3,y3;

bool calc()
{
  x1=y1=0;
  for(x2=0;x2<=n;x2++)
    for(y2=0;y2<=m;y2++) {
      if(x2==0 && x2==0) continue;
      for(x3=0;x3<=n;x3++)
	for(y3=0;y3<=m;y3++)
	  if(x2*y3-y2*x3==A) return 1;
    }
  return 0;
}

int main()
{
  int tt;
  scanf("%d", &tt);
  for(int t=1;t<=tt;t++) {
    scanf("%lld%lld%lld", &n, &m, &A);
    bool r=calc();
    if(!r) printf("Case #%d: IMPOSSIBLE\n", t);
    else printf("Case #%d: %lld %lld %lld %lld %lld %lld\n", t, x1, y1, x2, y2, x3, y3);
  }
  return 0;
}
