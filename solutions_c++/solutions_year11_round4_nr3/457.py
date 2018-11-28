#include <inttypes.h>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>

typedef long long ll;

using namespace std;

namespace {
vector<size_t> primes;
size_t IsConcate(size_t num) {
  size_t concate = 0;
  for (size_t i = 0; i < primes.size(); ++i) {
    if (num % primes[i] == 0) {
      ++concate;
      while (num % primes[i] == 0)
        num /= primes[i];
    }
  }

  if (concate == 0)
    primes.push_back(num);

  return concate;
}

void PrintOutput(size_t iter, const size_t result) {
  printf("Case #%d: %d\n", iter+1, result);
}
} //namespace

int main() {
  size_t T;
  cin >> T;

  for (size_t iter = 0; iter < T; ++iter) {
    size_t n;
    cin >> n;
    
    if (n == 1) {
      PrintOutput(iter, 0);
      continue;
    }
    
    primes = vector<size_t>(0);

    size_t max = n;
    size_t prime = 0;
    for (size_t i = 2; i <= n; ++i) {
      size_t res = IsConcate(i);
      if (res >= 2)
        --max;
      else if (res == 0)
        ++prime;
    }

    size_t result = max - prime;
    PrintOutput(iter, result);
  }
  return 0; 
}
