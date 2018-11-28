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
#include <assert.h>

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

char grid[60][60];
int n,m;


int main() {
  int ncases;
  scanf("%d",&ncases);
  FOR(ccases,ncases) {
    printf("Case #%d:\n",ccases+1);
    cin >> n >> m;
    FOR(i,n) cin >> grid[i];
    FOR(i,n-1) FOR(j,m-1) {
      if (grid[i][j] == '#' && grid[i+1][j] == '#' && grid[i][j+1] == '#' && grid[i+1][j+1] == '#') {
        grid[i][j] = '/';
        grid[i][j+1] = '\\';
        grid[i+1][j] = '\\';
        grid[i+1][j+1] = '/';
      }
    }
    bool ok = true;
    FOR(i,n) FOR(j,m) ok &= (grid[i][j] != '#');
    if (!ok) {
      cout << "Impossible" << endl;
    }
    else {
      FOR(i,n) cout << grid[i] << endl;
    }
  }
  return 0;
}
