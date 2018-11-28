#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool checkW(const string &patt, const string &word, const string &tried) {
  if (patt.length() != word.length()) return false;

  for (int i = 0; i < patt.length(); ++i)
    if (tried.find(patt[i]) != tried.find(word[i]))
      return false;

  return true;
  }

bool consistent(char c, int w, const vector<string> &dict, const string &tried) {
  for (vector<string>::const_iterator i = dict.begin(); i != dict.end(); ++i)
    if ((i->find(c) != string::npos) && checkW(dict[w], *i, tried))
      return true;
  return false;
  }

int score(int w, const string &order, const vector<string> &dict) {
  int s = 0;

  string tried;
  for (int i = 0; i < 26; ++i) {
    if (consistent(order[i], w, dict, tried))
      if (dict[w].find(order[i]) == string::npos)
        ++s;
    tried += order[i];
    }

  return s;
  }

int main() {
  int T; cin >> T;
  for (int cNum = 1; cNum <= T; ++cNum) {
    int N, M; cin >> N >> M;

    vector<string> dict(N);
    for (int i = 0; i < N; ++i)
      cin >> dict[i];

    cout << "Case #" << cNum << ":";
    for (int i = 0; i < M; ++i) {
      string order; cin >> order;
      int bestW = 0, bestPts = score(0, order, dict);
      for (int j = 1; j < N; ++j) {
        int t = score(j, order, dict);
        if (t > bestPts) {
          bestW = j; bestPts = t;
          }
        }
      cout << ' ' << dict[bestW];
      }
    cout << '\n';
    }
  }
