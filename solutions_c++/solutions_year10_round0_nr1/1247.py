#include <iostream>

int
main()
{
  int T;
  std::cin >> T;
  for (int i(1); i <= T; ++i) {
    int N;
    int K;
    std::cin >> N >> K;
    int const C(1 << N);
    std::cout << "Case #" << i << ": "
      << ((K % C == C - 1) ? "ON\n" : "OFF\n");
  }
  return 0;
}
