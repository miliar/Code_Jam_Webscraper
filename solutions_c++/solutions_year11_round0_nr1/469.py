#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>

using namespace std;

int main() {
  //freopen("A.in","r",stdin);
  //freopen("A.out","w",stdout);
  int ntest;
  scanf("%d",&ntest);
  for (int loop = 1; loop<=ntest; loop++) {
    int n,ta = 0,tb = 0,ca = 1,cb = 1,ct = 0;
    scanf("%d",&n);
    for (int i = 0; i<n; i++) {
      char s[2]; int k,tmp;
      scanf("%s%d",s,&k);
      if (s[0]=='O') {
        tmp = abs(k-ca)+1-ta;
        if (tmp<=0) tmp = 1;
        ct += tmp;
        ta = 0;
        tb += tmp;
        ca = k;
      }
      else {
        tmp = abs(k-cb)+1-tb;
        if (tmp<=0) tmp = 1;
        ct += tmp;
        tb = 0;
        ta += tmp;
        cb = k;
      }
    }
    printf("Case #%d: %d\n",loop,ct);
  }
  return 0;
}
