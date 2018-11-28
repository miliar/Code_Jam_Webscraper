#include <algorithm>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
#include <cstring>

#define SIZE(s) ((int)((s).size()))
#define FOREACH(it,vec) for(typeof((vec).begin())it=(vec).begin();it!=(vec).end();++it)
#define REP(i,n) for(int i=0;i<(int)(n);++i)

using namespace std;

int T,N,C,D;
string s;
int NB[26][26];
int OP[26][26];

int main(void) {
  cin >> T;
  REP(t,T) {
    memset(NB,-1,sizeof(NB));
    memset(OP,-1,sizeof(OP));

    cin >> C;
    REP(c,C) {
      cin >> s;
      REP(i,3) s[i]-='A';
      NB[(int)s[0]][(int)s[1]] = s[2];
      NB[(int)s[1]][(int)s[0]] = s[2];
    }

    cin >> D;
    REP(d,D) {
      cin >> s;
      REP(i,2) s[i]-='A';
      OP[(int)s[0]][(int)s[1]] = 1;
      OP[(int)s[1]][(int)s[0]] = 1;
    }

    cin >> N;
    cin >> s;

    vector<char> v;
    REP(i,N) {
      int add = s[i]-'A';
      while(SIZE(v)>0 && NB[(int)v.back()][add] > -1) {
        add = NB[(int)v.back()][add];
        v.pop_back();
      }

      bool boom = false;
      REP(j,SIZE(v)) if (OP[(int)v[j]][add] == 1) { boom = true; break; }
      if (boom) v.resize(0);
      else v.push_back(add);
    }

    cout << "Case #" << (t+1) << ": [";
    REP(i,SIZE(v)) {
      cout << (char)(v[i]+'A');
      if (i<SIZE(v)-1) cout << ", ";
    }
    cout << "]" << endl;
  }
  return 0;
}
