#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define FOR(i, N, M)  for(int i = (int)(N); i <= (int)(M); ++ i)
#define FORD(i, N, M) for (int i = (int)(N); i >= (int)(M); -- i)
#define FORI(it, x)   for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define REP(i, N)     for(int i = 0; i != (int)(N); ++ i)

inline void print(vector<char> &curr){
  cout << "[";
  bool first = true;
  FORI(it, curr){
    char c = *it;
    if(first)
      first = false;
    else
      cout << ", ";
    cout << c;
  }
  cout << "]";
}

inline void solve() { 
  int C, D, N;
  cin >> C;
  map<pair<char,char>,char> combine;
  set<pair<char,char> > oppose;
  FOR(i,1,C){
    char a,b,c;
    cin >> a >> b >> c;
    combine[make_pair(a,b)] = c;
    combine[make_pair(b,a)] = c;
  }
  cin >> D;
  FOR(i,1,D) {
    char a,b;
    cin >> a >> b;
    oppose.insert(make_pair(a,b));
    oppose.insert(make_pair(b,a));
  }

  cin >> N;
  vector<char> curr;
  FOR(i,1,N){
    char nxt;
    cin >> nxt;
    curr.push_back(nxt);
    // check for combinations
    bool removed = false;
    while(curr.size() > 1) {
      char last1 = curr[curr.size() - 1], last2 = curr[curr.size() - 2];
      pair<char,char> inp = make_pair(last1, last2);
      if(combine.find(inp) == combine.end())
        break;
      removed = true;
      curr.erase(curr.end() - 2, curr.end());
      curr.push_back(combine[inp]);
    }
    // check for opposing
    if(!removed) FOR(j, 0, curr.size() - 2) {
      if(oppose.find(make_pair(curr[j], curr[curr.size() - 1])) != oppose.end()){
        curr.clear();
      }
    }
  }

  print(curr);
}

int main() {
  int TESTS;
  cin >> TESTS;
  FOR(test, 1, TESTS) {
    cout << "Case #" << test << ": ";
    solve();
    cout << endl;
  }
} 
