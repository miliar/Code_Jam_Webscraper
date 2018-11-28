#include <iostream>
#include <vector>

int
main()
{
  int T;
  std::cin >> T;
  for (int t(1); t <= T; ++t) {
    int R;
    int k;
    int N;
    std::cin >> R >> k >> N;
    std::vector<int> g(N);
    for (int n(0); n < N; ++n) {
      std::cin >> g[n];
    }
    int total(0);
    int idx(0);
    for (int r(0); r < R; ++r) {
      int n_group(0);
      int n_ride(0);
      for (;;) {
        if ((n_group < N) && (n_ride + g[idx] <= k)) {
          ++n_group;
          n_ride += g[idx];
        } else {
          total += n_ride;
          break;
        }
        if (++idx == N) {
          idx = 0;
        }
      }
    }
    std::cout << "Case #" << t << ": " << total << '\n';
  }
  return 0;
}
