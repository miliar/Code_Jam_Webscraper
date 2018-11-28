#include <cstdio>
#include <cstdio>
#include <climits>

using namespace std;

int main() {
  //freopen("C-large.in","r",stdin);
  //freopen("C-large.out","w",stdout);
  int ntest;
  scanf("%d",&ntest);
  for (int loop = 1; loop<=ntest; loop++) {
    int n;
    scanf("%d",&n);
    int mmin = INT_MAX,sa = 0,sb = 0;
    for (int i = 0,x; i<n; i++) {
      scanf("%d",&x);
      sa ^= x; sb += x;
      if (mmin>x) mmin = x;
    }
    if (sa) printf("Case #%d: NO\n",loop);
    else printf("Case #%d: %d\n",loop,sb-mmin);
  }
  return 0;
}
