
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

int nRows, nCols;
integer base;
integer field[500+10][500+10];

const double EPS = 1e-10;

int main(void) {
  int nCases;
  cin >> nCases;

  REP(iCase, nCases) {
    cin >> nRows >> nCols >> base;
    REP(iRow, nRows){
      string s;
      cin >> s;
      assert((int)s.size() == nCols);
      REP(iCol, nCols){
	field[iRow][iCol] = (s[iCol] - '0') + base;
      }
    }
    
    int res = -1;
    int maxi = min(nRows, nCols);
    for(int k = 3; k <= maxi; ++k){
      REP(i, nRows - k + 1){
	REP(j, nCols - k + 1){
	  integer ci = 2*i + k-1;
	  integer cj = 2*j + k-1;
	  
	  integer gi = 0;
	  integer gj = 0;
	  REP(ii, k){
	    REP(jj, k){
	      if((ii == 0 || ii == k-1) &&
		 (jj == 0 || jj == k-1))
		continue;
	      gi += (2*i+2*ii - ci) * field[i+ii][j+jj];
	      gj += (2*j+2*jj - cj) * field[i+ii][j+jj];
	    }
	  }
	  
	  if(gi == 0 && gj == 0){
	    res = k;
	    goto NEXT_K;
	  }
	}
      }

    NEXT_K:
      ;
    }
    
    cout << "Case #" << (iCase+1) << ": ";
    if(res < 0){
      cout << "IMPOSSIBLE" << endl;
    }else{
      cout << res << endl;
    }
  }
  
  return 0;
}
