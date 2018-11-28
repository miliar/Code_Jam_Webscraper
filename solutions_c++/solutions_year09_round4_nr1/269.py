#include <algorithm>
#include <string>
#include <vector>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cctype>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <list>
#include <functional>
#include <numeric>
#include <bitset>
#include <ext/hash_set>
#include <ext/hash_map>
#include <stdexcept>
using namespace std;
using namespace __gnu_cxx;

typedef long long ll;
const int infinity = 1000000000;

int main() {
  int cases;
  scanf("%i\n", &cases);
  for (int caseno = 1; caseno <= cases; ++caseno) {
    printf("Case #%i: ", caseno);
    int n;
    scanf("%i", &n);

    vector<int> v;
    char str[100];
    for (int i = 0; i < n; ++i) {
      scanf("%s", str);
      int j;
      for (j = n - 1; j >= 0; --j)
        if (str[j] == '1') break;
      v.push_back(j + 1);
    }

    int ret = 0;
    for (;;) {
      bool change = false;
      for (int i = 0; i < n; ++i)
        if (v[i] > i + 1)
          for (int j = i + 1; j < n; ++j)
            if (v[j] <= i + 1) {
              swap(v[j], v[j - 1]);
              change = true;
              ++ret;
              goto next;
            }
next:;
      if (!change) break;
    }
    printf("%i\n", ret);
        
    fflush(stdout);
  }
  return 0;
}
