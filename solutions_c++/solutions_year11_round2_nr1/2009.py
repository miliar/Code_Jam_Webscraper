#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <list>

#define FOR(i, m, n) for (int i=m; i<n; i++)

using namespace std;

long long V[500], P[500];
long long D, C;

int main() {
  int t; scanf("%d", &t);
  FOR (www, 0, t) {
    long long sum = 0;
    scanf("%lld%lld", &C, &D);
    int pocet = 0;
    long long maly = 1000000, velky = -1000000;
    FOR (i, 0, C) {
      scanf("%d%d", &P[i], &V[i]);
      maly = min(maly, P[i]); velky = max(velky, P[i]);
      sum += V[i];
    }
    long double l = maly - sum*D;
    long double r = velky + sum*D;
    while(l<=r) {
      long double h = (l+r)/2.0;
    }
  }
  return 0;
}
