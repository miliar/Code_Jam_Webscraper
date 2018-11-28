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
#define EPS 1e-8
const double pi = acos(-1.0);
int dx[] = {-1, 0, 1, 0, 1, 1, -1, -1}; //up Right down Left
int dy[] = {0, 1, 0, -1, 1, -1, 1, -1};
typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef pair<int, int> PII;
//------------------------------------------------------------------------------

int n, m, d;
char w[1000][1000];

int main() {
#ifndef ONLINE_JUDGE
  READ("in");
  WRITE("out");
#endif
  int T, cas = 0;

  cin >> T;
  while (T--) {
    cin >> n >> m >> d;
    REP(i,n) {
      scanf("%s", w[i]);
    }
    int ret = 0;
    double sx, sy, ox, oy, sum;
    REP(i, n) {
      REP(j, m) {
        FOR(x, 3, n - i + 1) {
            sx = 0;
            sy = 0;
            sum = 0;
            int y = x;
            REP(ii, x) {
              REP(jj, y) {
                if (ii == 0 && jj == 0 ||
                        ii == 0 && jj == y - 1 ||
                        ii == x - 1 && jj == y - 1 ||
                        ii == x - 1 && jj == 0)
                  continue;
                sx += (w[ii + i][jj + j] + d) * (ii + i);
                sy += (w[ii + i][jj + j] + d) * (jj + j);
                sum += w[ii + i][jj + j] + d;
              }
            }

            sx /= sum;
            sy /= sum;
            ox = (double)(x - 1) / 2.0 + i;
            oy = (double)(y - 1) / 2.0 + j;
//            if (i == 1 && j == 1) {
//              printf("%f %f %f %f\n", sx, sy, ox, oy);
//              printf("%f\n", sum);
//            }
            if (fabs(sx - ox) < EPS && fabs(sy - oy) < EPS) {
              checkMax(ret, x);
            }

        }
      }
    }
    if (ret == 0) {
      printf("Case #%d: IMPOSSIBLE\n", ++cas);
    } else {
      printf("Case #%d: %d\n", ++cas, ret);
    }
  }
  return 0;
}