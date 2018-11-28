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
  
  //return 0;
  int T, c, d, n, cas = 0;
  cin >> T;
  char com[100][5];
  char opp[100][5];
  char str[1001];
  char ans[1001];
  while (T--) {
    cin >> c;
    REP(i, c) cin >> com[i];
    cin >> d;
    REP(i, d) cin >> opp[i];
    cin >> n >> str;
    int l = 0;
    bool ff;
    FOR(i, 0, n) {
      ff = false;
      if (l) {
        REP(j, c) {
          if (str[i] == com[j][0] && ans[l - 1] == com[j][1] ||
                  str[i] == com[j][1] && ans[l - 1] == com[j][0]) {
            ans[l - 1] = com[j][2];
            ff = true;
            break;
          }
        }
      }
      if (ff) continue;
      ff = false;
      REP(j, d) {
        //bool gg = false;
        //if (ff) break;
        if (str[i] == opp[j][0]) {
          REP(k, l) {
            if (ans[k] == opp[j][1]) {
              l = 0;
              ff = true;
              break;
            }
          }
        } else if (str[i] == opp[j][1]) {
          REP(k, l) {
            if (ans[k] == opp[j][0]) {
              l = 0;
              ff = true;
              break;
            }
          }
        }
      }
      if (ff) continue;
      ans[l++] = str[i];
    }
    printf("Case #%d: %c", ++cas, 91);
    REP(i, l - 1) {
      printf("%c, ", ans[i]);
    }
    if (l) printf("%c", ans[l - 1]);
    printf("%c\n", 93);
  }
  return 0;
}