#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

int add_mod(int x, int y) {
  return x ^ y;
}

std::vector<int> candies;

int compute()
{
    int patrick_sum = std::accumulate(candies.begin(), candies.end(), 0, add_mod);
    if(patrick_sum != 0) {
      return 0;
    }
    int sean_sum = std::accumulate(candies.begin(), candies.end(), 0);
    int smallest = *std::min_element(candies.begin(), candies.end());
    return sean_sum - smallest;
}

int main()
{
  int T;
  std::cin >> T;
  for(int c=1;c<=T;c++) {
    candies.clear();

    int N;
    std::cin >> N;
    for(int i=0;i<N;i++) {
      int C;
      std::cin >> C;
      candies.push_back(C);
    }

    int value = compute();
    std::cout << "Case #" << c << ": ";
    if(value > 0)
      std::cout << value;
    else
      std::cout << "NO";
    std::cout << "\n";
  }
  return 0;
}
