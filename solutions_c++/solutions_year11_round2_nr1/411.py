#include <iostream>
#include <iomanip>

using namespace std;

const int MAX_N = 100;

double calcRPI(double WP, double OWP, double OOWP) {
  return 0.25*WP + 0.50*OWP + 0.25*OOWP;
  }

double calcWP(int t, int result[][MAX_N], int N, int ig = -1) {
  double num = 0, den = 0;
  for (int j = 0; j < N; ++j)
    if (j != ig) {
      if (result[t][j] != 0) {
        ++den;
        if (result[t][j] == 1)
          ++num;
        }
      }
  return num/den;
  }

double calcOWP(int t, int result[][MAX_N], int N) {
  double num = 0, den = 0;
  for (int j = 0; j < N; ++j)
    if ((j != t) && (result[t][j] != 0)) {
      num += calcWP(j, result, N, t);
      ++den;
      }
  return num/den;
  }

double calcOOWP(int t, int result[][MAX_N], double OWP[], int N) {
  double num = 0, den = 0;
  for (int j = 0; j < N; ++j)
    if ((j != t) && (result[t][j] != 0)) {
      num += OWP[j];
      ++den;
      }
  return num/den;
  }

int main() {
  cout << fixed << setprecision(7);
  int T; cin >> T;
  for (int cNum = 1; cNum <= T; ++cNum) {
    int N; cin >> N;

    int result[MAX_N][MAX_N] = {{0}};
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < N; ++j) {
        char c; cin >> c;
        if (c == '0')
          result[i][j] = -1;
        else if (c == '1')
          result[i][j] = 1;
        }

    double WP[MAX_N], OWP[MAX_N], OOWP[MAX_N];
    for (int i = 0; i < N; ++i) {
      WP[i] = calcWP(i, result, N);
      OWP[i] = calcOWP(i, result, N);
      }

    for (int i = 0; i < N; ++i)
      OOWP[i] = calcOOWP(i, result, OWP, N);

    cout << "Case #" << cNum << ":\n";
    for (int i = 0; i < N; ++i)
      cout << calcRPI(WP[i], OWP[i], OOWP[i]) << '\n';
    }
  }
