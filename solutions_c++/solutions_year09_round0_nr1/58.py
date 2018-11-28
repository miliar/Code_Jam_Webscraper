#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <assert.h>
using namespace std;
inline vector< int > foo(string s) {
  vector< int > ret;
  int tmp;
  int at = 0;
  while (at < s.size()) {
    tmp = 0;
    if (s[at] == '(') {
      ++at;
      while (s[at] != ')')
	tmp |= 1<<(s[at++]-'a');
      ++at;
    } else
      tmp |= 1<<(s[at++]-'a');
    ret.push_back(tmp);
  }
  return ret;
}
int main() {
  int L, D, N;
  cin >> L >> D >> N;
  vector<string> v;
  for (int i = 0; i < D; ++i) {
    string s;
    cin >> s;
    v.push_back(s);
  }
  for (int rr = 1; rr <= N; ++rr) {
    string s;
    cin >> s;
    vector< int > w = foo(s);
    int ans = 0;
    for (int i = 0; i < D; ++i)
      for (int j = 0; j < L; ++j)
	if ((w[j] & (1<<(v[i][j]-'a'))) == 0)
	  break;
	else if (j+1 == L)
	  ++ans;
    printf("Case #%d: %d\n", rr, ans);
  }
  return 0;
}
