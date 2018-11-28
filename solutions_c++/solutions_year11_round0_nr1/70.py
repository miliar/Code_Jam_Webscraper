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



ii v[200];

int main() {
  int ncases;
  cin >> ncases;
  int ccase = 1;
  while (ncases--) {
    int n;
    cin >> n;
    FOR(i,n) {
      char c;
      int p;
      cin >> c >> p;
      v[i] = ii(c,p);
    }
    int o = 1, b = 1;
    int wo = 0, wb = 0;
    int wait = 0;
    int t = 0;
    FOR(i,n) {
      //cout << (char)v[i].first << " " << v[i].second;
      if (v[i].first == 'O') {
        wait = abs(v[i].second - o) - wo;
        o = v[i].second;
        wait = max(wait,0);
        t += wait + 1;
        wb += wait + 1;
        wo = 0;
      }
      else {
        wait = abs(v[i].second - b) - wb;
        b = v[i].second;
        wait = max(wait,0);
        t += wait + 1;
        wo += wait + 1;
        wb = 0;
      }
    }
    printf("Case #%d: %d\n",ccase++,t);
  }
  return 0;
}
