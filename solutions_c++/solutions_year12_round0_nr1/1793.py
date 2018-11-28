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

char M[26] = {'y', 'h', 'e', 's', 'o',
              'c', 'v', 'x', 'd', 'u',
              'i', 'g', 'l', 'b', 'k',
              'r', 'z', 't', 'n', 'w',
              'j', 'p', 'f', 'm', 'a', 'q'};

int T;
string s;

int main(void) {
  getline(cin,s);
  stringstream SS(s);
  SS >> T;
  REP(t,T) {
    getline(cin,s);
    cout << "Case #" << t+1 << ": ";
    REP(i,SIZE(s)) if (s[i]!=' ') cout << M[s[i]-'a']; else cout << s[i];
    cout << endl;
  }

  return 0;
}
