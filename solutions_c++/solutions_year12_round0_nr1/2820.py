#include <iostream>
#include <string>
using namespace std;

char _d[100] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

void solve() {
  string line;
  getline(cin, line);
  for (int i = 0; i < line.size(); ++i) {
    if (line[i] == ' ') cout << ' ';
    else {
      cout << _d[line[i] - 'a'];
    }
  }
  cout << endl;
}

int main() {
  int ncs;
  cin >> ncs; 
  cin.ignore(100, '\n');
  for (int i = 1; i <= ncs; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}

