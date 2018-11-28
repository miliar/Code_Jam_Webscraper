/* GCJ'09 Template v.2e-9
 * Per Austrin
 */
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cctype>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef map<string, int> msi;

int CASES;

void init() {
  scanf("%d", &CASES);
}

double sqr(double x) { return x*x; }

void solve(int P) {
  int N;
  scanf("%d", &N);
  int X[1000], Y[1000], R[1000];
  for (int i = 0; i< N; ++i)
    scanf("%d%d%d", X+i, Y+i, R+i);

  double ans = 0;
  if (N == 1) ans = R[0];
  else if (N == 2) ans = max(R[0], R[1]);
  else if (N == 3) {
    ans = 1e30;
    for (int i = 0; i < 3; ++i)
      for (int j = 0; j < i; ++j) {
	double d = sqrt(sqr(X[i]-X[j]) + sqr(Y[i]-Y[j]));
	ans = min(ans, max((d+R[i]+R[j])/2.0, 1.0*R[3-i-j]));
      }
  }
  
  printf("Case #%d: %.9lf\n", P, ans);
}

int main(void) {
  init();
  for (int i = 1; i <= CASES; ++i) solve(i);
  return 0;
}
