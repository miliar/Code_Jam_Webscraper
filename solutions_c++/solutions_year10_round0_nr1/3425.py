#include <iostream>
#include <vector>

using namespace std;

typedef unsigned long long ull;
int main(void) {
  int t, n;
  ull k;
  
  cin >> t;
  for (int i=0; i<t; i++) {
    cin >> n >> k;
    ull s = 1;
    for (int j=0; j<n; j++) {
      s = s*2;
    }
    k = k % s;
    cout << "Case #" << (i+1) << ": ";
    if (k == s-1) {
      cout << "ON";
    } else {
      cout << "OFF";
    }
    cout << endl;
  }
  return 0;
}