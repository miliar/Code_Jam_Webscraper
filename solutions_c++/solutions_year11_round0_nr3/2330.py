#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstddef>
using namespace std;

int main()
{
  size_t num_test_cases;
  cin >> num_test_cases;
  for (size_t i = 0; i < num_test_cases; ++i)
  {
    std::vector<size_t> candies;

    size_t num_candies;
    cin >> num_candies;
    for (size_t j = 0; j < num_candies; ++j)
    {
      size_t candy;
      cin >> candy;
      candies.push_back(candy);
    }

    size_t total_xor = accumulate(candies.begin(), candies.end(), 0, std::bit_xor<size_t>());

    cout << "Case #" << i + 1 << ": ";
    if (total_xor != 0)
    {
      cout << "NO";
    }
    else
    {
      std::sort(candies.begin(), candies.end());
      cout << accumulate(candies.begin() + 1, candies.end(), 0);
    }
    cout << endl;
  }
}
