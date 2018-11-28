#include <iostream>
#include <algorithm>
using namespace std;

typedef long double ld;

const ld INF = 1e+30;
const ld EPS = 1e-9;

int N;
ld D;
ld pos[2000000];

bool fun(double dist) {
  ld last = -INF;
  for (int i = 0; i < N; ++i) {
    ld p = max(last + D, pos[i] - dist);
//     cerr << "i=" << i << " p=" << p << " last=" << last << endl;
    if (p > pos[i] + dist) return false;
    last = p;
  }
  return true;
}

int main() {
  cout.setf(ios::fixed);
  cout.precision(10);
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    int c;
    cin >> c >> D;
    N = 0;
    for (int i = 0; i < c; ++i) {
      ld p;
      int v;
      cin >> p >> v;
      for (int j = 0; j < v; ++j) pos[N++] = p;
    }
    sort(pos, pos + N);
    
//     cerr << N << endl;
    
    ld e = 0, d = INF;
    while (d - e > EPS) {
      ld m = 0.5*(e + d);
      if (fun(m)) {
        d = m;
//         cerr << "m=" << m << " ok" << endl;
      }
      else {
        e = m;
//         cerr << "m=" << m << " fail" << endl;
      }
    }
    
    cout << "Case #" << cas << ": " << d << endl;
//     break;
  }
}
