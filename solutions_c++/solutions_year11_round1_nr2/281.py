#include <iostream>
#include <string>
#include <vector>

using namespace std;

void remove(vector<int>& prev, vector<int>& next, int ind) {
  int p = prev[ind], n = next[ind];
  prev[n] = p;
  next[p] = n;
  prev[ind] = ind;
}

int score(const vector<string>& dict, string list, string word, vector<int>& prev, vector<int>& next) {
  for (int i = 0; i < int(dict.size()+2); ++i) {
    prev[i] = i-1;
    next[i] = i+1;
  }
  int score = 0;
  string known(word.size(), '_');
  for (int i = next[0]; i < int(next.size())-1; i = next[i]) {
    if (dict[i-1].size() != word.size()) remove(prev, next, i);
  }
  for (int i = 0; i < int(list.size()); ++i) {
    bool consistent = false;
    for (int j = next[0]; j < int(next.size())-1 && !consistent; j = next[j]) {
      for (int k = 0; k < int(word.size()); ++k) {
        if (known[k] == '_' && dict[j-1][k] == list[i]) consistent = true;
      }
    }
    if (consistent) {
      bool appears = false;
      for (int j = 0; j < int(word.size()); ++j) {
        if (word[j] == list[i]) {
          known[j] = list[i];
          appears = true;
        }
      }
      if (!appears) ++score;
      for (int j = next[0]; j < int(next.size())-1; j = next[j]) {
        for (int k = 0; k < int(known.size()); ++k) {
          if ((known[k] != '_' && dict[j-1][k] != known[k]) || (known[k] == '_' && dict[j-1][k] == list[i])) {
            remove(prev, next, j);
            break;
          }
        }
      }
    }
  }
  return score;
}

int main() {
  int T;
  cin >> T;
  for (int ca = 1; T--; ++ca) {
    int n, m;
    cin >> n >> m;
    vector<string> dict(n);
    for (int i = 0; i < n; ++i) {
      cin >> dict[i];
    }
    vector<string> list(m);
    for (int i = 0; i < m; ++i) {
      cin >> list[i]; // permutation of "abcdefghijklmnopqrstuvwxyz"
    }
    vector<int> prev(dict.size()+2), next(dict.size()+2);
    cout << "Case #" << ca << ":";
    for (int il = 0; il < m; ++il) {
      string best = "";
      int bscore = -1;
      for (int id = 0; id < n; ++id) {
        int cscore = score(dict, list[il], dict[id], prev, next);
        if (cscore > bscore) {
          best = dict[id];
          bscore = cscore;
        }
      }
      cout << " " << best;
    }
    cout << endl;
  }
}
