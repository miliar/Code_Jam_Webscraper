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
  int i, N, x, s, t, T;
  int nb[1000008];
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d", &N);
    for (i=x=s=0; i<N; i++) {
      scanf("%d", nb+i);
      x^=nb[i];
      s+=nb[i];
    }
    PRINT("Case #%d: ", t);
    if (x!=0)
      PRINT("NO");
    else {
      sort(nb, nb+i);
      PRINT("%d", s-nb[0]);
    }
    PRINT("\n");
  }
  return 0;
}
