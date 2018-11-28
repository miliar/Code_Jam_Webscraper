#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int main()
{
  int cas;
  int T;
  cin >> T;

  for (cas = 1; cas <= T; cas++) {
    string s;
    cin >> s;
    if (next_permutation(s.begin(), s.end())) {
    } else {
      sort(s.begin(), s.end());
      s = "0" + s;
      for (int i = 0; ; i++) {
        if (s[i] != '0') {
          s[0] = s[i];
          s[i] = '0';
          break;
        }
      }
    }
    cout << "Case #" << cas << ": " << s << endl;
  }

  return 0;
}

