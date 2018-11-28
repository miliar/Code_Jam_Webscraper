#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int main() {
  int T;
  scanf("%d\n", &T);
  for (int t = 1; t <= T; ++t) {
    printf("Case #%d: ", t);

    int c, d, n;
    vector<pair<pair<char, char>, char> > cs;
    vector<pair<char, char> > ds;
    cs.clear();
    ds.clear();
    scanf("%d", &c);
    for (int i = 0; i < c; ++i) {
      char c1, c2, res;
      scanf(" %c%c%c", &c1, &c2, &res);
      cs.push_back(make_pair(make_pair(c1, c2), res));
    }
    scanf("%d", &d);
    for (int i = 0; i < d; ++i) {
      char c1, c2, res;
      scanf(" %c%c", &c1, &c2);
      ds.push_back(make_pair(c1, c2));
    }
    scanf("%d ", &n);
    string s = "";
    for (int i = 0; i < n; ++i) {
      char C;
      scanf("%c", &C);
      s += C;
      if (s.size() == 1) {
        continue;
      }
      for (unsigned int j = 0; j < cs.size(); ++j) {
        if ((cs[j].first.first == s[s.size() - 1] &&
             cs[j].first.second == s[s.size() - 2]) ||
            (cs[j].first.first == s[s.size() - 2] &&
             cs[j].first.second == s[s.size() - 1])) {
          s.replace(s.size() - 2, 2, &cs[j].second, 1);
          j = 0;
        }
      }
      for (unsigned int j = 0; j < ds.size(); ++j) {
        if (s.find(ds[j].first) != string::npos && 
            s.find(ds[j].second) != string::npos) {
          s.clear();
        }
      }
    }
    if (s.size() == 0) {
      printf("[]\n");
    } else {
      printf("[");
      for (int i = 0; i < s.size() - 1; ++i) {
        printf("%c, ", s[i]);
      }
      printf("%c]\n", s[s.size() - 1]);
    }
  }
  return 0;
}
