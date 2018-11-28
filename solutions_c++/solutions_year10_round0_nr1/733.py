#include <iostream>

using namespace std;

int main() {
  int t;
  cin >> t;
  for(int tcase=1;tcase<=t;tcase++){
    int n, k;
    cin >> n >> k;
    cout << "Case #" << tcase << ": ";
    if( (k & ((1 << n) - 1)) == ((1 << n) - 1))
      cout << "ON\n";
    else
      cout << "OFF\n";
  }
}
