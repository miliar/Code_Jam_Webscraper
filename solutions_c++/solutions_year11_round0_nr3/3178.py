#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define p(a) cout << a << endl
#define sz(a) (int)(a).size()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define zero(a) memset(a, 0, sizeof(a))
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
typedef long long int64;//NOTES:int64
typedef unsigned long long uint64;//NOTES:uint64

typedef vector<int> vint;


int main()
{
  int n,cant;
  cin >> n;
  forn(_i,n)
  {
    cin >> cant;
    vint tot;
    int x;
    forn(i,cant)
    {
     cin >> x;
     tot.pb(x);
    }
    
    int xo=tot[0];
    forab(i,1,sz(tot))
        xo ^= tot[i];
    
    if(xo)
    {
     p("Case #"<<_i+1<<": "<<"NO");
    }
    else{
     sort(tot.begin(),tot.end());
     reverse(tot.begin(),tot.end());
     tot.pop_back();
     int res=0;
     forit(i,tot)
      res += *i;
     p("Case #"<<_i+1<<": "<<res);
     
    }
  }
}
