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


int main() {
  int ncases;
  cin >> ncases;
  FOR(kk, ncases) {
    int res = 0;
    printf("Case #%d: ", kk+1);
    int n,s,p;
    cin >> n >> s >> p;
    FOR(i,n) {
      int sc;
      cin >> sc;
      bool ok = true;
      for (int j = 0; j <= 10; j++) {
        for (int k = j; k <= j+1; k++) {
          for (int l = k; l <= j+1; l++) {
            if (l >= p && ok && j+k+l == sc) res++, ok = false;
          }
        }
      }
      if (ok == false || s == 0) continue;
      for (int j = 0; j <= 10; j++) {
        for (int k = j; k <= j+2; k++) {
          for (int l = k; l <= j+2; l++) {
            if (l >= p && s && ok && j+k+l == sc) res++, ok = false, s--;
          }
        }
      }
    }
    cout << res << endl;
  }
  return 0;
}
