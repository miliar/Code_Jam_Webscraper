#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

int main() {
  int Tc;
  std::cin >> Tc;
  for (int tcase = 1; tcase <= Tc; ++tcase) {
    int R, C, D;
    std::cin >> R >> C >> D;


    vector<vector<int> > w;
    for (int i = 0; i < R; ++i) {
      w.push_back(vector<int>());
      for (int j = 0; j < C; ++j) {
        char tmp;
        std::cin >> tmp;
        w[i].push_back(tmp - '0');
      }
    }

    int maxr = 0;
    
    for (int i = 1; i < R - 1; ++i) {
      for (int j = 1; j < C - 1; ++j) {

          int m = std::min(std::min(i, R - 1 - i),
                           std::min(j, C - 1 - j));

          int ci = 0, cj = 0;
          int r = 0;

          while (r < m) {
            ++r;

            for (int di = -r; di <= r; ++di) {
              ci += di * w[i + di][j - r];
              cj += (-r) * w[i + di][j - r];
              ci += di * w[i + di][j + r];
              cj += r * w[i + di][j + r];
            }

            for (int dj = -(r-1); dj <= r-1; ++dj) {
              ci += (-r) * w[i - r][j + dj];
              cj += dj * w[i - r][j + dj];
              ci += r * w[i + r][j + dj];
              cj += dj * w[i + r][j + dj];
            }

            int ti = ci, tj = cj;

            ti -= (-r) * w[i - r][j - r];
            tj -= (-r) * w[i - r][j - r];
          
            ti -= (r) * w[i + r][j - r];
            tj -= (-r) * w[i + r][j - r];

            ti -= (-r) * w[i - r][j + r];
            tj -= (r) * w[i - r][j + r];

            ti -= (r) * w[i + r][j + r];
            tj -= (r) * w[i + r][j + r];

            if (ti == 0 && tj == 0 && maxr < 2*r+1) {
              maxr = 2*r+1;
            }
          }
      }
    }

    for (int i = 1; i < R - 2; ++i) {
      for (int j = 1; j < C - 2; ++j) {
        int m = std::min(std::min(i+1, R - 1 - i),
                         std::min(j+1, C - 1 - j));

        int ci = 0, cj = 0;
        ci += -1 * w[i][j];
        cj += -1 * w[i][j];
        ci += 1 * w[i+1][j];
        cj += -1 * w[i+1][j];
        ci += -1 * w[i][j+1];
        cj += 1 * w[i][j+1];
        ci += 1 * w[i+1][j+1];
        cj += 1 * w[i+1][j+1];

        int r = 1;

          while (r < m) {
            ++r;

            for (int di = -r + 1; di <= r; ++di) {
              ci += (2*di-1) * w[i + di][j + 1- r];
              cj += (-2*(r-1)-1) * w[i + di][j + 1 - r];
              ci += (2*di-1) * w[i + di][j + r];
              cj += (2*r-1) * w[i + di][j + r];
            }

            for (int dj = -(r-1) + 1; dj <= r-1; ++dj) {
              ci += (-2*(r-1)-1) * w[i + 1 - r][j + dj];
              cj += (2*dj-1) * w[i + 1 - r][j + dj];
              ci += (2*r-1) * w[i + r][j + dj];
              cj += (2*dj-1) * w[i + r][j + dj];
            }

            int ti = ci, tj = cj;

            ti -= (-2*(r-1)-1) * w[i + 1 - r][j + 1 - r];
            tj -= (-2*(r-1)-1) * w[i + 1 - r][j + 1 - r];
          
            ti -= (2*r-1) * w[i + r][j + 1 - r];
            tj -= (-2*(r-1)-1) * w[i + r][j + 1 - r];

            ti -= (-2*(r-1)-1) * w[i + 1 - r][j + r];
            tj -= (2*r-1) * w[i + 1 - r][j + r];

            ti -= (2*r-1) * w[i + r][j + r];
            tj -= (2*r-1) * w[i + r][j + r];

            if (ti == 0 && tj == 0 && maxr < 2*r) {
              maxr = 2*r;
            }
          }

      }
    }


    if (maxr > 0) {
      std::cout << "Case #" << tcase << ": " << maxr << std::endl;
    } else {
      std::cout << "Case #" << tcase << ": " << "IMPOSSIBLE" << std::endl;
    }
  }
}
