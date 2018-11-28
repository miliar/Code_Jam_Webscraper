#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cassert>
#include <queue>
#include <cctype>
using namespace std;

typedef long double Real;

const Real o = 1e-8;
const Real pi = acos(-1.0);

char trans[26];

void build_trans(const string &a, const string &b) {
  assert(a.length() == b.length());
  for (size_t i = 0; i < a.length(); ++i) {
    if (islower(a[i])) {
      assert(islower(b[i]));
      trans[a[i] - 'a'] = b[i];
    } else {
      assert(!islower(b[i]));
    }
  }
}

int main() {
  memset(trans, 0, sizeof trans);
  build_trans("ejp mysljylc kd kxveddknmc re jsicpdrysi",
              "our language is impossible to understand");
  build_trans("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
              "there are twenty six factorial possibilities");
  build_trans("de kr kd eoya kw aej tysr re ujdr lkgc jv",
              "so it is okay if you want to just give up");
  build_trans("qz", "zq");

#if 0
  for (int i = 0; i < 26; ++i) {
    if (trans[i] == '\0')
      printf("unknown\n");
    else
      printf("%c\n", trans[i]);
  }
#endif

  int T;
  string line;
  cin >> T; getline(cin, line);
  for (int I = 0; I < T; ++I) {
    getline(cin, line);
    cout << "Case #" << (I + 1) << ": ";
    for (size_t i = 0; i < line.length(); ++i) {
      if (islower(line[i]))
        cout << trans[line[i] - 'a'];
      else
        cout << line[i];
    }
    cout << "\n";
  }

	return 0;
}

