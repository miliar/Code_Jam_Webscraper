#include <iostream>
#include <vector>
#include <sstream>
#include <map>
#include <string>
#include <algorithm>

using namespace std;
typedef unsigned int uint;
typedef map<pair<int,int>, uint> rmap_t;

string welcome("welcome to code jam");

uint find_welcome(rmap_t &rmap, map<char, vector<int> > &my_map, uint wpos = 0, int spos = 0) {
  if (wpos == welcome.size()) return 1;
  if (rmap.count(make_pair(wpos, spos)) > 0) return rmap[make_pair(wpos, spos)];
  vector<int> &pos_list = my_map[welcome[wpos]];
  uint cnt = 0;
  for (uint i=0; i<pos_list.size(); i++)
    if (pos_list[i] >= spos) cnt += find_welcome(rmap, my_map, wpos + 1, pos_list[i] + 1);
  rmap[make_pair(wpos, spos)] = cnt;
  return cnt;
}

void solve_it() {
  string line;
  getline(cin, line);
  map<char, vector<int> > my_map;
  for (uint i=0; i<line.size(); i++) my_map[line[i]].push_back(i);
  rmap_t rmap;
  uint cnt = find_welcome(rmap, my_map);
  cnt %= 10000;
  if (cnt < 10)  cout << "0";
  if (cnt < 100) cout << "0";
  if (cnt < 1000) cout << "0";
  cout << cnt << endl;
}

int main() {
  int cases;
  cin >> cases;
  cin.ignore();
  for (int i=1; i<=cases; i++) {
    cout << "Case #" << i << ": ";
    solve_it();
  }
}
