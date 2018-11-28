#include <iostream>
#include <vector>
#include <list>
#include <sstream>
#include <map>
#include <string>
#include <algorithm>

using namespace std;
typedef unsigned int uint;
typedef unsigned long long ull; 
typedef pair<char, uint> pcu_t;

bool pcmp(const pcu_t &a, const pcu_t &b) {
  return (a.second < b.second);
}

void solve_it(int T) {
  string s;
  cin >> s;
  map<char,uint> cm;
  for (int i=0; i<s.size(); i++) cm[s[i]]++;
  uint base = cm.size();
  if (base == 1) base++;
  vector<pair<char, uint> > pl;
  for (map<char,uint>::iterator it=cm.begin(); it!=cm.end(); it++) pl.push_back(*it);
  sort(pl.begin(), pl.end(), pcmp);
  ull res = 0;
  uint cnt = 1;
  uint maps = 0;
  map<char,uint> tm;
  //cout << s << endl;
  for (int i=0; i<s.size(); i++) {
    if (tm.count(s[i]) == 0) { 
      if (maps == 1) {
        tm[s[i]] = 0;
        res = res * base;
      }
      else {
        tm[s[i]] = cnt;
        res = base * res + cnt++;
      };
      maps++;
    }
    else res = res * base + tm[s[i]];
    //cout << i << " " << base << " " << s[i] << " " << tm[s[i]] << " " << res << endl;
  }
  cout << res << endl;
}

int main() {
  int cases;
  cin >> cases;
  for (int i=1; i<=cases; i++) {
    cout << "Case #" << i << ": ";
    solve_it(i);
  }
}
