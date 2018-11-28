#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int T, L, P, C, r;
  cin >> T;
  for(int i = 1 ; i <= T ; i++) {
    cin >> L;
    cin >> P;
    cin >> C;
    r = ceil(log((log((double) P / L)) / log(C)) / log(2));
    if(r <= 0)
      cout << "Case #" << i << ": 0" << endl;
    else
      cout << "Case #" << i << ": " << r << endl;
  }
  return 0;
}
