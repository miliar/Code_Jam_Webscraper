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
  int i, j, C, D, E, N, t, T;
  char c;
  char bf[108];
  char el[108];
  char ds[26][26];
  char cm[26][26];
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    memset(cm, 0, sizeof cm);
    memset(ds, 0, sizeof ds);
    scanf("%d", &C);
    for (i=0; i<C; i++) {
      scanf("%s", bf);
      cm[bf[0]-'A'][bf[1]-'A']=bf[2];
      cm[bf[1]-'A'][bf[0]-'A']=bf[2];
    }
    scanf("%d", &D);
    for (i=0; i<D; i++) {
      scanf("%s", bf);
      ds[bf[0]-'A'][bf[1]-'A']=1;
      ds[bf[1]-'A'][bf[0]-'A']=1;
    }
    scanf("%d", &N);
    scanf("%s", bf);
    E=0;
    for (i=0; i<N; i++) {
      el[E++]=bf[i];
      while (true) {
        if (E>=2 && (c=cm[el[E-2]-'A'][el[E-1]-'A'])!=0) {
          E--;
          el[E-1]=c;
          continue;
        }
        for (j=0; j<E-1; j++)
          if (ds[el[j]-'A'][el[E-1]-'A'])
            break;
        if (j!=E-1)
          E=0;
        break;
      }
    }
    PRINT("Case #%d: [", t);
    if (E>0)
      PRINT("%c", el[0]);
    for (i=1; i<E; i++)
      PRINT(", %c", el[i]);
    PRINT("]\n");
  }
  return 0;
}
