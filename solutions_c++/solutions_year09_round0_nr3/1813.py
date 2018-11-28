#include <iostream>
#include <string>
#include <memory.h>
#include <cstdio>

using namespace std;

const string str = "welcome to code jam";

int ans[500][50];

int main() {
  int n; cin >> n;
  string _s; getline(cin, _s);

  for (int _t = 0; _t < n; _t++) {
    getline(cin, _s);
    string s = "$"; s += _s;
    memset(ans, 0, sizeof ans);
    for (int i = 1; i < s.size(); i++) {
      if (s[i] == str[0]) ans[i][0] = (ans[i][0] + 1) % 10000;
      for (int j = 1; j < str.size(); j++)
        if (s[i] == str[j])
          for (int k = 0; k < i; k++)
            ans[i][j] = (ans[i][j] + ans[k][j - 1]) % 10000;
    }

    int res = 0;
    for (int i = 0; i < s.size(); i++)
      res = (res + ans[i][str.size() - 1]) % 1000;
    cout << "Case #" << (_t + 1) << ": ";
    printf("%04d", res);
    cout << endl;
  }

  return 0;
}
