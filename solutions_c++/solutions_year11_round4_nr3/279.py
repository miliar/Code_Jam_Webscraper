#include <boost/foreach.hpp>
#include <cmath>
#include <iostream>
#include <vector>

#define foreach BOOST_FOREACH

typedef long long Integer;
typedef std::vector<Integer> IntegerVector;


IntegerVector getPrimes()
{
  IntegerVector result;

  std::vector<bool> bitmap(1024 * 1024, true);
  
  bitmap[0] = false;
  bitmap[1] = false;
  
  for (size_t i = 0; i < bitmap.size(); ++i) {
    if (bitmap[i]) {
      result.push_back(i);
      for (size_t j = i; j < bitmap.size(); j += i) {
        bitmap[j] = false;
      }
    }
  }
  
  return result;
}

const IntegerVector kPrimes = getPrimes();

Integer Log(Integer base, Integer number)
{
  Integer result = 0;
  while (number >= base) {
    number /= base;
    ++result;
  }
  return result;
}

Integer Solve(const Integer n)
{
  if (n == 1) {
    return 0;
  }
  
  Integer fast = 0;
  Integer slow = 1;
    
  foreach (Integer prime, kPrimes) {
    const Integer log_prime = Log(prime, n);
    if (log_prime > 0) {
      fast += 1;
      slow += log_prime;
    }
  }

  return slow - fast;  
}


int main()
{
  size_t number_of_cases;
  std::cin >> number_of_cases;
  
  for (size_t case_number = 1; case_number <= number_of_cases; ++case_number) {
    Integer n;
    std::cin >> n;
    
    std::cout << "Case #" << case_number << ": " << Solve(n) << '\n';
  }
  
  return 0;
}
