#include <iostream>
#include <string>

int convert[26] = {
  0, 8, 9, 1, 2, 3, 10, 11, 12, 13, 14, 15, 16,
  17, 18, 19, 4, 5, 6, 20, 21, 22, 7, 23, 24, 25
};

int main()
{
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int combine[26][26] = {0};
    int oppose[26][26] = {0};

    int C;
    std::cin >> C;
    for (int c = 0; c < C; ++c) {
      std::string s;
      std::cin >> s;
      int a = s[0] - 'A';
      int b = s[1] - 'A';
      int c = s[2] - 'A' + 1;
      combine[a][b] = c;
      combine[b][a] = c;
    }

    int D;
    std::cin >> D;
    for (int d = 0; d < D; ++d) {
      std::string s;
      std::cin >> s;
      int a = s[0] - 'A';
      int b = s[1] - 'A';
      oppose[a][b] = 1;
      oppose[b][a] = 1;
    }

    int N;
    std::cin >> N;
    std::string in;
    std::cin >> in;

    int out[100];
    int size = 0;
    for (int n = 0; n < N; ++n) {
      int cur = in[n] - 'A';

      while (size > 0 && combine[cur][out[size - 1]] > 0) {
	cur = combine[cur][out[size - 1]] - 1;
	--size;
      }

      for (int i = 0; i < size; ++i) {
	if (oppose[cur][out[i]]) {
	  cur = -1;
	  break;
	}
      }
      if (cur >= 0) {
	out[size] = cur;
	++size;
      } else {
	size = 0;
      }
    }

    std::cout << "Case #" << t << ": [";
    if (size > 0)
      std::cout << (char)(out[0] + 'A');
    for (int i = 1; i < size; ++i)
      std::cout << ", " << (char)(out[i] + 'A');
    std::cout << "]" << std::endl;
  }
}
