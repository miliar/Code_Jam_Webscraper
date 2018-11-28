#include <iostream>

int main()
{
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N;
    std::cin >> N;
    int x = 0;
    int total = 0;
    int min = 1000000;
    for (int n = 0; n < N; ++n) {
      int cur;
      std::cin >> cur;
      x ^= cur;
      total += cur;
      if (min > cur)
	min = cur;
    }

    std::cout << "Case #" << t;
    if (x)
      std::cout << ": NO";
    else
      std::cout << ": " << (total - min);
    std::cout << std::endl;
  }
}
