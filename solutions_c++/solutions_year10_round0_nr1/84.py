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

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;

#define ITE(v) typeof(v.begin())
#define FOR(i,n) for(int i = 0; i < n; i++)
#define FORIT(it,v) for(ITE(v) it = v.begin(); it != v.end(); it++)
#define ALL(v) v.begin(), v.end()
#define SZ(v) int(v.size())
#define pb push_back
#define SQR(a) ((a)*(a))

#define INF 0x3f3f3f3f
#define EPS (1e-8)

inline int cmp(double a, double b = 0.0) {
  if (fabs(a-b) <= EPS) return 0;
  if (a < b) return -1;
  return 1;
}


int main() {
  long long ntest;
  cin >> ntest;
  long long kk = 1;
  while (ntest--) {
    cout << "Case #" << kk++ << ": ";
    long long n, k;
    cin >> n >> k;
    long long mask = 1LL<<n;
    mask--;
    if ((k&mask) == mask) cout << "ON" << endl;
    else cout << "OFF" << endl;
    // while (mask) {
    //   cout << (mask&1);
    //   mask >>= 1;
    // }
    // cout << endl;
    // while (k) {
    //   cout << (k&1);
    //   k >>= 1;
    // }
    // cout << endl;

  }
  return 0;
}
