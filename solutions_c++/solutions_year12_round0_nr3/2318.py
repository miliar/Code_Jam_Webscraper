#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <fstream>
#include <numeric>
#include <limits.h>
#include <iomanip>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef long long ll;

#define ITE(v) typeof(v.begin())
#define FOR(i,n) for(int i = 0; i < n; i++)
#define FORIT(it,v) for(ITE(v) it = v.begin(); it != v.end(); it++)
#define ALL(v) v.begin(), v.end()
#define SZ(v) int(v.size())
#define pb push_back
#define SQR(a) ((a)*(a))

#define INF 0x3f3f3f3f
#define EPS (1e-9)

inline int cmp(double a, double b = 0.0) {
  if (fabs(a-b) <= EPS) return 0;
  if (a < b) return -1;
  return 1;
}

int h(int s, bool show = false) {
  int maxs = s;
  int m = 1;
  int ss = s;
  int cnt = 1;
  while (ss/m >= 10) m *= 10, cnt++;
  FOR(i, cnt) {
    if (show) cout << s << endl;
    int u = s/m;
    s = s - u*m;
    s = 10*s + u;
    if (s > maxs) maxs = s;
  }
  return maxs;
}

#define MAXV 10000000
int cnt[MAXV];

int main(int argc, char **argv) {
  if (argc > 1) {
    h(atoi(argv[1]), true);
    exit(0);
  }
  int ncases;
  cin >> ncases;
  FOR(kk, ncases) {
    memset(cnt, 0, sizeof(cnt));
    printf("Case #%d: ", kk+1);
    int a,b;
    cin >> a >> b;
    string s;
    for (int i = a; i <= b; i++) {
      cnt[h(i)]++;
    }
    ll res = 0;
    FOR(i,MAXV) res += 1LL*cnt[i]*(cnt[i]-1);
    cout << res/2 << endl;
  }
  return 0;
}
