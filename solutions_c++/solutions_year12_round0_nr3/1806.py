#include <iostream>
#include <sstream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <complex>
#include <cmath>
#include <iomanip>
#include <cstdlib>
#include <unordered_map>

using namespace std;
#define pb         push_back
#define all(a)     (a).begin(),(a).end()
#define sz(a)      (int)((a).size())
#define rep(i,n)   for(int i=0; i<n; ++i)
#define REP(i,j,k) for(int i=j; i<k; ++i)

int main () {
  int TC; scanf("%d", &TC);
  unordered_map<int, set<int> > h;
  char s[16], t[16];
  REP (i, 1, 2000001) {
    sprintf(s, "%d", i);
    strcpy(t, s);
    int l = strlen(t);
    int j;
    rep (k, l-1) {
      rotate(t, t+1, t+l);
      j = atoi(t);
      if (i < j) h[i].insert(j);
    }
  }
  
  rep (tc, TC) {
    int a, b; scanf("%d %d", &a, &b);
    int result = 0;
    REP (i, a, b) {
      for (auto it = h[i].begin(); it != h[i].end(); it++) {
	result += i < *it && *it <=b;
      }
    }
    cout << "Case #" << tc+1 << ": " << result << endl;
  }
  return 0;
}
