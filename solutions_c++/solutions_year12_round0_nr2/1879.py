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

int N,T,S,P,x;

int main(void) {
  cin >> T;
  REP(t,T) {
    cin >> N >> S >> P;
    int ma = 0;
    int vie = 0;
    REP(n,N) {
      cin >> x;
      if (x==0) {
        if (P==0) ++ma;
        continue;
      }

      if (x%3== 1) {
        if ((x+2)/3 >= P) ++ma;
      }
      else {
        int y = (x+2)/3;
        if (y >= P) ++ma;
        else if (y+1 == P) ++vie;
      }
    }
    ma+= min(vie,S);
    cout << "Case #" << t+1 << ": " << ma << endl;
  }
  return 0;
}
