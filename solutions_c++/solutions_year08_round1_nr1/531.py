#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long lint;

int main(void)
{
  int T;
  cin >> T;
  for( int k = 0 ; k < T ; ) {
    cout << "Case #" << (++k) << ": ";
    int n;
    cin >> n;
    vector<lint> x, y;
    int neg, pos;
    lint j;
    for( int i = 0 ; i < n ; ++i ) {
      cin >> j;
      x.push_back(j);
    }
    for( int i = 0 ; i < n ; ++i ) {
      cin >> j;
      y.push_back(j);
    }

    sort(x.begin(), x.end());
    sort(y.begin(), y.end());
    lint prod = 0;
    for( int i = 0 ; i < n ; ++i ) {
      prod += x[i] * y[n - i - 1];
      //cerr << x[i] << "*" << y[n - i - 1] << "=" << x[i] * y[n - i - 1] << "\n";
    }

    cout << prod << "\n";
  }
}
