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
  //  freopen("b.in","r",stdin);
  int nCases;
  const int Inf=1000000000;
  cin >> nCases;
  forUp(caseNr,nCases) {
    int N,K,B,T;
    cin >> N >> K >> B >> T;
    // disp4(N,K,B,T);
    Vi x(N),v(N);
    forUp(i,N) cin >> x[i];
    forUp(i,N) cin >> v[i];
    // disp2(x,v);
    Mi Z(K+1,N+1);
    for(int k=1; k<=K; k++) Z[k][0]=Inf;
    for(int n=1; n<=N; n++)
      for(int k=1; k<=K; k++) {
        Z[k][n]=k+Z[k][n-1];
        if (T*v[n-1]>=B-x[n-1]) {
          // disp2(k,n);
          Z[k][n]=min(Z[k][n],Z[k-1][n-1]);
        }
      }
    // disp(Z);
    cout << "Case #" << caseNr+1 << ": ";
    if (Z[K][N]>=Inf)
      cout << "IMPOSSIBLE";
    else
      cout << Z[K][N];
    cout << endl;
  }
  return 0;
}






