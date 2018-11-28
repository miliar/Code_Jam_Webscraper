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


int ncases;

int v[1010];
bool mark[1010];

int main() {
  cin >> ncases;
  FOR(kk,ncases) {
    printf("Case #%d: ",kk+1);
    int n;
    cin >> n;
    FOR(i,n) {
      cin >> v[i];
      v[i]--;
    }
    memset(mark,0,sizeof(mark));
    double res = 0;
    FOR(i,n) {
      if (mark[i]) continue;
      mark[i] = true;
      int sz = 1;
      int a = v[i];
      while (!mark[a]) {
        mark[a] = true;
        sz++;
        a = v[a];
      }
      if (sz > 1) res += sz;
    }
    printf("%.6lf\n",res);
  }
  return 0;
}
