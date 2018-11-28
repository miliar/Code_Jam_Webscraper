#include <cstdio>
using namespace std;
int t,tt,i,j,r;
bool a[1000111];
long long n,d,e;
int main() {
  freopen("Cl.in","r",stdin);
  freopen("Cl.out","w",stdout);
  for (i=2; i<=1000100; i++) if (!a[i]) for (j=i+i; j<=1000100; j+=i) a[j]=true;
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%I64d",&n); r=int(n>1);
    for (e=2; e<=1000100; e++) if (!a[e]) for (d=e*e; d<=n; d*=e, r++);
    printf("Case #%d: %d\n",t,r);
  }
  return 0;
}
