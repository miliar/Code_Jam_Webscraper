#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include<cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include<bitset>

#define REP(i,b,n) for(int i=b;i<(int)n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define FOR(it,o)  for(__typeof((o).begin()) it=(o).begin(); it!=(o).end(); ++it)


typedef long long ll;

using namespace std;

map<char, char> M;

void precalc(){
  vector<string> from, to;
  from.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
  from.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
  from.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");
  from.push_back("y qeez");
  
  to.push_back("our language is impossible to understand");
  to.push_back("there are twenty six factorial possibilities");
  to.push_back("so it is okay if you want to just give up");
  to.push_back("a zooq");
  
  rep(i, 4){
    rep(j, from[i].length()){
      if(from[i][j] == ' ')continue;
      M[from[i][j]] = to[i][j];
    }
  }
}

string conv(string s){
  rep(i, s.length()){
    if(s[i] != ' ')s[i] = M[s[i]];
  }
  return s;
}

int main(){
  precalc();
  int T;
  cin >> T;
  string tmp;
  getline(cin, tmp);
  rep(tc, T){
    string s;
    getline(cin, s);
    cout << "Case #" << tc+1 <<": " << conv(s)  << endl;;
  }
  return 0;
}
