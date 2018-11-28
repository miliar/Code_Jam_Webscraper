#include <iostream>
#include "gmpxx.h"

using namespace std;

int main()
{
  // I'm sure there's a more elegant way to do this, but we're in a time crunch. Fix when we have more time to research it.

  mpf_class base(3.0, 1000000);
  mpf_class product(5.0, 1000000);
  base += sqrt(product);

  int cases;
  cin >> cases;

  for (int j = 0; j < cases; ++j)
  {
    int n;
    cin >> n;
    product = 1.0;

    for (int i = 0; i < n; ++i)
    {
      product *= base;
    }

    mpf_class result;
    result = floor(product);
    result -= floor(result / 1000.0) * 1000.0;

    cout << "Case #" << j + 1 << ": ";
    cout.width(3);
    cout.fill('0');
    cout << result << endl;
  }

  return 0;
}
