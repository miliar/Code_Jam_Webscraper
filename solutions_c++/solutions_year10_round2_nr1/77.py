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

char bf[108];

int main() {
  int i, j, A, t, T, E, C;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    A=0;
    set<string> ex;
    vector<string> cr;
    scanf("%d %d", &E, &C);
    for (i=0; i<E; i++) {
      scanf("%s", bf);
      for (j=1; true; j++) {
        if (bf[j]=='\0') {
          ex.insert(bf);
          break;
        }
        if (bf[j]=='/') {
          bf[j]='\0';
          ex.insert(bf);
          bf[j]='/';
        }
      }
    }
    for (i=0; i<C; i++) {
      scanf("%s", bf);
      cr.push_back(bf);
    }
    sort(cr.begin(), cr.end());
    for (i=0; i<C; i++) {
      strcpy(bf, cr[i].c_str());
      for (j=1; true; j++) {
        if (bf[j]=='\0') {
          if (!ex.count(bf)) {
            A++;
            ex.insert(bf);
          }
          break;
        }
        if (bf[j]=='/') {
          bf[j]='\0';
          if (!ex.count(bf)) {
            A++;
            ex.insert(bf);
          }
          bf[j]='/';
        }
      }
    }
    PRINT("Case #%d: %d\n", t, A);
  }
  return 0;
}
