#include <iostream>
#include <queue>
#include <cmath>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;
string go(const vector<int> &v, const string &s, int k) {
  string ret = "";
  int at = 0;
  for (int i = 0; i < s.size()/k; ++i, at += k) {
    string q = "";
    for (int j = 0; j < k; ++j)
      q += string(1, s[at+v[j]]);
    ret += q;
  }
  return ret;
}
int calc(const string &s) {
  int ret = 1;
  for (int i = 1; i < s.size(); ++i)
    if (s[i] != s[i-1])
      ++ret;
  return ret;
}
int main() {
  int no_cases;
  cin >> no_cases;
  for (int rr = 1; rr <= no_cases; ++rr) {
    int k, ret = 1000000;
    string s;
    cin >> k >> s;
    vector<int> v = vector<int>(k);
    for (int i = 0; i < k; ++i)
      v[i] = i;
    do {
      ret <?= calc(go(v, s, k));
    } while (next_permutation(v.begin(), v.end()));
    printf("Case #%d: %d\n", rr, ret);
  }
  return 0;
}
