/* 
 * Author: Hakobyan Tigran
 */

#pragma comment(linker, "/STACK:60777216") 
#define printTime(begin, end) printf("%.3lf\n", (double)(end - begin) / (double)CLOCKS_PER_SEC) 


#include <string.h>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#include <functional>
#include <complex>
#include <iostream>
#include <fstream>
#include <sstream>
#include <bitset>
#include <limits>
#include <ctime>
#include <cassert>
#include <valarray>

using namespace std;

#define IN(a) freopen(a, "r", stdin)
#define OUT(a) freopen(a, "w", stdout)

#define mp(a, b) make_pair(a, b)
#define det(a, b, c, d) (a * d - c * b)
#define sbstr(s, i, j) s.substr(i, j - i + 1)

#define clear(dp) memset(dp, -1, sizeof(dp))
#define reset(arr) memset(arr, 0, sizeof(arr))

#define EPS 1e-9
#define PI acos(-1.0)
#define MOD 1000000007
#define IINF 1000000000
#define LINF 6000000000000000000LL

int n = 4;
char a[5][5];
int test_id = 0;

void init () {
  for(int i = 0; i < n; ++i) {
    scanf("%s", a[i]);
  }
}

char c[2] = {'X', 'O'};

bool check (int id) {
  for(int i = 0; i < 4; ++i) {
    bool ok = true;
    for(int j = 0; j < 4; ++j) {
      if(a[i][j] == '.' || a[i][j] == c[id ^ 1]) {
        ok = false;
      }
    }
    if(ok) return true;
  }
  for(int j = 0; j < 4; ++j) {
    bool ok = true;
    for(int i = 0; i < 4; ++i) {
      if(a[i][j] == '.' || a[i][j] == c[id ^ 1]) {
        ok = false;
      }
    }
    if(ok) return true;
  }
  bool ok = true;
  for(int i = 0; i < 4; ++i) {
    if(a[i][i] == '.' || a[i][i] == c[id ^ 1]) {
      ok = false;
    }
  }
  if(ok) return true;
  ok = true;
  for(int i = 0; i < 4; ++i) {
    if(a[i][n - i - 1] == '.' || a[i][n - i - 1] == c[id ^ 1]) {
      ok = false;
    }
  }
  return ok;
}

bool full () {
  for(int i = 0; i < n; ++i) {
    for(int j = 0; j < n; ++j) {
      if(a[i][j] == '.') return false;
    }
  }
  return true;
}

void solve () {
  if(check(0)) {
    printf("Case #%d: %c won\n", ++test_id, c[0]);
  }
  else if(check(1)) {
    printf("Case #%d: %c won\n", ++test_id, c[1]);
  }
  else if(full()) {
    printf("Case #%d: Draw\n", ++test_id);
  }
  else {
    printf("Case #%d: Game has not completed\n", ++test_id);
  }
}

int main () {
#ifndef ONLINE_JUDGE
  IN("/home/tigran/Desktop/Debug/input.txt");
  OUT("/home/tigran/Desktop/Debug/output.txt");
#endif
  int test_case;
  scanf("%d", &test_case);
  while(test_case--) {
    init();
    solve();
  }
  return 0;
}
