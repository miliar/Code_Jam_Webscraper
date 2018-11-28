#include <iostream>
#include <vector>
#include <algorithm>

int main() {
  int Tc;
  std::cin >> Tc;
  for (int tcase = 1; tcase <= Tc; ++tcase) {
    int X, S, R, t, N;
    std::cin >> X >> S >> R >> t >> N;

    std::vector<int> B(N);
    std::vector<int> E(N);
    std::vector<int> W(N);
    std::vector<std::pair<int, int> > L(N+1);

    int sum = 0;
    for (int i = 0; i < N; ++i) {
      std::cin >> B[i] >> E[i] >> W[i];
      L[i+1].second = E[i] - B[i];
      L[i+1].first = W[i];
      sum += L[i+1].second;
    }

    L[0].second = X - sum;
    L[0].first = 0;

    std::sort(L.begin(), L.end());

    // now chop

    double tot = 0.0;
    double u = t;

    for (int i = 0; i < N + 1; ++i) {
      double seglen = L[i].second;
      int segsp = L[i].first;
      if (u > 0) {
        double t_rns = seglen / (R + segsp);

        if (t_rns < u) {
          tot += t_rns;
          u -= t_rns;
        } else {
          tot += u;
          seglen -= (u * (R + segsp));
          u = 0;
          goto remainder;
        }
      } else {
      remainder:
        double t_walk = seglen / (S + segsp);

        tot += t_walk;
      }
    }

    std::cout.setf(std::ios::fixed, std::ios::floatfield);
    std::cout.precision(10);
    std::cout << "Case #" << tcase << ": " << tot << std::endl;
  }
}
