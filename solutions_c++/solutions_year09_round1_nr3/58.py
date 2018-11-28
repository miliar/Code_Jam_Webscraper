
#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <cmath>
#include <complex>
#include <numeric>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i,s) for(__typeof((s).begin()) i = (s).begin(); i != (s).end(); ++i)
#define ALLOF(s) ((s).begin()), ((s).end())

typedef long long integer;
typedef double decimal;

decimal memo[50][50][50];


integer chmemo[50][50];
integer choose(int n, int c) {
  integer& res = chmemo[n][c];
  if(res == 0){
    if(c == 0){
      res = 1;
    }else if(c == n){
      res = 1;
    }else{
      res = choose(n - 1, c) + choose(n - 1, c - 1);
    }
  }
  return res;
}

decimal prob(int nEach, int nKinds, int nRest, int newcard) {
  assert(newcard <= nRest);
  return 
    (decimal) choose(nRest, newcard)
    * (decimal) choose(nKinds-nRest, nEach - newcard)
    / (decimal) choose(nKinds, nEach);
}

decimal solve(int nEach, int nKinds, int nRest) {
  decimal& res = memo[nEach][nKinds][nRest];
  if(res < 0){
    if(nRest == 0){
      res = 0;
    }else{
      
      int mini = min(nEach, nRest);
      decimal tmp = 0;
      for(int newcard = mini; newcard > 0; --newcard){
	tmp += prob(nEach, nKinds, nRest, newcard) * (1 + solve(nEach, nKinds, nRest - newcard));
      }
      decimal p0 = prob(nEach, nKinds, nRest, 0);
      res = (tmp + p0) / (1.0 - p0);
      
    }
  }
  
//   cerr << "solve(" << nEach << ", " << nKinds << ", " << nRest << ") = " << res << endl;
  return res;
}


int main(void) {
  REP(i, 50) REP(j, 50) REP(k, 50)
    memo[i][j][k] = -1;
  
  int nCases;
  cin >> nCases;
  
  REP(iCase, nCases) {
    int nKinds;
    int nEach;
    cin >> nKinds >> nEach;
    
    decimal res = 1 + solve(nEach, nKinds, nKinds - nEach);
    
    printf("Case #%d: %7lf\n", iCase + 1, res);
  }
  
  return 0;
}
