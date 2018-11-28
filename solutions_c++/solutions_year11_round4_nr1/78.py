#include <iostream>
#include <iomanip>
#include <map>
using namespace std;

struct walk {
  int B, E, w;
  bool operator<(const walk& o) const {
    return B < o.B;
  }
};

walk W[1010];

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int X, S, R, T, N;
    cin >> X >> S >> R >> T >> N;
    for (int i = 0; i < N; i++)
      cin >> W[i].B >> W[i].E >> W[i].w;
    sort(W, W+N);

    map<int, int> st;
    int used = 0;
    for (int i = 0; i < N; i++) {
      st[W[i].w+S] += W[i].E-W[i].B;
      used += W[i].E-W[i].B;
    }
    st[S] += X-used;

    double res = 0, rt = T;
    for (map<int, int>::iterator it = st.begin(); it != st.end(); ++it) {
      double run = min(1.0*it->second, rt*(it->first+R-S));
      res += run / (it->first+R-S);
      res += (it->second-run) / it->first;
      rt -= run / (it->first+R-S);
    }
    cout.setf(ios::fixed);
    cout << setprecision(8);
    cout << "Case #" << c << ": " << res << endl;
  }
  return 0;
}
