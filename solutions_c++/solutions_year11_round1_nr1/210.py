#include <string>
#include <iostream>
using namespace std;
int gcd(int a, int b) {
  return b ? gcd(b, a%b) : a;
}
string solve() {
  int D, G;
  long long int N;
  cin >> N >> D >> G;
  if (!D) {
    if (G == 100) {
      return "Broken";
    }
    return "Possible";
  }
  if (!G) {
    return "Broken";
  }
  if (G == 100 && D < 100) {
    return "Broken";
  }

  int mult = gcd(D, 100);
  mult = 100 / mult;

  if (mult > N) return "Broken";
  return "Possible";
}
int main() {
  int cases;
  cin >> cases;
  for (int i = 1; i <= cases; i++) {
    cout << "Case #" << i << ": " << solve() << endl;
  }
  return 0;
}

