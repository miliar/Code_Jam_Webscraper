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

int dt[108];
int sp[108];
int rc[108];

int main() {
  int i, j, C, M, D, Z, A, t, T;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d %d %d %d", &C, &M, &D, &Z);
    for (i=0; i<C; i++)
      scanf("%d", dt+i);
    for (i=0; i<C; i++)
      scanf("%d", sp+i);
    for (i=0; i<C; i++)
      rc[i]=0;
    A=0;
    for (i=C-1; i>=0 && M>0; i--)
      if (dt[i]+sp[i]*Z>=D) {
        M--;
        rc[i]=1;
        for (j=i+1; j<C; j++)
          if (!rc[j])
            A++;
      }
    if (M==0)
      PRINT("Case #%d: %d\n", t, A);
    else
      PRINT("Case #%d: %s\n", t, "IMPOSSIBLE");
  }
  return 0;
}
