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

int main() {
  // freopen("a1.in","r",stdin);
  int t,n,k;
  cin >> t;
  forUp(i,t) {
    cin >> n >> k;
    bool on=((k+1)%(1<<n)==0);
    cout << "Case #" << i+1 << ": " << (on?"ON":"OFF") << endl;
  }
  return 0;
}






