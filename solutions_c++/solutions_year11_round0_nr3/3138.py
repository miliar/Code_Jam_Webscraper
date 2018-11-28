#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

typedef signed   long long i64;
typedef unsigned long long u64;

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define setall(x, val) memset((x), (val), sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define For(i, st, en) for(iint i=(st); i<=(en); i++)
#define Ford(i, st, en) for(iint i=(st); i>=(en); i--)
#define forn(i, n) for(int i=0; i<(n); i++)
#define fors(i, n, s) for(int i=s; i<(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)
#define ind(i, j, cols) (i * cols + j)


int addPatrik(int a, int b) {
  int res = 0, addA, addB, pp = 0;
  while (a > 0 || b > 0) {
    addA = a ? a % 2 : 0;
    addB = b ? b % 2 : 0;
    a /= 2; b /= 2;
    if (addA + addB == 1) res += 1 << pp;
    pp++;
  }
  return res;
}

void calc() {
  int t, n, res, sum, mm, nums[1001];
  scanf("%d\n", &t);
  forn(tt, t) {
    res = -1;
    scanf("%d", &n);
    forn(i, n) scanf("%d", &nums[i]);
    sum = 0;
    forn(i, n) sum = addPatrik(sum, nums[i]);
    if (!sum) {
      mm = 10000000;
      forn(i, n) {
        res += nums[i];
        mm = min(nums[i], mm);
      }
      res -= mm - 1;
    }
    if (res < 0) printf("Case #%d: NO\n", tt+1);
    else printf("Case #%d: %d\n", tt+1, res);
  }
}

int main() {
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);

  calc();

  return 0;
}
