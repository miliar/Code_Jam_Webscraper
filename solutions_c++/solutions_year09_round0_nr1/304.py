#include <iostream>
#include <list>
#include <string>
#include <vector>

using namespace std;

int main() {
  int L, D, N;
  scanf("%d %d %d\n", &L, &D, &N);

  list<string> dict;
  for (int i = 0; i < D; ++i) {
    string s;
    cin >> s;
    dict.push_back(s);
  }
  for (int t = 1; t <= N; ++t) {
    list<string> copy(dict.begin(), dict.end());
    string pattern;
    cin >> pattern;
    for (int i = 0, j = 0; i < L; ++i, ++j) {
      vector<bool> allowed(256, false);
      if (pattern[j] == '(') {
        for (++j; pattern[j] != ')'; ++j) {
          allowed[pattern[j]] = true;
        }
      } else {
        allowed[pattern[j]] = true;
      }
      for (list<string>::iterator it = copy.begin(); it != copy.end(); ) {
        if (!allowed[(*it)[i]]) {
          it = copy.erase(it);
        } else {
          ++it;
        }
      }
    }
    printf("Case #%d: %d\n", t, copy.size());
  }

  return 0;
}
