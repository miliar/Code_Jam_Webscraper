#include <iostream>
#include <string>
using namespace std;

int main() {
  char deco[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
  int T, cas;
  cin >> T;
  cas = 1;
  string s;
  getline(cin, s);
  while (cas <= T) {
    getline(cin, s);
    for (int i = 0; i < s.size(); ++i) if (s[i] != ' ') s[i] = deco[s[i] - 'a'];
    cout << "Case #" << cas << ": " << s << endl;
    ++cas;
  }
}