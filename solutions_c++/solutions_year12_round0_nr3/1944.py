#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <numeric>
#include <utility>

using namespace std;

string itos(int i) {
  ostringstream oss; oss << i; return oss.str();
}

int main(void) {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    int A, B; cin >> A >> B;
    int ans = 0;
    string B_str = itos(B);
    for (int n = A; n < B; n++) {
      string n_str = itos(n);
      set <string> answers;
      for (int i = 1; i < (int) n_str.length(); i++) {
	string m_str = n_str.substr(i) + n_str.substr(0, i);
	if (n_str < m_str && m_str <= B_str)
	  answers.insert(m_str);
      }
      ans += answers.size();
    }
    printf("Case #%d: %d\n", t, ans);
  }
}
