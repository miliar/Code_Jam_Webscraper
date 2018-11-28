#include <iostream>
#include <cmath>
using namespace std;

bool is_sqr(string& s) {
  long long v = 0;
  for (int i = 0; i < s.size(); i++)
    v = 2*v+(s[i]-'0');
  // cout << "\t" << v << endl;
  long long sqrtv = (long long)sqrt(v);
  return sqrtv*sqrtv == v;
}

bool go(string& s, int idx) {
  int nxt = s.find('?', idx);
  if (nxt == string::npos) {
    return is_sqr(s);
  }

  s[nxt] = '0';
  if (go(s, nxt+1)) return true;
  s[nxt] = '1';
  if (go(s, nxt+1)) return true;
  s[nxt] = '?';
  return false;
}

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    string s; cin >> s; go(s, 0);
    cout << "Case #" << c << ": " << s << endl;
  }
  return 0;
}
