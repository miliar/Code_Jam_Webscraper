#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int main () {
  int tests;
  cin >> tests;
  string x;
  int n, p;
  for (int test = 0; test < tests; ++test) {
    cin >> n;
    int r1, r2, s1, s2;
    r1 = r2 = 1;
    s1 = s2 = 0;
    int times = 0;
    for (int i = 0; i < n; ++i) {
      cin >> x >> p;
      if (x.find('O') != string::npos) {
        int t = max(0, abs(r1 - p)-s1) + 1;
        times += t;
        r1 = p;
        s1 = 0; s2 += t;
      } else  {
        int t = max(0, abs(r2 - p)-s2) + 1;
        times += t;
        r2 = p;
        s1 += t; s2 = 0;
      }
    }
    cout << "Case #" << test+1 << ": " << times << endl;
  }
};
