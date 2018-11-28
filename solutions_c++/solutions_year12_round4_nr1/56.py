#include <iostream>
#include <vector>

int find_max_index(const std::vector<int>& maxes, const std::vector<bool>& processed) {
  int max_index = -1;
  int max = -1;
  for (int i = 0, e = maxes.size(); i < e; ++i) {
    if (maxes[i] >= max && !processed[i]) {
      max_index = i;
      max = maxes[i];
    }
  }
  return max_index;
}

int main() {
  int num_cases;
  std::cin >> num_cases;
  for (int casenum = 1; casenum <= num_cases; ++casenum) {
    int n;
    std::cin >> n;

    std::vector<int> d;
    std::vector<int> l;
    for (int i = 0; i < n; ++i) {
      int di, li;
      std::cin >> di >> li;
      d.push_back(di);
      l.push_back(li);
    }

    int D;
    std::cin >> D;

    // Given vine k, distance d, you can catch vine at location x in
    // [k-d,k+d] with new distance min(|x-k|, length(x)).

    // Only need to maintain max possible distance... can never
    // lengthen distance.

    // Go breadth first prioritizing max childs.

    std::vector<int> maxes(n, -1);
    std::vector<bool> processed(n, false);

    maxes[0] = d[0];

    bool success = false;
    for(;;) {
      int ix = find_max_index(maxes, processed);

      if (ix == -1) {
        break;
      }

      processed[ix] = true;

      int rope = maxes[ix];

      if (rope == -1) {
        break;
      }

      //      std::cout << "found max index with " << ix << " and rope " << rope << std::endl;

      if (rope + d[ix] >= D) {
        success = true;
        break;
      }

      for (int i = ix - 1; i >= 0 && d[ix] - d[i] <= rope; --i) {
        int dist = d[ix] - d[i];
        if (dist > l[i]) { dist = l[i]; }
        if (maxes[i] < dist) {
          maxes[i] = dist;
        }
      }

      for (int i = ix + 1; i < n && d[i] - d[ix] <= rope; ++i) {
        int dist = d[i] - d[ix];
        if (dist > l[i]) { dist = l[i]; }
        if (maxes[i] < dist) {
          maxes[i] = dist;
        }
      }
    }

    std::cout << "Case #" << casenum << ": " << (success ? "YES" : "NO") << std::endl;
  }

}
