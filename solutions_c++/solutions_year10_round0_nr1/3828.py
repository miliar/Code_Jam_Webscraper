#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
//#include <cstdlib>

using namespace std;

int main() {
  unsigned int ncases;
  unsigned int n;
  unsigned long k, x, d;
  cin >> ncases;
  for(int i=1;i<=ncases;i++) {
    cout << "Case #" << i << ": ";
    cin >> n >> k;
    x = pow(2, n);

    if (k%2 == 1) {
      if (k<=x) {
        cout << ( (x-1) == k ? "ON" : "OFF" );
      } else {
        d = (k+1)/x;
        cout << ( (k-(d-1)*x) == (x-1) ? "ON" : "OFF");
      }
    } else
        cout << "OFF";
    cout << endl;
  }
}
