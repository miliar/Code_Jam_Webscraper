#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>

using namespace std;

static const double EPS = 1e-5;

// typedefs
typedef unsigned long long     ULL;
typedef signed long long       LL;
typedef unsigned int           UINT;
typedef signed int             INT;

// macros
#define ALL(x)                 (x).begin(), (x).end()
#define RALL(x)                (x).rbegin(), (x).rend()
#define CLEAR(x, a)            memset(x, (a), sizeof(x))
#define FALL(i, a)             for(UINT i = 0; i < SZ(a); ++i)
#define FOR(i, a, b)           for(UINT i = (a); i < (b); ++i)
#define FORI(iter, x)          for(typeof(x.begin()) iter = x.begin(); iter != x.end(); ++iter)
#define PB(v, a)               v.push_back(a)
#define SZ(a)                  (UINT)(a).size()

int main() {
  //    freopen("C.in","r", stdin);
  //  freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
  freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
  //  freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
  //  freopen("A-small-practice.in","r", stdin);freopen("A-small-practice.out","w",stdout);
  //  freopen("A-large-practice.in","r", stdin);freopen("A-large-practice.out","w",stdout);

  UINT maxL = 110;
  char bugs[maxL + 1][maxL + 1];
  int numOfTestCases; scanf("%d",&numOfTestCases);

  for (int caseId=1; caseId <= numOfTestCases; caseId++) {
    CLEAR(bugs, '0'); FOR(i, 0, maxL) bugs[maxL][i] = '\0';
    // read each input
    int R; scanf("%d", &R);
    int x1 = 0; int x2 = 0; int y1 = 0; int y2 = 0;
    FOR(i, 0, R) {
      scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
      FOR(y, y1, y2 + 1) {
        FOR(x, x1, x2 + 1) {
          bugs[y - 1][x - 1] = '1';
        }
      }
    }

    char tmp[maxL + 1][maxL + 1];
    int result = 0;
    while(1) {
      CLEAR(tmp, '0');
      /*
      FOR(y, 0, maxL) {
        FOR(x, 0, maxL) {
            printf("%c", bugs[y][x]);
        }
        printf("\n");
      }
      printf("\n");
      */
      
      FOR(y, 0, maxL) {
        FOR(x, 0, maxL) {
          if(bugs[y][x] == '1') {
            if (x == 0 || y == 0) tmp[y][x] = '0';
            else if (bugs[y-1][x] == '1' || bugs[y][x-1] == '1') tmp[y][x] = '1';
            else tmp[y][x] = '0';
          } else {
            if (x == 0 || y == 0) tmp[y][x] = '0';
            else if (bugs[y-1][x] == '1' && bugs[y][x-1] == '1') tmp[y][x] = '1';
            else tmp[y][x] = '0';
          }
        }
      }

      bool updated = false;
      FOR(y, 0, maxL) FOR(x, 0, maxL) {
        bugs[y][x] = tmp[y][x];
        if (bugs[y][x] == '1') updated = true;
      }
      result++;
      if(!updated) break;
    };

    // result
    printf("Case #%d: ", caseId);
    printf("%d", result);
    printf("\n");
  }
  return 0;
}

