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

#define PRUSH(stream, format, args...) do { fprintf(stream, format, ## args); fflush(stream); } while (0)
#define DEBUG(format, args...) do { PRUSH(stderr, format, ## args); } while (0)
#define PRINT(format, args...) do { PRUSH(stdout, format, ## args); DEBUG(format, ## args); } while (0)

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

int main() {
  int t, T;
  int N, S, P, A, b, v;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d %d %d", &N, &S, &P);
    A=0;
    while (N--) {
      scanf("%d", &v);
      b=v/3;
      if (v%3==0 && b-1>=0 && b+1==P && S>0)
        A++, S--;
      else if (v%3==2 && b+2==P && S>0)
        A++, S--;
      else if (b+!!(v%3)>=P)
        A++;
    }
    PRINT("Case #%d: %d\n", t, A);
  }
  return 0;
}
