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
  int i, j, Y, X, f, t, T;
  char gd[108][108];
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d %d", &Y, &X);
    for (i=0; i<Y; i++)
      scanf("%s", gd[i]);
    for (i=0; i<Y-1; i++)
      for (j=0; j<X-1; j++)
        if (gd[i][j]=='#' && gd[i][j+1]=='#' && gd[i+1][j]=='#' && gd[i+1][j+1]=='#') {
          gd[i][j]=gd[i+1][j+1]='/';
          gd[i][j+1]=gd[i+1][j]='\\';
        }
    f=0;
    for (i=0; i<Y; i++)
      for (j=0; j<X; j++)
        f|=(gd[i][j]=='#');
    PRINT("Case #%d:\n", t);
    if (f)
      PRINT("Impossible\n");
    else
      for (i=0; i<Y; i++)
        PRINT("%s\n", gd[i]);
  }
  return 0;
}
