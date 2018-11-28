#include <iostream>
#include <vector>
#include <sstream>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

typedef unsigned int uint;
typedef map<pair<int, char>, vector<string> > dir_t;

int solve_it(dir_t &dir, string &s) {
  int pos = 0;
  map<string, int> res;
  for (uint i=0; i<s.size(); i++) {
    if (s[i] == '(') { 
      while (s[i] != ')') {
        vector<string> &wl = dir[make_pair(pos, s[++i])];
        for (uint j=0; j<wl.size(); j++) res[wl[j]] += 1;
      }
    }
    else {
      vector<string> &wl = dir[make_pair(pos, s[i])];
      for (uint j=0; j<wl.size(); j++) res[wl[j]] += 1;
    }
    pos++;
  }
  uint cnt = 0;
  for (map<string, int>::iterator it=res.begin(); it != res.end(); it++) if (it->second == pos) cnt++; 
  return cnt;
}

int main() {
  int L, D, N;
  cin >> L >> D >> N;
  dir_t dir;
  for (int i=0; i<D; i++) {
    string w;
    cin >> w;
    for (int j=0; j<L; j++) dir[make_pair(j, w[j])].push_back(w);
  }
  for (int i=1; i<=N; i++) {
    string w;
    cin >> w;
    int c = solve_it(dir, w);
    cout << "Case #" << i << ": " << c << endl;
  }
}
