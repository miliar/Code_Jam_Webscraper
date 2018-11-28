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
  int i, f, F, L, H, t, T;
  int fq[108];
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d %d %d", &F, &L, &H);
    for (i=0; i<F; i++)
      scanf("%d", &fq[i]);
    for (f=L; f<=H; f++) {
      for (i=0; i<F; i++)
        if (f%fq[i]!=0 && fq[i]%f!=0)
          break;
      if (i==F) {
        PRINT("Case #%d: %d\n", t, f);
        goto QUIT;
      }
    }
    PRINT("Case #%d: NO\n", t);
    QUIT:;
  }
  return 0;
}
