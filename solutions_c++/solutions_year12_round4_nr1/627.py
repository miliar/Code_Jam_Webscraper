#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define FORE(it,V) for(__typeof(V.begin()) it = V.begin(); it != V.end(); ++it)
#define FI first
#define SE second
#define PB push_back
#define MP make_pair
typedef long long LL;

const int MAX_N = 10005;
int d[MAX_N], l[MAX_N];
bool mozna[MAX_N];
int najdluzsza[MAX_N];

void testcase() {
  int n;
  scanf("%d", &n);
  REP(i,n) {
    scanf("%d %d", d+i, l+i);
  }
  int D;
  scanf("%d", &D);
  REP(i,n) najdluzsza[i] = -1;
  najdluzsza[0] = d[0];

  REP(i,n) FOR(j,i+1,n-1) {
    if (d[i]+najdluzsza[i] >= d[j]) {
      najdluzsza[j] = max(najdluzsza[j], min(d[j] - d[i], l[j]));
    }
  }

  bool ok = false;
  REP(i,n) if (d[i] + najdluzsza[i] >= D) {
    ok = true;
    break;
  }
  if (ok) {
    printf("YES\n");
  } else {
    printf("NO\n");
  }
}

int main() {
  int t;
  scanf("%d", &t);
  REP(i,t) {
    printf("Case #%d: ", i+1);
    testcase();
  }
}
