#include <string>
#include <vector>
#include <iostream>
using namespace std;
int x2m1(int x, int r) {
  while (r--) x = x * 2 + 1;
  return x;
}
int solver() {
  int p, misses[2048], prices[2048], view[2048], price = 0;
  cin >> p;
  for (int x = 0; x < (1<<p); x++) {
    cin >> misses[x]; view[x] = 0;
  } p--;

  for (int z = p, r = 1; z > -1; z--, r++) {
    for (int x = 0; x < (1<<z); x++) {
      cin >> prices[x];
      int buy = 0;
      for (int y = (x << r); y <= x2m1(x, r); y++) {
        if (misses[y] == 0) { buy = 1; break; }
      }
      if (buy) {
        price += prices[x];
        // for (int y = (x << r); y <= x2m1(x, r); y++) if (misses[y] >= z + 1) misses[y]++;
      } else {
        for (int y = (x << r); y <= x2m1(x, r); y++) misses[y]--;
      }
    }
  }
  return price;
}
int main() {
  int c;
  cin >> c;
  for (int x = 1; x <= c; x++) cout << "Case #" << x << ": " << solver() << endl;
  return 0;
}

