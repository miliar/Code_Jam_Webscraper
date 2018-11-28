#include <iostream>
#include <string>
#include <hash_map>
#include <hash_set>
using namespace std;

vector<char> process(string s, const hash_map<string, char> &comb, const hash_set<string> &opp) {
  vector<char> list;
  list.push_back(s[0]);
  int n = s.length();
  for (int i = 1; i < n; i++) {
    if (list.empty()) { list.push_back(s[i]); continue; }
    string pair; pair += s[i]; pair += list.back();
    hash_map<string, char>::const_iterator iter = comb.find(pair);
    if (iter != comb.end()) {
      char replace = iter->second;
      list.pop_back();
      list.push_back(replace);
    } else {
      string p; p += s[i];
      int m = list.size();
      bool found = false;
      for (int j = 0; j < m; j++) {
        hash_set<string>::const_iterator iter = opp.find(p + list[j]);
        if (iter != opp.end()) {
          list.clear();
          found = true;
          break;
        }
      }
      if (!found)
        list.push_back(s[i]);
    }
  }
  return list;
}

int main() {
  freopen("data.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  int n, C, D;
  string s;
  cin >> n;
  for (int i = 0; i < n; i++) {
    hash_map<string, char> comb;
    cin >> C;
    for (int j = 0; j < C; j++) {
      cin >> s;
      string ss; ss += s[0]; ss += s[1];
      comb.insert(pair<string, char>(ss, s[2]));
      ss = ""; ss += s[1]; ss += s[0];
      comb.insert(pair<string, char>(ss, s[2]));
    }
    cin >> D;
    hash_set<string> opp;
    for (int j = 0; j < D; j++) {
      cin >> s;
      opp.insert(s);
      string ss; ss += s[1]; ss += s[0];
      opp.insert(ss);
    }
    int t;
    cin >> t >> s;
    vector<char> ans = process(s, comb, opp);
    cout << "Case #" << i+1 << ": [";
    int k = ans.size();
    for (int j = 0; j < k; j++) {
      cout << ans[j];
      if (j != k-1) cout << ", ";
    }
    cout << "]" << endl;
  }
}