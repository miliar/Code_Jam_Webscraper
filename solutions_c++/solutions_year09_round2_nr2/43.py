#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    string N;
    cin >> N;
    vector<int> digs;
    for (int j = N.length() - 1; j >= 0; j--) {
      digs.push_back(N[j] - '0');
    }
    digs.push_back(0);
    digs.push_back(0);
    reverse(digs.begin(), digs.end());
    next_permutation(digs.begin(), digs.end());
    
    cout << "Case #" << i+1 << ": ";
    bool printed = false;
    for (int j = 0; j < digs.size(); j++) {
      if (digs[j] != 0) printed = true;
      if (printed) cout << digs[j];
    }
    if (!printed) cout << 0 << endl;
    cout << endl;
  }
  return 0;
}
