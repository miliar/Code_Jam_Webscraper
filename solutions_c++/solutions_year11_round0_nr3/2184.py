using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }
template <class T> int toInt(const T &x)
{ stringstream s; s << x; int r; s >> r; return r; }

#define For(i, a, b) for (int i=(a); i<(b); ++i)
#define foreach(x, v) for (typeof (v).begin() x = (v).begin(); \
                           x != (v).end(); ++x)
#define D(x) cout << #x " = " << (x) << endl

const double EPS = 1e-9;
int cmp(double x, double y = 0, double tol = EPS){
    return( x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

int main(){
  int t;
  cin >> t;
  for(int c = 1; c <= t; ++c)
    {
      int n;
      cin >> n;
      vector<int> candy;
      int mask = 0;
      for(int i = 0, dummy; i < n and cin >> dummy ; ++i)
        {
          candy.push_back(dummy);
          mask ^= dummy;
        }
      
      if(mask == 0)
        {
          sort(candy.begin(), candy.end());
          int ans = 0;
          for(int i = 1; i < candy.size() ; ++i)
            ans += candy[i];
          printf("Case #%d: %d\n", c, ans);
        }
      else
        printf("Case #%d: NO\n", c);
      
    }
  return 0;
}
