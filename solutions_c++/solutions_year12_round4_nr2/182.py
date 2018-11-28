#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define X first
#define Y second
#define PB push_back
#define FOR(x,y) for (int x = 0; x < int(y); ++x)
#define debug(x) cerr << #x << " = " << x << endl

typedef long long ll;
typedef long double ld;
typedef pair<int, int> P;
typedef vector<bool> Vb;
typedef vector<Vb> Mb;
typedef vector<char> Vc;
typedef vector<Vc> Mc;
typedef vector<int> Vi;
typedef vector<Vi> Mi;
typedef vector<P> Vp;
typedef vector<Vp> Mp;
typedef vector<string> Vs;
typedef vector<Vs> Ms;

typedef queue<int> Q;
typedef priority_queue<int> PQ;
typedef stack<int> STACK;
typedef set<P> SET;
typedef SET::iterator Sit;
typedef map<int, int> MAP;
typedef MAP::iterator Mit;
typedef stringstream SS;

template <class Ta, class Tb> inline Tb cast(Ta a) { SS ss; ss << a; Tb b; ss >> b; return b; };

const double EPS = 1e-9;
const int INF = 1000000000;
const int MOD = 1000000007;
const int diri[8] = { -1, 0, 1, 0, -1, 1, 1, -1 };
const int dirj[8] = { 0, 1, 0, -1, 1, 1, -1, -1 };

bool sortf(P a, P b) {
  return a.X > b.X;
}

ll dist2(P a, P b) {
  ll x = b.X - a.X;
  ll y = b.Y - a.Y;
  return x*x + y*y;
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    cerr << "RUNNING CASE " << cas << endl;
    int n;
    cin >> n;
    
    int dx, dy;
    cin >> dx >> dy;
    
    Vi rad(n);
    for (int i = 0; i < n; ++i)
      cin >> rad[i];
    
    Vp v(n);
    for (int i = 0; i < n; ++i) v[i] = P(rad[i], i);
    sort(v.begin(), v.end(), sortf);
    
    SET cand;
    cand.insert(P(0, 0));
    cand.insert(P(0, dy));
    cand.insert(P(dx, 0));
    cand.insert(P(dx, dy));
    
    Vp res(n);
    
    int oks = 0;
    
    for (int i = 0; i < n; ++i) {
      int r = v[i].X;
      
      Vp prova;
      for (Sit it = cand.begin(); it != cand.end(); ++it) {
        P p = *it;
        prova.PB(p);
        prova.PB(P(p.X - r, p.Y - r));
        prova.PB(P(p.X - r, p.Y + r));
        prova.PB(P(p.X + r, p.Y - r));
        prova.PB(P(p.X + r, p.Y + r));
        
        prova.PB(P(p.X, p.Y - r));
        prova.PB(P(p.X, p.Y + r));
        prova.PB(P(p.X + r, p.Y));
        prova.PB(P(p.X + r, p.Y));
      }
      sort(prova.begin(), prova.end());
      
      int sz = prova.size();
      for (int j = 0; j < sz; ++j) {
        int x = prova[j].X;
        int y = prova[j].Y;
        bool ok = 0 <= x and x <= dx and 0 <= y and y <= dy;
        for (int k = 0; ok and k < i; ++k) {
          ll d = dist2(res[k], prova[j]);
          if (d < ll(r + v[k].X)*ll(r + v[k].X)) ok = false;
        }
        if (ok) {
//           cerr << "OK! " << v[i].Y << " -> (" << x << " " << y << ")" << endl;
          cand.insert(P(x + r, y + r));
          cand.insert(P(x + r, y - r));
          cand.insert(P(x - r, y + r));
          cand.insert(P(x - r, y - r));
          
          cand.insert(P(0, y - r));
          cand.insert(P(0, y + r));
          cand.insert(P(dx, y - r));
          cand.insert(P(dx, y + r));
          
          cand.insert(P(x - r, 0));
          cand.insert(P(x + r, 0));
          cand.insert(P(x - r, dy));
          cand.insert(P(x + r, dy));
          
          res[i] = prova[j];
          ++oks;
          break;
        }
      }
    }
    
    if (oks != n) cerr << "ERROR CASE " << cas << endl;
    
    Vp res2(n);
    for (int i = 0; i < n; ++i) res2[v[i].Y] = res[i];
    
    cout << "Case #" << cas << ":";
    for (int i = 0; i < n; ++i) cout << " " << res2[i].X << " " << res2[i].Y;
    cout << endl;
    
//     for (int i = 0; i < n; ++i)
//       for (int j = 0; j < n; ++j) {
//         if (i == j) continue;
//         ll d = dist2(res2[i], res2[j]);
//         if (d < ll(rad[i] + rad[j])*ll(rad[i] + rad[j])) {
//           cerr << i << " VS " << j << endl;
//         }
//       }
  }
}
