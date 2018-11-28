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
#define INF 100000000
#define EPS 1e-14
const double pi = acos(-1.0);
int dx[] = {-1, 0, 1, 0, 1, 1, -1, -1}; //up Right down Left
int dy[] = {0, 1, 0, -1, 1, -1, 1, -1};
typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef pair<int, int> PII;
//------------------------------------------------------------------------------
int s, r;
struct node {
  int b, e, w;
  bool operator <(const node &t) const {
    return w < t.w;
    double x1 = 1.0 / (double)(s + w) - 1.0 / (double)(r + w);
    double x2 = 1.0 / (double)(s + t.w) - 1.0 / (double)(r + t.w);
    if (fabs(x1 - x2) > EPS) return x1 > x2;
    return e - b > t.e - t.b;
  }
}way[5000];

int main() {
#ifndef ONLINE_JUDGE
  READ("in");
  WRITE("out");
#endif
  int T, cas = 0;

  cin >> T;
  while (T--) {
    int x, n;
    double t;
    cin >> x >> s >> r >> t >> n;
    int sum = 0;
    REP(i, n) {
      scanf("%d%d%d", &way[i].b, &way[i].e, &way[i].w);
      sum += way[i].e - way[i].b;
    }
    int m;
    //cout << sum << endl;
    if (sum == x) {
      m = n;
    } else {
      m = n + 1;
      way[n].b = 0;
      way[n].e = x - sum;
      way[n].w = 0;
    }
//    int cur = 0;
//    int m = n;
//    REP(i, n) {
//      if (way[i].b == cur) {
//        cur = way[i].e;
//      } else {
//        way[m].b = cur;
//        way[m].e = way[i].b;
//        way[m].w = 0;
//        cur = way[i].e;
//        ++m;
//      }
//    }
//    if (way[n - 1].e != x) {
//      way[m].b = way[n - 1].e;
//      way[m].e = x;
//      way[m].w = 0;
//      ++m;
//    }
    
    sort(way, way + m);
    //cout << m << endl;
    double ret = 0;
    REP(i, m) {
      double l = way[i].e - way[i].b;
      //printf("%d %d %d %f %f\n", way[i].b, way[i].e, way[i].w, l, t);
      if (t > l / (r + way[i].w) + EPS || fabs(t - l / (r + way[i].w)) < EPS) {
        //cout << l << endl;
        t -= l / (r + way[i].w);
        ret += l / (r + way[i].w);
      } else {
        if (fabs(t) > EPS) {
          ret += t;
          l -= t * (r + way[i].w);
          //cout << l << endl;
          t = 0;
          ret += l / (s + way[i].w);
          //cout << ret << endl;
        } else {
          ret += l / (s + way[i].w);
        }
      }
    }
    printf("Case #%d: %.10f\n", ++cas, ret);
  }
  return 0;
}