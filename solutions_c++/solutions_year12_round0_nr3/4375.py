#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
using namespace std;

void testcase() {
  int a, b;
  cin >> a >> b;
  int result = 0;
  for (int i = max(a,10); i < b; ++i)
    for (int j = i+1; j <= b; ++j) {
      stringstream ss;
      ss << i << " " << j;
      string a, b;
      ss >> a >> b;
      if (a.size() != b.size()) continue;
      bool ok = false;
      for (int pocz = 0; pocz < a.size(); ++pocz) {
	rotate(a.begin(), a.begin()+1, a.end());
	if (a == b) { ok = true; break; }
      }
      if (ok) {
	++result;
      }
    }
    cout << result;
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    testcase();
    cout << endl;
  }
}
