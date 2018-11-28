#include <iostream>
#include <string>
#include <memory.h>

using namespace std;

int l, d, n;
string ss[5000];
bool pat[20][1024];

int main() {
  cin >> l >> d >> n;
  for (int i = 0; i < d; i++) cin >> ss[i];
  for (int i = 0; i < n; i++) {
    string s; cin >> s;
    memset(pat, 0, sizeof pat);
    for (int j = 0, pos = 0; pos < l; ) {
      while (pos < l && s[j] != '(')
        pat[pos++][s[j++] + 256] = true;
      j++;
      if (pos == l) break;
      while (s[j] != ')')
        pat[pos][s[j++] + 256] = true;
      pos++; j++;
    }

    int res = 0;
    for (int j = 0; j < d; j++) {
      bool ok = true;
      for (int pos = 0; pos < l && ok; pos++)
        ok = pat[pos][ss[j][pos] + 256];
      if (ok) res++;
    }

    cout << "Case #" << (i + 1) << ": " << res << endl;
  }
  return 0;
}

