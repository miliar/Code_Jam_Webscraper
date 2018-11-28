
#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

#include <boost/lexical_cast.hpp>


using namespace std;


int const gcd(int x, int y) {
  if (x < y) {
    return gcd(y, x);
  }
  if (y <= 0) {
    return x;
  }
  return gcd(y, x%y);
}




int main() {
  int C;
  cin >> C;

  for (int i = 0; i < C; ++i) {
    int N;
    cin >> N;
    vector<int> t(N);
    for (int j = 0; j < N; ++j) {
      cin >> t[j];
    }
    sort(t.begin(), t.end());

    vector<int> dif(N-1);
    for (int j = 0; j < N-1; ++j) {
      dif[j] = t[j+1] - t[j];
    }


    cout << "Case #" << i+1 << ": ";

    int g;
    if (N == 2) {
      g = dif[0];
    } else {
      g = gcd(dif[0], dif[1]);
      for (int j = 2; j < N-1; ++j) {
	g = gcd(g, dif[j]);
      }
    }

    int n = t[0] / g;
    int T;
    if (t[0] - g*n > 0) {
      T = g*(n+1) - t[0];
    } else {
      T = g*n - t[0];
    }

    cout << T << "\n";

  }

  return 0;
}
