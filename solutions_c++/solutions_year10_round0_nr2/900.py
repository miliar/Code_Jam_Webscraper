#include <iostream>
using namespace std;
#include <cmath>

int pgcd(int a, int b) {
  if(a == 0)
    return b;
  else if(b == 0)
    return a;
  else if(a % b == 0)
    return b;
  else if(b % a == 0)
    return a;
  else if(a > b)
    return pgcd(a % b, b);
  else
    return pgcd(b % a, a);
}

int main() {
  int C, N, a, b, c, d, y;
  cin >> C;
  for(int i = 1 ; i <= C ; i++) {
    cin >> N;
    if(N == 2) {
      cin >> a;
      cin >> b;
      d = abs(a - b);
      y = (d == 1 || (a % d) == 0) ? 0 : d - (a % d);
    } else {
      cin >> a;
      cin >> b;
      cin >> c;
      d = pgcd(abs(b - a), abs(c - a));
      y = (d == 1 || (a % d) == 0) ? 0 : d - (a % d);
    }
    cout << "Case #" << i << ": " << y << endl;
  }
  return 0;
}
