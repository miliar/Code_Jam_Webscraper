#include <iostream>
#include <complex>
#include <vector>
using namespace std;
typedef complex<double> pt;
const double eps = 1e-6;

pt CMS[510][510][2], CMR[510][510][2], CMC[510][510][2], CM[510][510];
double W[510][510], WS[510][510][2], WR[510][510][2], WC[510][510][2];
char G[510][510];

int main() {
  int T, C = 1, nr, nc, d;
  cin >> T;
  while (T-- && cin >> nr >> nc >> d) {
    for (int i = 0; i < nr; ++i) {
      cin >> G[i];
      for (int j = 0; j < nc; ++j)
        W[i][j] = G[i][j] - '0' + 1;
    }

    int cur = 0;
    for (int r = 0; r < nr; ++r)
      for (int c = 0; c < nc; ++c) {
        CMS[r][c][!cur] = CMR[r][c][!cur] = CMC[r][c][!cur] = CM[r][c] = W[r][c] * pt(r + 0.5, c + 0.5);
        WR[r][c][!cur] = WC[r][c][!cur] = WS[r][c][!cur] = W[r][c];
      }

    int best = 0;
    for (int k = 2; k <= min(nr, nc); ++k) {
      for (int r = 0; r < nr; ++r)
        for (int c = 0; c < nc; ++c) {
          if (c+1 < nc) CMR[r][c][cur] = CMR[r][c+1][!cur] + CM[r][c], WR[r][c][cur] = WR[r][c+1][!cur] + W[r][c];
          if (r+1 < nr) CMC[r][c][cur] = CMC[r+1][c][!cur] + CM[r][c], WC[r][c][cur] = WC[r+1][c][!cur] + W[r][c];
        }

      for (int r = 0; r+k <= nr; ++r)
        for (int c = 0; c+k <= nc; ++c)
          CMS[r][c][cur] = CMS[r+1][c+1][!cur] + CMR[r][c][cur] + CMC[r+1][c][!cur], WS[r][c][cur] = WS[r+1][c+1][!cur] + WR[r][c][cur] + WC[r+1][c][!cur];

      bool f = false;
      if (k > 2) {
        for (int r = 0; !f && r+k <= nr; ++r)
          for (int c = 0; !f && c+k <= nc; ++c) {

            pt x = CMS[r+1][c+1][!cur] + CMR[r][c][cur] + CMC[r+1][c][!cur] -
              CM[r][c] - CM[r+k-1][c] - CM[r+k-1][c+k-1] - CM[r][c+k-1];
            double w = WS[r][c][cur] - W[r][c] - W[r+k-1][c] - W[r+k-1][c+k-1] -
              W[r][c+k-1];
            
            //cout << CMS[r+1][c+1][!cur] << endl;
            //cout << r << ' ' << c << ' ' << k << ' ' << x << ' ' << w << endl;
            
            pt p(r+(double)k/2.0, c+(double)k/2.0);
            
            if (abs((1.0/w)*x - p) < eps)
              f = true;
          }
      }
      if (f)
        best = k;

      cur = !cur;
    }
    
    cout << "Case #" << C++ << ": ";
    if (best) cout << best << endl;
    else cout << "IMPOSSIBLE" << endl;
  }
}
