#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main() {
  int L, D, N;
  cin >> L >> D >> N;
  vector<string> words(D);
  for (int i = 0; i < D; i++)
    cin >> words[i];

  for (int c = 1; c <= N; c++) {
    string pattern;
    cin >> pattern;

    vector<set<char> > p(L);
    int ind = 0;
    for (int i = 0; i < L; i++) {
      if (pattern[ind] != '(')
        p[i].insert(pattern[ind]);
      else {
        while (pattern[++ind] != ')')
          p[i].insert(pattern[ind]);
      }
      ind++;
    }

    int res = 0;
    for (int i = 0; i < D; i++) {
      bool match = true;
      for (int j = 0; j < L && match; j++)
        match = match && (p[j].find(words[i][j]) != p[j].end());
      res += match;
    }

    cout << "Case #" << c << ": " << res << endl;
  }

  return 0;
}
