#include <iostream>
#include <string>
#include <vector>

using namespace std;

#include "/home/isaac/program/topcoder/vectorRangeCheck.h"
#include "/home/isaac/program/topcoder/dispUtils.h"
#include "/home/isaac/program/topcoder/debugUtils.h"


////////////////////////////////////////////////////////////////
/// Please remove the code above. It's only for diagnostics ////
////////////////////////////////////////////////////////////////


#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <numeric>
#include <iterator>
#include <cmath>
#include <set>

typedef long long LL;
typedef vector<string> Vs;
typedef vector<int> Vi;
typedef vector<bool> Vb;
typedef vector<long long> Vll;
typedef vector<double> Vd;
typedef vector<Vi> Mi;
#define forUp(x,y) for(int x=0;x<(y);x++)
#define forDown(x,y) for(int x=(y)-1;x>=0;x--)
#define LET(l,r) forUp(_t,1) for(typeof(r) l=r; !_t; _t=1)
#define forEach(x,c) LET(&_s,(c)) LET(_x,_s.begin()) for(;_x!=_s.end();_x++) LET(&x,*_x)

struct Dir {
  map<string,Dir> subdirs;
  int mkdir(string s) {
    if (s.size()==0) return 0;
    if (s[0]=='/') s=s.substr(1);
    int k=s.find('/');
    string subdir=s.substr(0,k);
    int needed=0;
    if (subdirs.count(subdir)==0) needed++;
    needed+=subdirs[subdir].mkdir(k==string::npos?"":s.substr(k));
    return needed;
  }
};

int main() {
  //  freopen("a.in","r",stdin);
  int nCases;
  cin >> nCases;
  forUp(caseNr,nCases) {
    int N,M;
    Dir root;
    cin >> N >> M;
    forUp(i,N) {
      string s;
      cin >> s;
      root.mkdir(s);
    }
    int needed=0;
    forUp(i,M) {
      string s;
      cin >> s;
      needed+=root.mkdir(s);
    }

    cout << "Case #" << caseNr+1 << ": " << needed << endl;
  }
  return 0;
}






