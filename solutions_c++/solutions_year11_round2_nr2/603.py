#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
#include <assert.h>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <fstream>
#include <sstream>
using namespace std;

#define FS(i,a) for(int i=0;a[i];++i)
#define FD(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,a) for(int i=0;i<a;++i)
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define PR2(a,n,m) REP(i,n){REP(j,m)cout<<a[i][j]<<' ';puts("");}
#define MP make_pair
#define CLQ(que) while(!que.empty()) que.pop();
#define CL(m,what) memset(m,what,sizeof(m))
#define READ(a) freopen(a,"r",stdin)
#define WRITE(a) freopen(a,"w",stdout)
#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define checkMin(a,b) (a=min(a,b))
#define checkMax(a,b) (a=max(a,b))
#define sq(a) ((a)*(a))
#define INF 1e20
#define EPS 1e-8
const double pi = acos(-1.0);
int dx[] = {-1, 0, 1, 0, 1, 1, -1, -1}; //up Right down Left
int dy[] = {0, 1, 0, -1, 1, -1, 1, -1};
typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef pair<int, int> PII;
//------------------------------------------------------------------------------
double d;
int c;
double p[200];
int v[200];

bool check(double s) {
  double lim = -INF;
  double x;
  REP(i, c) {
    x = max(p[i] - s, lim + d);
    lim = x;
    lim += d * (v[i] - 1);
    if (lim > p[i] + s + EPS) return false;
  }
  return true;
}

int main() {
#ifndef ONLINE_JUDGE
  READ("in");
  WRITE("out");
#endif
  int T, cas = 0;

  cin >> T;
  while (T--) {
    cin >> c >> d;
    REP(i, c) {
      cin >> p[i] >> v[i];
    }
    double low = 0;
    double hi = INF;
    double mid;
    double ret = 0;
    printf("Case #%d: ", ++cas);
    check(2.0);
    while (low + EPS< hi) {
      mid = (low + hi) / 2.0;
      //cout << mid << endl;
      if (check(mid)) {
        ret = mid;
        hi = mid;
      } else {
        low = mid;
      }
    }
    printf("%.8f\n", ret);
  }
  return 0;
}