#include <iostream>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <numeric>

#include <cmath>
#include <cctype>

#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

#define FOREACH(iter, cont) for(__typeof((cont).begin()) iter = (cont).begin(); iter != (cont).end(); iter++)
#define FOR(i, begin, end) for(int i = (begin); i < (end); i++)
#define CLEAR(arr) memset(arr, 0, sizeof(arr))
#define ALL(cont) (cont).begin(),(cont).end()

const int maxn = 10100;

int t[maxn], c[maxn];
int a[maxn][2];

int n;

inline int f(int a, int b, int t) {
  return (t == 1) ? (a&b) : (a|b);
}

void compute(int x) {
  if (x < (n-1)/2) {
    int l = 2*x+1;
    int r = 2*x+2;
    compute(l);
    compute(r);
    a[x][0] = -1;
    a[x][1] = -1;

#define check(p, q, r, h) if (q != -1 && r != -1 && (a[x][h] == -1 || p+q+r < a[x][h])) a[x][h] = p+q+r;

      check(0, a[l][0], a[r][0], f(0, 0, t[x]));
      check(0, a[l][0], a[r][1], f(0, 1, t[x]));
      check(0, a[l][1], a[r][0], f(1, 0, t[x]));
      check(0, a[l][1], a[r][1], f(1, 1, t[x]));
    if (c[x]) {
      check(1, a[l][0], a[r][0], f(0, 0, 1-t[x]));
      check(1, a[l][0], a[r][1], f(0, 1, 1-t[x]));
      check(1, a[l][1], a[r][0], f(1, 0, 1-t[x]));
      check(1, a[l][1], a[r][1], f(1, 1, 1-t[x]));
    }
  }
  else {
    a[x][t[x]] = 0;
    a[x][1-t[x]] = -1;
  }
}

int main() {
  int cases;
  cin >> cases;
  for (int cs = 1; cs <= cases; cs++) {
    int v;
    cin >> n >> v;
    FOR(i, 0, (n-1)/2) 
      cin >> t[i] >> c[i];
    FOR(i, (n-1)/2, n) 
      cin >> t[i];

    compute(0);
    cout << "Case #" << cs << ": ";
    if (a[0][v] != -1) 
      cout << a[0][v];
    else 
      cout << "IMPOSSIBLE";
    cout << endl; 
  }
}
