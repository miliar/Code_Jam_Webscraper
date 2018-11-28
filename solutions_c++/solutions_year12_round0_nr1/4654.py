#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long int int64;
typedef vector<int> VI;
#define REP(i,a,b) for (int i=int(a); i<int(b); ++i)
void unittest();

const char *ts[3] = {
  "ejp mysljylc kd kxveddknmc re jsicpdrysi",
  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
  "de kr kd eoya kw aej tysr re ujdr lkgc jv",
};
const char *tt[3] = {
  "our language is impossible to understand",
  "there are twenty six factorial possibilities",
  "so it is okay if you want to just give up",
};

typedef map<char, char> CCMAP;
CCMAP stmap;
CCMAP tsmap; // For debug

void solve(int caseNum) {
  string source;
  while (source.empty())
    getline(cin, source);
  // cout<<"*"<<source<<"*\n";
  string target;
  REP(i, 0, source.size()) {
    char cs = source[i];
    target += (cs==' ' ? ' ' : stmap[cs]);
  }
  printf("Case #%d: %s\n", caseNum, target.c_str());
}

int main() {
  unittest();

  REP(i, 0, 3) {
    const char* s = ts[i];
    const char* t = tt[i];
    int len = strlen(s);
    REP(j, 0, len) {
      char cs = s[j];
      if (cs==' ') continue;
      char ct = t[j];
      stmap[cs] = ct;
      tsmap[ct] = cs;
    }
  }
  stmap['q'] = 'z';
  stmap['z'] = 'q';

  if (0) { // debug
    cout<<stmap.size()<<endl;
    REP(i, 0, 26) {
      char c = 'a' + i;
      if (stmap.find(c)==stmap.end())
        cout<<c<<endl;
    }
    REP(i, 0, 26) {
      char c = 'a' + i;
      if (tsmap.find(c)==tsmap.end())
        cout<<c<<endl;
    }
  }

  int caseCount;
  cin>>caseCount;
  REP(i, 1, caseCount+1)
    solve(i);

  return 0;
}

void unittest() {
}

