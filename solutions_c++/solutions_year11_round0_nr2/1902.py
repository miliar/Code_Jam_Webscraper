#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <fstream>
#include <sstream>
#include <set>

using namespace std;

int main() {
  ifstream cin("B-large.in");
  ofstream cout("out.txt");
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    map<pair<char, char>, char> comb;
    set<pair<char, char> > opp;
    int C;
    cin >> C;
    for(int i = 0; i < C; i++) {
      char c1,c2;
      cin >> c1 >> c2;
      char c;
      cin >> c;
      comb[make_pair(c1, c2)] = c;
      comb[make_pair(c2, c1)] = c;
    }
    int D = 0;
    cin >> D;
    for(int i = 0; i < D; i++) {
      char c1, c2;
      cin >> c1 >> c2;
      opp.insert(make_pair(c1, c2));
      opp.insert(make_pair(c2, c1));
    }
    int N = 0;
    cin >> N;
    vector<char> list;
    for(int i = 0; i < N; i++) {
      char c;
      cin >> c;
      list.push_back(c);
      if(i == 0)
        continue;
      map<pair<char, char>, char>::const_iterator it = comb.find(make_pair(c, list[list.size()-2]));
      if(it != comb.end()) {
        list.pop_back();
        list.back() = it->second;
      } else {
        for(int i = 0; i < list.size(); i++) {
          if(opp.find(make_pair(c, list[i])) != opp.end()) {
            list.clear();
            break;
          }
        }
      }
    }
    cout << "Case #" << t << ": ";
    cout << '[';
    for(int i = 0; i < list.size(); i++) {
      cout << list[i];
      if(i != list.size()-1)
        cout << ", ";
    }
    cout << ']';
    cout << endl;
  }
}
