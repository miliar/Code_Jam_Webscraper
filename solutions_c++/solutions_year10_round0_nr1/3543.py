#include <iostream>
#include <string>
using namespace std;

int main() {

  int t = 0;
  cin >> t;
  for (int i = 0 ; i < t; i++) {
    int n, k;
    cin >> n >> k;
    bool on = ((k % (1<<n)) == (1<<n)-1);
    cout << "Case #" << (i+1) << ": " << (on ? "ON" : "OFF") << endl;
  }
}
