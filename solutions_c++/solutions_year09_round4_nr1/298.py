
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
int n;

bool isOK(const vector<int>& mat) {
  REP(i, n){
    if(mat[i] > i)
      return false;
  }
  return true;
}

int solve(vector<int> mat) {
  int res = 0;
  REP(i, n-1){
    if(mat[i] <= i)
      continue;
    for(int j = i+1; j < n; ++j){
      if(mat[j] <= i){
	for(int k = j-1; k >= i; --k){
	  swap(mat[k], mat[k+1]);
	  res++;
	}
	goto NEXT;
      }
    }
  NEXT:
    ;
  }
  return res;
}

int main(void) {
  int nCases;
  cin >> nCases;
  
  REP(iCase, nCases) {
    cin >> n;
    
    vector<int> mat;
    REP(i, n){
      string s;
      cin >> s;
      int pos = n-1;
      for(; pos >= 0; --pos){
	if(s[pos] == '1')
	  break;
      }
      pos = max(0, pos);
      mat.push_back(pos);
    }

    int res = 0;
    res = solve(mat);
    
    cout << "Case #" << (iCase+1) << ": " << res << endl;
  }
  
  return 0;
}
