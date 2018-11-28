#include <iostream>


template <typename T>
T gcd(T a, T b)
{
  for (;;) {
    if (a == 0) {
      return b;
    }
    b %= a;
    if (b == 0) {
      return a;
    }
    a %= b;
  }
}


int main()
{
  size_t number_of_cases;
  std::cin >> number_of_cases;
  
  for (size_t case_index = 1; case_index <= number_of_cases; ++case_index) {
    long long n, pd, pg;
    std::cin >> n >> pd >> pg;
    
    bool is_broken = false;
    
    if (pg == 100 && pd != 100) {
      is_broken = true;
    }
    if (pg == 0 && pd != 0) {
      is_broken = true;
    }
    
    if (pd > 0) {
      const long long k = gcd(100LL, pd);
      if (100 / k > n) {
        is_broken = true;
      }
    }
    
    std::cout << "Case #" << case_index << ": " << (is_broken ? "Broken" : "Possible") << '\n';
  }
  
  return 0;
}