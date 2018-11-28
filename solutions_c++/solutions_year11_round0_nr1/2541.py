#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <sstream>
#include <complex>
#include <cmath>
#include <iomanip>
#include <cstdlib>

using namespace std;
#define pb          push_back
#define all(a)      (a).begin(),(a).end()
#define sz(a)       (int)((a).size())
#define REP(i,j,k)  for(int i=j;i<k;++i)
#define rep(i,n)    for(int i=0;i<n;++i)

int main () {
  int T; scanf("%d", &T);

  rep (tc, T) {
    int result = 0;

    int N; scanf("%d", &N);
    int b = 1, o = 1, tb = 0, to = 0;
    
    while (N--) {
      char c; scanf(" %c", &c);
      int  a; scanf("%d", &a);

      if (c == 'O') {
	int x = abs(o-a)-to>0?abs(o-a)-to+1:1;
	result += x;
	tb     += x;
	to      = 0;
	o = a;
      } else {
	int x = abs(b-a)-tb>0?abs(b-a)-tb+1:1;
	result += x;
	to     += x;
	tb      = 0;
	b = a;
      }
    }
    
    printf("Case #%d: %d\n", tc+1, result);
  }
  return 0;
}
