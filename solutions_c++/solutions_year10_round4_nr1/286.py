/* headers {{{1 */
#include <cassert>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <complex>
#include <iostream>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

/* defines {{{1 */
#define debug(x) cerr << __LINE__ << ": " << #x << " = " << (x) << "\n"
#define debugf(x...) fprintf(stderr, x)
#define mp make_pair
#define pb push_back
#define A first
#define B second
#define X real()
#define Y imag()
#define foreach(i, v) for (typeof(v.begin()) i = v.begin(); i != v.end(); ++i)

typedef long long ll;
const int inf = 1 << 29; const ll llinf = (ll)inf * (ll)inf;

/* funcs {{{1 */
template<class T> inline int sz(const T& v) { return (int)v.size(); }

template<class T> inline T gcd(T a, T b) { return (b == 0) ? a : gcd(b, a % b); }
template<class T> inline T cross(complex<T> a, complex<T> b) { return a.X * b.Y - b.X * a.Y; }
template<class T> inline int cross_sign(complex<T> a, complex<T> b) { 
  double t = (double)a.X * b.Y - (double)b.X * a.Y; 
  return (abs(t) < 1e-9) ? 0 : (t > 0); 
}
template<class T1, class T2> struct conv_impl { inline static T1 conv(T2 x) { stringstream ss; ss << x; T1 y; ss >> y; return y; } };
template<class T2> struct conv_impl<string, T2> { inline static string conv(T2 x) { stringstream ss; ss << x; return ss.str(); } };
template<class T1, class T2> inline T1 conv(T2 x) { return conv_impl<T1, T2>::conv(x); }
template<class T> inline vector<T> split(string x, string y=" \n\t") { 
  vector<T> r; 
  for (int i = 0; i <= sz(x); ) { 
    int j = x.find_first_of(y, i); 
    if (j < 0) j = sz(x); 
    r.pb(conv<T>(x.substr(i, j - i))); 
    i = j + 1;
  }
  return r; 
}
template<class T> inline vector<T> tokenize(string x, string y=" \n\t") { 
  vector<T> r; 
  for (int i = x.find_first_not_of(y); 0 <= i && i <= sz(x); ) { 
    int j = x.find_first_of(y, i); 
    if (j < 0) j = sz(x); 
    r.pb(conv<T>(x.substr(i, j - i))); 
    i = x.find_first_not_of(y, j);
  }
  return r; 
}
/* end }}}1 */

const int MAXK = 100, MAXN = 200;
int k, a[MAXN][MAXN];

int size(int pos) {
  int dist = max(pos, 2*k-2-pos);
  return dist + 1;
}

void solve_case() {
  scanf("%d", &k);
  memset(a, 255, sizeof(a));
  int num = 0, offset = k;
  for (int i = 0; i < 2*k-1; i++) {
    if (i < k) {
      num++;
      offset--;
    } else {
      num--;
      offset++;
    }

    for (int j = 0; j < num; j++) {
      scanf("%d", &a[i][offset + j*2]);
    }
  }

  /*
  printf("\n");
  for (int i = 0; i < 2*k-1; i++) {
    for (int j = 0; j < 2*k-1; j++)
      printf("%c ", (a[i][j] == -1) ? '_' : (a[i][j] + '0'));
    printf("\n");
  }
  printf("\n");
  */

  bool horiz[MAXN];
  for (int i = 0; i < 2*k-1; i++) {
    horiz[i] = true;
    for (int j = 0; j < 2*k-1 && horiz[i]; j++)
      for (int p = 0; p < i && horiz[i]; p++)
        if (i + (i - p) < 2*k-1 && a[j][p] != a[j][i + (i - p)] && a[j][p] != -1 && a[j][i + (i - p)] != -1)
          horiz[i] = false;
  }

  bool vert[MAXN];
  for (int i = 0; i < 2*k-1; i++) {
    vert[i] = true;
    for (int j = 0; j < 2*k-1 && vert[i]; j++)
      for (int p = 0; p < i && vert[i]; p++)
        if (i + (i - p) < 2*k-1 && a[p][j] != a[i + (i - p)][j] && a[p][j] != -1 && a[i + (i - p)][j] != -1)
          vert[i] = false;
  }

  int ans = 9999999;
  for (int i = 0; i < 2*k-1; i++)
    for (int j = 0; j < 2*k-1; j++)
      if (horiz[i] && vert[j])
        ans = min(ans, k + abs(i - (k-1)) + abs(j - (k-1)));

  printf("%d\n", ans*ans - k*k);

}

void base_init() {
}

const bool newline_after_case = false;

/* main {{{1 */
int main() {
  base_init(); 
  int t; 
  scanf("%d", &t);
  for (int i = 1; i <= t; ++i) {
    printf("Case #%d:%s", i, newline_after_case ? "\n" : " "); 
    solve_case();
  }
  return 0;
}
/* end }}}1 */


