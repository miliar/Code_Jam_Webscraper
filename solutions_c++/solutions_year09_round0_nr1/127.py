#include<iostream>
#include<string>
#include<vector>

using namespace std;

int N, L, D;
vector<string> dict;


inline bool match(const string &w, const string &p) {
  int j = 0;
  for (int i = 0; i < w.size(); ++i,++j) {
    if (p[j] != '(') {
      if (w[i] != p[j]) return false;
    } else {
      bool g = false;
      while (p[j] != ')') {
        j++;
        if (w[i] == p[j]) g = true;
      }
      if (!g) return false;
    }
  }
  return true;
}

int main() {
  cin >> L >> D >> N;

  for (int i = 0; i < D; ++i) {
    string s;
    cin >> s;
    dict.push_back(s);
  }
  for (int i = 0; i < N; ++i) {
    string p;
    cin >> p;
    int ret = 0;
    for (int j = 0; j < dict.size(); ++j) {
      if (match(dict[j], p)) ret++;
    }
    cout << "Case #" << i+1 << ": " << ret << endl;
  }
  return 0;
}
