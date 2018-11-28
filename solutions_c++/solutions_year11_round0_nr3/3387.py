#include <iostream>

using namespace std;

int main() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; t++) {
    int n;
    cin >> n;
    int k;
    int min = 99999999;

    int total = 0;
    int x = 0;
    for (int i = 0; i<n; i++) {
      cin >> k;
      x ^= k;
      total+=k;
      if (k<min)
	min = k;
    }
    
    cout << "Case #" << t << ": ";
    if (x)
      cout << "NO" << endl;
    else
      cout << total-min << endl;
  }
  return 0;
}
