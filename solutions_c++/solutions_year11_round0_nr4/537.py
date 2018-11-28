
#include <iostream>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

#define REP(i, n) for(int i = 0; i < (int)(n); ++i)

using namespace std;

int main(void) {
  int nCases;
  cin >> nCases;
  REP(iCase, nCases){
    int n;
    cin >> n;
    double ans = 0;
    REP(i, n){
      int x;
      cin >> x;
      if(x != i+1)
	ans++;
    }

    printf("Case #%d: %.6f\n", iCase+1, ans);
  }
  return 0;
}
