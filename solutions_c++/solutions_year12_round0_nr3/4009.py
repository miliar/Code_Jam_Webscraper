#include <iostream>
#include <cstdio>
#include <map>
using namespace std;

int count(int x, int b){
  int cnt = 0;
  int d = 10, d1 = 10;
  while (x / d1 > 0) d1 *= 10;
  d1 /=10;

  map<int, bool> used;
  while (x / d > 0) {
    int nb = x / d + d1 * (x % d);
    if (nb <= b && nb > x){
      if (!used[nb]){
	used[nb] = true;
	cnt++;
      }
    }

    d*= 10; d1/=10;
  }

  return cnt;
}

int main() {
  int t, a, b;
  cin >> t;
  for (int tt = 1; tt <= t; tt++){
    cin >> a >> b;
    int res = 0;
    for (int x = a; x <= b; x++)
      res += count(x, b);
    cout << "Case #" << tt << ": " << res << endl;
  }
  return 0;
}
