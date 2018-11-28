#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
using namespace std;

#define X first
#define Y second
#define PB push_back

typedef long long ll;
typedef long double ld;
typedef long long ent;
typedef pair<ll, ll> P;
typedef vector<ll> Vi;
typedef vector<Vi> Mi;
typedef vector<P> Vp;
typedef vector<Vp> Mp;

typedef queue<int> Q;
typedef set<int> SET;
typedef SET::iterator Sit;
typedef map<int, int> MAP;
typedef MAP::iterator Mit;
typedef stringstream SS;
typedef pair<int, P> PP;
typedef vector<PP> Vpp;

const int INF = 1000000000;



int main() {
  cout.setf(ios::fixed);
  cout.precision(9);
  
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    ll X, S, R, T, N;
    cin >> X >> S >> R >> T >> N;
    Vi B(N), E(N), W(N);
//     Vpp vect(N);
    for (ll i = 0; i < N; ++i) {
      cin >> B[i] >> E[i] >> W[i];
//       cin >> vect[i].X >> vect[i].Y.X >> vect[i].Y.Y;
    }
//     sort(vect.begin(), vect.end());
    
//     for (int i = 0; i < N; ++i) {
// //       B[i] = vect[i].X;
//       E[i] = vect[i].Y.X;
//       W[i] = vect[i].Y.Y;
//     }
    
    int p = 0;
    ll pos = 0;
    
    Vp vect;
    
    while (p < N) {
      if (pos == B[p]) {
        vect.PB(P(W[p], E[p] - B[p]));
        pos += E[p] - B[p];
        ++p;
      }
      else {
        vect.PB(P(0, B[p] - pos));
        pos = B[p];
      }
    }
    if (pos < X) vect.PB(P(0, X - pos));
    
    sort(vect.begin(), vect.end());
    
    ld res = 0;
    ld tim = T;
    
    int M = vect.size();
    for (int i = 0; i < M; ++i) {
      ld t = vect[i].Y/ld(R + vect[i].X);
      t = min(t, tim);
      tim -= t;
      ld r = t*(R + vect[i].X);
      res += t + (vect[i].Y - r)/ld(S + vect[i].X);
    }
    
//     ld res = 0;
    
    cout << "Case #" << cas << ": " << res << endl;
  }
}
