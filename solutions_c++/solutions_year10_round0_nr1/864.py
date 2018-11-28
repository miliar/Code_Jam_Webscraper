#include <iostream>

using namespace std;

int main() {
  int t; cin >> t;
  for (int caseNo = 1; caseNo <= t; caseNo++) {
    int n, k; cin >> n >> k;
    int m = (1 << n) - 1;
    cout << "Case #" << caseNo << ": " << ((k & m) == m ? "ON" : "OFF") << endl;
  }
  return 0;
}

