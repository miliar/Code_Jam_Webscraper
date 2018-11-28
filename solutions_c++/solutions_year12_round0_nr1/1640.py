#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <utility>
#include <cctype>
#include <numeric>
using namespace std;

#define rep(i,n) for(int (i)=0; (i)<(int)(n); ++(i))
#define foreach(c,i) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define mp make_pair

int T;
string G;
map<char,char> m;

void f() {
  m.insert(mp('a', 'y'));
  m.insert(mp('b', 'h'));
  m.insert(mp('c', 'e'));
  m.insert(mp('d', 's'));
  m.insert(mp('e', 'o'));
  m.insert(mp('f', 'c'));
  m.insert(mp('g', 'v'));
  m.insert(mp('h', 'x'));
  m.insert(mp('i', 'd'));
  m.insert(mp('j', 'u'));
  m.insert(mp('k', 'i'));
  m.insert(mp('l', 'g'));
  m.insert(mp('m', 'l'));
  m.insert(mp('n', 'b'));
  m.insert(mp('o', 'k'));
  m.insert(mp('p', 'r'));
  m.insert(mp('q', 'z'));
  m.insert(mp('r', 't'));
  m.insert(mp('s', 'n'));
  m.insert(mp('t', 'w'));
  m.insert(mp('u', 'j'));
  m.insert(mp('v', 'p'));
  m.insert(mp('w', 'f'));
  m.insert(mp('x', 'm'));
  m.insert(mp('y', 'a'));
  m.insert(mp('z', 'q'));
}

int main() {
  f();
  cin >> T;
  cin.ignore();
  rep(loop,T) {
    getline(cin, G);
    rep(i,G.size()) {
      if (G[i] == ' ') continue;
      G[i] = m[G[i]];
    }
    cout << "Case #" << loop+1 << ": " << G << endl;
  }
  return 0;
}
