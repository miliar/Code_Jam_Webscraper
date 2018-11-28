#include "cctype"
#include "cstdio"
#include "algorithm"
#include "string"
#include "vector"
using namespace std;
typedef long long i64;

vector<int> ParsePattern(const string& s) {
  vector<int> pattern;
  for (int i = 0; i < (int)s.size();)
    if (islower(s[i])) {
      const int x = s[i++] - 'a';
      pattern.push_back(1 << x);
    } else {
      const int end = s.find(')', i + 1);
      int mask = 0;
      for (int j = i + 1; j < end; ++j) {
        const int x = s[j] - 'a';
        mask |= 1 << x;
      }
      pattern.push_back(mask);
      i = end + 1;
    }
  return pattern;
}
bool Match(const vector<int>& pattern, const string& s) {
  bool ok = true;
  for (int i = 0; i < (int)pattern.size() && ok; ++i) {
    const int x = s[i] - 'a';
    ok = (pattern[i] & (1 << x)) != 0;
  }
  return ok;
}
int main() {
  int m, d, n; scanf("%d %d %d", &m, &d, &n);
  vector<string> v;
  for (int i = 0; i < d; ++i) {
    char s[20]; scanf("%s", s);
    v.push_back(string(s));
  }
  sort(v.begin(), v.end());
  for (int i = 0; i < n; ++i) {
    char s[1000]; scanf("%s", s);
    const vector<int> pattern = ParsePattern(s);
    int count = 0;
    for (int j = 0; j < d; ++j)
      if (Match(pattern, v[j])) ++count;
    printf("Case #%d: %d\n", i + 1, count);
  }
  return 0;
}
