#include <vector>
#include <algorithm>
#include <iostream>

int64_t calc()
{
  size_t n;
  std::cin >> n;
  // Input two vectors of size n
  std::vector<int64_t> x(n), y(n);
  for (size_t i = 0; i < n; i++)
    std::cin >> x[i];
  for (size_t i = 0; i < n; i++)
    std::cin >> y[i];
  // Sort both vectors in opposite orders
  std::sort(x.begin(), x.end(), std::less<int64_t>());
  std::sort(y.begin(), y.end(), std::greater<int64_t>());
  // Calculate dot product of sorted (permuted) vectors
  int64_t product = 0;
  for (size_t i = 0; i < n; i++)
    product += x[i] * y[i];
  return product;
}

int main()
{
  size_t count;
  std::cin >> count;
  for (size_t i = 0; i < count; i++) {
    std::cout << "Case #" << (i + 1) << ": " << calc() << std::endl;
  }
}
