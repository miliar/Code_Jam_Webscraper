#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
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

#define PR2(a,n,m) REP(i,n){REP(j,m)cout<<a[i][j]<<' ';puts("");}
#define MP make_pair
#define CLQ(que) while(!que.empty()) que.pop();
#define CL(m,what) memset(m,what,sizeof(m))
#define FS(i,a) for(int i=0;a[i];++i)
#define FD(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,a) for(int i=0;i<a;++i)
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define READ(a) freopen(a,"r",stdin)
#define WRITE(a) freopen(a,"w",stdout)
#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define checkMin(a,b) (a=min(a,b))
#define checkMax(a,b) (a=max(a,b))
#define sq(a) ((a)*(a))
#define INF 100000000
#define EPS 1e-8
int dx[] = {-1, 0, 1, 0, 1, 1, -1, -1}; //up Right down Left
int dy[] = {0, 1, 0, -1, 1, -1, 1, -1};
typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef pair<int, int> PII;
//------------------------------------------------------------------------------

int main() {
#ifndef ONLINE_JUDGE
  READ("in");
  WRITE("out");
#endif
  int T, n, cas = 0;
  cin >> T;
  char str[10];
  while (T--) {
    cin >> n;
    int co = 0, cb = 0;
    int poso = 1, posb = 1;
    int m;
    while (n--) {
      scanf("%s%d", str, &m);
      if (str[0] == 'O') {
        co += abs(m - poso) + 1;
        checkMax(co, cb + 1);
        poso = m;
      } else {
        cb += abs(m - posb) + 1;
        checkMax(cb, co + 1);
        posb = m;
      }
    }
    //printf("%d %d\n", co, cb);
    printf("Case #%d: %d\n", ++cas, max(co, cb));
  }
  return 0;
}