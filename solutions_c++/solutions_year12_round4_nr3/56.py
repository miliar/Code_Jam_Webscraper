#include <iostream>
#include <vector>

#include <stdint.h>

// i->j highest means i->j greatest forward from i
// 

void fill_between_peaks(const std::vector<int>& h, std::vector<int>& heights,
                        int p, int p_height, int n, int n_height, bool *impossible) {
  for (int i = p + 1; i < n; ++i) {
    if (h[i] > n) {
      *impossible = true;
      return;
    }

    if (h[i] == n) {
      // (n_height - x) / (n - i) > (x - p_height) / (i - p)
      // (n_height - x) * (i - p) > (x - p_height) * (n - i)
      //  + n_height * (i - p) + p_height * (n - i) > x * ((n - p))
      int64_t m = int64_t(n_height) * int64_t(i - p);
      m += int64_t(p_height) * int64_t(n - i);
      int64_t x = (m - 1) / (n - p);

      heights[i] = x;

      // new_p_height <= n_height - ((n_height - x) / (n - i)) * (n - p)

      int64_t new_p_height = n_height - (int64_t(n_height - x) * int64_t(n - p) + (n - i)) / (n - i);
      fill_between_peaks(h, heights, p, new_p_height, i, x, impossible);

      if (*impossible) { return; }

      fill_between_peaks(h, heights, i, x, n, n_height, impossible);
      return;
    }

  }
}

int main() {
  int num_cases;
  std::cin >> num_cases;
  for (int casenum = 1; casenum <= num_cases; ++casenum) {
    int n;
    std::cin >> n;
    std::vector<int> h;
    for (int i = 0; i < n-1; ++i) {
      int highest;
      std::cin >> highest;
      h.push_back(highest - 1);
    }

    std::vector<int> heights(n, -1);

    bool impossible = false;

    int w = 0;
    while (!impossible && w < n - 1) {
      int prev_w = w;
      w = h[w];
      heights[prev_w] = 999999999;
      heights[w] = 999999999;
      fill_between_peaks(h, heights, prev_w, 999999999, w, 999999999, &impossible);
    }

    // done!

    std::cout << "Case #" << casenum << ":";
    if (impossible) {
      std::cout << " Impossible" << std::endl;
    } else {
      for (int i = 0; i < n; ++i) {
        std::cout << " " << heights[i];
      }
      std::cout << std::endl;
    }


  }

}
