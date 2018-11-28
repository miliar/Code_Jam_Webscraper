/* headers {{{1 */
#include <cassert>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <complex>
#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
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
#define sz(v) ((int)(v).size())
#define foreach(i, v) for (typeof(v.begin()) i = v.begin(); i != v.end(); ++i)

typedef long long ll;
const int inf = 1 << 29; const ll llinf = (ll)inf * (ll)inf;

/* funcs {{{1 */
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

const int MAXN = 20;
int w, h;

bool grid[MAXN][MAXN];

int n;

struct set_t {
  pair< int, int > pos[5];

  void add(int r, int c) {
    pos[n++] = mp(r, c);
  }

  bool stable() {
    if (n == 1) return true;

    return abs(pos[0].A - pos[1].A) + abs(pos[0].B - pos[1].B) == 1;
    /*
    bool ok = true;
    for (int i = 0; i < n; ++i) {
      bool ok2 = false;
      for (int j = 0; j < n; ++j) if (i != j && abs(pos[i].A - pos[j].A) + abs(pos[i].B - pos[j].B) == 1) ok2 = true;
      ok = ok & ok2;
    }
    return ok;
    */
  }

  inline pair<int, int> get_corner() {
    pair<int, int> r = mp(20, 20);
    for (int i = 0; i < n; ++i) {
      r.A = min(r.A, pos[i].A);
      r.B = min(r.B, pos[i].B);
    }
    return r;
  }

  inline ll get_mask(pair<int, int> c) {
    ll r = 0;
    for (int i = 0; i < n; ++i) {
      r |= 1ll << ((pos[i].A - c.A) * 8 + (pos[i].B - c.B));
    }
    return r;
  }

  inline bool col(int r, int c) {
    for (int i = 0; i < n; ++i) if (pos[i].A == r && pos[i].B == c) return true;
    return false;
  }

  void print() {
    for (int r = 0; r < h; ++r) {
      for (int c = 0; c < w; ++c) cerr << (col(r, c) ? '#' : '.');
      cerr << '\n'; 
    }

  }
} start, goal;

int n_mask_id = 0;
map< ll, int > mask_id;

int get_id(set_t& s, pair<int, int> c) {
  ll m = s.get_mask(c);
  if (mask_id.count(m) == 0) mask_id[m] = n_mask_id++;
  return mask_id[m];
}

set< pair< pair<int, int>, int> > seen;

bool has_seen(set_t s) {
  pair<int, int> c = s.get_corner();
  int id = get_id(s, c);
  if (seen.count(mp(c, id))) return true;
  seen.insert(mp(c, id));
  return false;
}

vector< set_t > q;

const int dr[] = {0, 1, 0, -1}, dc[] = {1, 0, -1, 0};

bool good(int r, int c) {
  return r >= 0 && c >= 0 && r < h && c < w && !grid[r][c];
}

void solve_case() {
  cin >> h >> w;

  start = set_t();
  goal = set_t();

  int n2;
  n = n2 = 0;

  for (int r = 0; r < h; ++r) {
    string s;
    cin >> s;

    for (int c = 0; c < w; ++c) {
      grid[r][c] = s[c] == '#';
      if (s[c] == 'o' || s[c] == 'w') start.pos[n++] = mp(r, c);
      if (s[c] == 'x' || s[c] == 'w') goal.pos[n2++] = mp(r, c);
    }
  }

  sort(start.pos, start.pos + n);
  sort(goal.pos, goal.pos + n);

  seen.clear();
  q.clear();

  has_seen(start);

  int qs = 0, qe = 0, qne = 1;
  q.pb(start);

  int t = 0;

  while (qe < qne) {
    qe = qne;
    t++;
    while (qs < qe) {
      set_t x = q[qs++];

      //x.print();

      bool ok = true;
      for (int i = 0; i < n; ++i) if (!goal.col(x.pos[i].A, x.pos[i].B)) ok = false;

      if (ok) {
        cout << t - 1 << '\n';
        return;
      }

      bool stable = x.stable();

      for (int i = 0; i < n; ++i) {
        int r = x.pos[i].A, c = x.pos[i].B;
        for (int d = 0; d < 4; ++d) {
          int ra = r + dr[d], rb = r - dr[d], ca = c + dc[d], cb = c - dc[d];

          if (!good(ra, ca) || !good(rb, cb)) continue;
          if (x.col(ra, ca) || x.col(rb, cb)) continue;

          set_t y = x;
          y.pos[i].A += dr[d];
          y.pos[i].B += dc[d];

          if (!stable && !y.stable()) continue;

          if (!has_seen(y)) {
            sort(y.pos, y.pos + n);
            q.pb(y);
            qne++;
          }
        }
      }
    }
  }



  cout << "-1\n";
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


