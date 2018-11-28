#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <sstream>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#define REP(i, n) for(int i=0; i<(int)n; ++i)
#define FOR(i, c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(),(c).end()
#define each(i, c) FOR(i, c)

#define VAR(a) cout << #a << " : " << a << endl;

typedef long long int lli;

using namespace std;

pair<double, double> f(double s1, double s2, double sum)
{
  double small = 0;
  double large = 1;
  for (int loop = 1000; loop--; ) {
    double c = (small + large) / 2.0;
    double a = c;
    double b = 1.0 - c;

    double p = s1 + sum * a;
    double q = s2 + sum * b;
    
    if (p == q) return make_pair(a, b);
    if (p < q) small = c;
    else large = c;
  }
  return make_pair(large, 1.0 - large);
  // return make_pair(1.0 - large, large);
}

int main(int argc, char *argv[])
{
  int tc;
  cin >> tc;
  while (tc--) {
    int n;
    cin >> n;
    double s[n];
    for (int i = 0; i < (int)n; ++i) {
      cin >> s[i];
    }

    double sum = accumulate(s, s + n, 0.0);

    priority_queue< pair<double, int> > q;
    for (int i = 0; i < (int)n; ++i) {
      q.push(make_pair(-s[i], i));
    }
    for (int loop = 100000000; loop--; ) {
      pair<double, int> p = q.top();
      q.pop();
      p.first -= sum * 0.00000001;
      q.push(p);
    }

    double r[n];

    // copy(s, s + n, r);
    
    // for (int loop = 100000000; 0 <= loop; ) {
    //   double mn = 1e125;
    //   for (int i = 0; i < (int)n; ++i) {
    //     mn = min(mn, r[i]);
    //   }
    //   for (int i = 0; i < (int)n && loop; ++i) {
    //     if (mn == r[i]) {
    //       r[i] += sum * 0.00000001;
    //       --loop;
    //     }
    //   }
    // }


    

    while (q.size()) {
      pair<double, int> p = q.top();
      q.pop();
      r[p.second] = -p.first;
    }

    static int tc = 0;
    printf("Case #%d:", ++tc);
    for (int i = 0; i < (int)n; ++i) {
      double m = r[i] - s[i];
      m /= sum;
      printf(" %.6lf", m * 100.0);
    }
    puts("");
  }
  // cout << 24.0 + 75.0 * 0.34666667 << endl;
  // cout << 30.0 + 75.0 * 0.26666667 << endl;
  // cout << 21.0 + 75.0 * 0.38666667 << endl;
  return 0;
}
