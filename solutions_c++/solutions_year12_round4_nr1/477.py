#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <iostream>

using namespace std;

#define pb push_back
#define mp make_pair
#define x first
#define y second
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define sz(a) (int)((a).size())
#define all(a) (a).begin(), (a).end()

typedef long long ll;
typedef long double ld;
typedef pair <int, int> pii;

#define maxn 10010

int T;
int N, D;
int d[maxn], l[maxn];

int maxl[maxn];

ld sqr(ld x) {
  return x * x;
}

int main() {
  scanf("%d", &T);
  for (int q = 1; q <= T; q++) {
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
      scanf("%d %d", &d[i], &l[i]);
    }
    scanf("%d", &D);

    for (int i = 0; i < N; i++) {
      maxl[i] = 0;
    }

    bool ok = false;
    maxl[0] = d[0];
    for (int i = 0; i < N; i++) {
      if (maxl[i] > l[i]) maxl[i] = l[i];
      if (maxl[i] <= 0) continue;
      ok |= maxl[i] >= D - d[i];
      for (int j = i + 1; j < N; j++) {
        if (d[j] - d[i] <= maxl[i])
          maxl[j] = max(maxl[j], min((d[j] - d[i]), l[j]));
      }
    }

    printf("Case #%d: %s\n", q, ok ? "YES" : "NO");
  }
  

  return 0;
}
