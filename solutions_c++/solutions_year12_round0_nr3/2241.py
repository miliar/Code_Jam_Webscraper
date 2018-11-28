#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

int bn[2000008];

int main() {
  int t, T;
  int A, B, C, d, n, m, p;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d %d", &A, &B);
    for (d=1; d*10<=A; d*=10)
      ;
    C=0;
    memset(bn, 0, sizeof bn);
    for (n=A; n<B; n++)
      for (p=1; p<d; p*=10) {
        m=n/(10*p)+(n%(10*p))*(d/p);
        if (n<m && m<=B && bn[m]!=n) {
          C++;
          bn[m]=n;
        }
      }
    printf("Case #%d: %d\n", t, C);
  }
  return 0;
}
