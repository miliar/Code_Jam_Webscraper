#include <iostream>
#include <cassert>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main() {
  int n;
  freopen("data.txt", "r", stdin);
  cin >> n;
  int m, x;
  
  char c;
  for (int i = 0; i < n; i++) {
    
    cin >> m;
    vector<int> O, B;
    string s;
    for (int j = 0; j < m; j++) {
      
      cin >> c >> x;
      s += c;
      if (c == 'O') {
        O.push_back(x);
      } else {
        B.push_back(x);
      }
    }
    int tO = 0, tB = 0, p = 0, q = 0, lO = 1, lB = 1, t = 0;
    for (int j = 0; j < s.length(); j++) {
      if (s[j] == 'O') {
        assert(p < O.size());
        tO += abs(O[p] - lO);
        lO = O[p];
        t = max(tO, tB) + 1;
        tO = t;
        p++;
      } else {
        assert(q < B.size());
        tB += abs(B[q] - lB);
        lB = B[q];
        t = max(tO, tB) + 1;
        tB = t;
        q++;
      }
    }
    cout << "Case #" << i+1 << ": " << t << endl;
  }
  
}