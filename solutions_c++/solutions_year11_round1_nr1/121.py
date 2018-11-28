
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



int main(void) {
  int nCases;
  cin >> nCases;
  REP(iCase, nCases) {
    integer n, pd, pg;
    cin >> n >> pd >> pg;

    bool res = false;
    if(pg == 100){
      res = pd == 100;
    }else if(pg == 0){
      res = pd == 0;
    }else{
      
      int tmp = 100;
      while(pd % 2 == 0 && tmp % 2 == 0){
	pd /= 2;
	tmp /= 2;
      }
      
      while(pd % 5 == 0 && tmp % 5 == 0){
	pd /= 5;
	tmp /= 5;
      }
      
      res = tmp <= n;
    }
    
    cout << "Case #" << (iCase+1) << ": ";
    if(res)
      cout << "Possible" << endl;
    else
      cout << "Broken" << endl;
  }
  
  return 0;
}
