#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> comb, opp;

bool combines (string & s, char c) {
  if (s.empty())
    return false;
  char o = s[s.size()-1];
  for (int i = 0; i < comb.size(); ++i)
    if (comb[i].substr(0,2).find(o) != string::npos &&
        comb[i].substr(0,2).find(c) != string::npos &&
        (comb[i].find(o) != comb[i].find(c) ||
        comb[i][0] == comb[i][1])) {
      s.resize(s.size()-1);
      s.push_back(comb[i][2]);
      return true;
    } 
  return false;
}

bool opposes (string & s, char c) {
  if (s.empty())
    return false;
  for (int i = 0; i < opp.size(); ++i) {
    char o = 0;
    if (opp[i][0] == c)
      o = opp[i][1];
    else if (opp[i][1] == c)
      o = opp[i][0];
    if (o != 0) {
      if (s.find(o) != string::npos) {
        s.clear();
        return true;
      }
    }
  }
  return false;
}

int main () {
  int c;
  string s;
  int tests; cin >> tests;
  for (int test = 0; test < tests; ++test) {
    s.clear();
    cin >> c;
    comb.resize(c);
    for (int i = 0; i < c; ++i)
      cin >> comb[i];
    cin >> c;
    opp.resize(c);
    for (int i = 0; i < c; ++i)
      cin >> opp[i];

    int k;
    cin >> k;
    cin >> s;
    
    string res;
    for (int i = 0; i < s.size(); ++i) {
      if (combines(res, s[i])) {
      } else if (opposes(res, s[i])) {
      } else {
        res.push_back(s[i]);
      }
    }

    cout << "Case #" << test+1 << ": " << "[";
    for (int i = 0; i < res.size(); ++i) {
      cout << res[i];
      if (i + 1 < res.size())
        cout << ", ";
    }
    cout << "]" << endl;
  }
  return 0;
};
