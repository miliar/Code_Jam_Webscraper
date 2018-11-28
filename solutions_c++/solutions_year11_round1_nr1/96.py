#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int gcd(int a,int b) {
  return b==0?a:gcd(b,a%b);
}

int main() {
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  int ntest;
  cin>>ntest;
  for (int loop = 1; loop<=ntest; loop++) {
    long long n;
    int pd,pg;
    cin>>n>>pd>>pg;
    int gd = 100/gcd(pd,100),gg = 100/gcd(pg,100);
    if (pg==100) {
      if (pd==100) printf("Case #%d: Possible\n",loop);
      else printf("Case #%d: Broken\n",loop);
      continue;
    }
    if (pg==0) {
      if (pd==0) printf("Case #%d: Possible\n",loop);
      else printf("Case #%d: Broken\n",loop);
      continue;
    }
    if (gd<=n) printf("Case #%d: Possible\n",loop);
    else printf("Case #%d: Broken\n",loop);
  }
  return 0;
}
