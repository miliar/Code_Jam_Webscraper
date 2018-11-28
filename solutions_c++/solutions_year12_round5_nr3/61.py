#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
//#include <queue>
#include <iomanip>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

ll solve(ll m, ll m2, ll s2, ll s3, ll p3) {
  ll k = m2 / p3;
  if (m2 % p3 == 0 && k == s2 + 1) {
    return m / p3;
  }
  if (1 + s2 > k) {
    ll x = m / m2;
    return (s2 + 1) * x + min((m - m2 * x) / p3, (s3 - s2) * x);
  }
  ll m3 = m2 + p3 * (s3 - s2);
  ll x = min((m-1) / m3 + 1, m / m2);
  ll ans1 = (s2 + 1) * x + min((m - m2 * x) / p3, (s3 - s2) * x);
  x = min(m / m3, m / m2);
  ll ans2 = (s2 + 1) * x + min((m - m2 * x) / p3, (s3 - s2) * x);
  return max(ans1, ans2);
}

int main()
{
  int tcase = 0;
  cin >> tcase;
  for (int tind = 1; tind <= tcase; tind++) {
    int i,j;
    ll m, f;
    int n;
    ll p[201], s[201];
    cin >> m >> f >> n;
    for (i = 0; i < n; ++i) {
      cin >> p[i] >> s[i];
    }
    for (i = 0; i < n; ++i) {
      for (j = 0; j < n; ++j) {
        if (i < n && i != j && p[i] <= p[j] && s[i] >= s[j]) {
          n--;
          swap(p[j], p[n]);
          swap(s[j], s[n]);
        }
      }
    }
    for (i = 0; i < n; ++i) {
      for (j = i+1; j < n; ++j) {
        if (p[i] > p[j]) {
          swap(p[i], p[j]);
          swap(s[i], s[j]);
        }
      }
    }
    cerr << n << " food left" << endl;
    for (i = 0; i < n; ++i)
      cerr << p[i] << ' ' << s[i] << endl;
    ll sum = f;
    // solve(ll m, ll m2, ll s2, ll s3, ll p3)
    ll bestans = solve(m, sum, -1, s[0], p[0]);
    sum += (s[0] + 1) * p[0];
    for (i = 1; i < n; ++i) {
      ll ans = solve(m, sum, s[i-1], s[i], p[i]);
      bestans = max(bestans, ans);
      sum += (s[i] - s[i-1]) * p[i];
    }

    cout << "Case #" << tind << ": " << bestans << endl;
  }
  return 0;
}
