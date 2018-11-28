#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
using namespace std;


vector<string> S;
string L;

bool eq(string &s, string &t, char &c) {
  for(int i = 0; i < s.size(); ++i) {
    if(s[i] == '_') {
      if(t[i] == c) return false;
      continue;
    }
    if(s[i] != t[i]) return false;
  }
  return true;
}

pair<int, string> solve(vector<int> v, int p) {
  int lossP = 0;
  string s(S[p].size(), '_');
  for(int i = 0; v.size() > 1 && i < L.size(); ++i) {
    bool flag = false;
    for(int j = 0; j < v.size(); ++j) {
      if(S[v[j]].find(L[i]) != string::npos) break;
      if(j+1 == v.size()) flag = true;
    }
    if(flag) continue;
    if(S[p].find(L[i]) == string::npos) {
      ++lossP;
    } else {
      for(int j = 0; j < S[p].size(); ++j) {
	if(S[p][j] == L[i]) s[j] = S[p][j];
      }
    }
    for(vector<int>::iterator it = v.begin(); it != v.end(); ) {
      if(!eq(s, S[*it], L[i])) {
	it = v.erase(it);
      } else {
	++it;
      }
    }
  }
  return make_pair(lossP, S[p]);
}

int main() {
  int T;
  cin >> T;
  for(int tc = 0; tc < T; ++tc) {
    int N, M;
    cin >> N >> M;
    S.clear();
    for(int i = 0; i < N; ++i) {
      string s;
      cin >> s;
      S.push_back(s);
    }
    //    sort(S.begin(), S.end());
    cout << "Case #" << tc+1 << ":";
    for(int i = 0; i < M; ++i) {
      cin >> L;

      pair<int, string> ans = make_pair(-1, "");
      for(int l = 1; l <= 10; ++l) {
	vector<int> v;
	for(int i = 0; i < S.size(); ++i)
	  if(S[i].size() == l) v.push_back(i);
	if(v.size() == 0) continue;
	for(int i = 0; i < v.size(); ++i) {
	  pair<int, string> tmp = solve(v, v[i]);
	  if(tmp.first > ans.first) {
	    ans = tmp;
	  }
	}
      }

      cout << " " << ans.second;
    }
    cout << endl;
  }
  return 0;
}
