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
int n;
char str[200][200];
double wp[200], owp[200], oowp[200];
double ct[200];

void cal(double s[], double t[]) {
  int wt[200];
  REP(i, n) {
    t[i] = 0;
    REP(j, n) {
      if (str[i][j] == '1') {
        t[i] += s[j] * ct[j] / (ct[j] - 1);
      } else if (str[i][j] == '0') {
        t[i] += (s[j] * ct[j] - 1) / (ct[j] - 1);
      }
    }
    if (ct[i] != 0) t[i] /= ct[i];
    //cout << t[i] << endl;;
  }
}

int main() {
#ifndef ONLINE_JUDGE
  READ("in");
  WRITE("out");
#endif
  int T, cas = 0;
  cin >> T;
  while (T--) {
    printf("Case #%d:\n", ++cas);
    cin >> n;
    REP(i, n) {
      scanf("%s", str[i]);
      double cnt = 0;
      double win = 0;
      REP(j, n) {
        if (isdigit(str[i][j])) {
          ++cnt;
          if (str[i][j] == '1') {
            ++win;
          }
        }
      }
      ct[i] = cnt;
      if (cnt == 0)
        wp[i] = 0;
      else
        wp[i] = win / cnt;
      //printf("%f\n", wp[i]);
    }

    cal(wp, owp);
    REP(i, n) {
      oowp[i] = 0;
      REP(j, n) {
        if (str[i][j] != '.')
          oowp[i] += owp[j];
      }
      if (ct[i] != 0) {
        oowp[i] /= ct[i];
      }
    }
    //cal(owp, oowp);

    REP(i, n) {
      printf("%.8f\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
    }
  }
  return 0;
}