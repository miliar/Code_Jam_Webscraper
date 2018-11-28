#include <cstdio>
#include <cstring>

using namespace std;

int main() {
  //freopen("D-large.in","r",stdin);
  //freopen("D-large.out","w",stdout);
  int ntest;
  scanf("%d",&ntest);
  for (int loop = 1; loop<=ntest; loop++) {
    int n,co = 0;
    scanf("%d",&n);
    for (int i = 1,j; i<=n; i++) {
      scanf("%d",&j);
      if (i==j) co++;
    }
    printf("Case #%d: %.6f\n",loop,(double)n-co);
  }
  return 0;
}
