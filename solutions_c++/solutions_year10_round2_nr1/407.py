#include <algorithm>
#include <string>
#include <vector>
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

vector<string> parse(string s) {
  vector<string> v;
  s += "/";
  for (;;) {
    s = s.substr(1);
    if (s.empty()) break;

    int pos = s.find('/');
    v.push_back(s.substr(0, pos));
    s = s.substr(pos);
  }
  return v;
}

int numvert(const vector<string>& v) {
  int n = v.size();
  set<string> m;

  for (int i = 0; i < n; ++i) {
    vector<string> w = parse(v[i]);

    string t = "/";
    for (int i = 0; i < w.size(); ++i) {
      t = t + w[i] + "/";
      m.insert(t);
    }
  }
  return m.size();
}

int main() {
  int cases;
  scanf("%i", &cases);
  for (int numcase = 1; numcase <= cases; ++numcase) {
    int n, m;
    scanf("%i%i\n", &n, &m);
    string s;
    
    vector<string> a;
    for (int i = 0; i < n; ++i) {
      cin >> s;
      a.push_back(s);
    }
    vector<string> b(a);
    for (int i = 0; i < m; ++i) {
      cin >> s;
      if (find(a.begin(), a.end(), s) == a.end())
        b.push_back(s);
    }

    int r = numvert(b) - numvert(a);
    printf("Case #%i: %i\n", numcase, r);
  }
  return 0;
}
