#include <iostream>
using namespace std;

char A[120][120];
double WP[120], WPX[120][120], OWP[120], OOWP[120];

int main() {
  int T, C = 1, n;
  cin >> T;
  while (T-- && cin >> n) {
    for (int i = 0; i < n; ++i)
      cin >> A[i];

    for (int i = 0; i < n; ++i) {
      int W = 0, L = 0;
      for (int j = 0; j < n; ++j) {
        if (A[i][j] == '0') ++L;
        else if (A[i][j] == '1') ++W;
      }

      WP[i] = double(W)/double(W + L);
      for (int j = 0; j < n; ++j) {
        int w = 0, l = 0;
        if (A[i][j] == '0') ++l;
        else if (A[i][j] == '1') ++w;
        WPX[i][j] = double(W - w)/double(W - w + L - l);
      }
    }

    for (int i = 0; i < n; ++i) {
      int c = 0;
      OWP[i] = 0;
      for (int j = 0; j < n; ++j) {
        if (A[j][i] != '.') {
          OWP[i] += WPX[j][i];
          ++c;
        }
      }
      OWP[i] /= c;
    }

    for (int i = 0; i < n; ++i) {
      int c = 0;
      OOWP[i] = 0;
      for (int j = 0; j < n; ++j) {
        if (A[j][i] != '.') {
          OOWP[i] += OWP[j];
          ++c;
        }
      }
      OOWP[i] /= c;
    }

    cout << "Case #" << C++ << ":" << endl;
    cout.setf(ios::fixed);
    cout.precision(12);
    for (int i = 0; i < n; ++i) {
      cout << 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i] << endl;
    }
  }
}
