#include <cstdio>
#include <cmath>
using namespace std;

int n,m,a;

int main() {
  int cases,kase=0;
  for (scanf("%d",&cases);cases>0;cases--) {
    scanf("%d%d%d",&n,&m,&a);
    bool found=false;
    for (int i=1;i<=int(sqrt(1.0*a))+1;i++) {
      if (a%i==0) {
	int k1=i,k2=a/i;
	if (k1<=n && k2<=m) {
	  printf("Case #%d: %d %d %d %d %d %d\n",++kase,0,0,k1,0,0,k2);
	  found=true;
	  break;
	}
	if (k1<=m && k2<=n) {
	  printf("Case #%d: %d %d %d %d %d %d\n",++kase,0,0,k2,0,0,k1);
	  found=true;
	  break;
	}
      }
    }
    if (!found) printf("Case #%d: IMPOSSIBLE\n",++kase);
  }
}
