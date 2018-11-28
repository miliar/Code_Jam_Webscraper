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

int main() {
  cin >> ncases;
  FOR(kk,ncases) {
    printf("Case #%d: ",kk+1);
    int n;
    cin >> n;
    int minv = INT_MAX;
    int nimsum = 0;
    int sum = 0;
    int a;
    FOR(i,n) {
      cin >> a;
      sum += a;
      minv = min(minv,a);
      nimsum ^= a;
    }
    if (nimsum != 0) cout << "NO" << endl;
    else cout << sum-minv << endl;
  }
  return 0;
}
