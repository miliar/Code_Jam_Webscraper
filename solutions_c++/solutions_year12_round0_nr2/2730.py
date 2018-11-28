#include <iostream>
#include <numeric>
#include <cstring>


int N, S, p, t[100];


int memo_[100+1][10+1];


int search(int i, int j)
{
  int& r = memo_[i][j];

  if (r >= 0)
    return r;

  if (i == N)
    if (j == 0) {
      return r = 0;
    }
    else {
      return r = -(1 << 30);
    }

  if (t[i] == 3 * p - 4 || t[i] == 3 * p - 3) {
    if (j > 0 && 2 <= t[i] && t[i] < 29) {
      return r = std::max(search(i + 1, j - 1) + 1,
			  search(i + 1, j));
    }
    else {
      return r = search(i + 1, j);
    }
  }
  else if (3 * p - 2 <= t[i]) {
    if (j > 0 && 2 <= t[i] && t[i] < 29) {
      return r = std::max(search(i + 1, j - 1) + 1,
			  search(i + 1, j)     + 1);
    }
    else {
      return r = search(i + 1, j) + 1;
    }
  }
  else {
    if (j > 0 && 2 <= t[i] && t[i] < 29) {
      return r = std::max(search(i + 1, j - 1),
			  search(i + 1, j));
    }
    else {
      return r = search(i + 1, j);
    }
  }
}

int main(int argc, char** argv)
{
  int T;

  std::cin >> T;

  for (int i = 0; i < T; i ++) {
    std::cin >> N >> S >> p;

    memset(memo_, -1, sizeof(memo_));
    
    for (int j = 0; j < N; j ++)
      std::cin >> t[j];

    std::cout << "Case #" << i + 1 << ": " << search(0, S) << std::endl;
  }
}
