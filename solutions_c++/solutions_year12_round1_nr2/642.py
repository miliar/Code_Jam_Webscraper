#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
#include "../../../../print.hpp"

using namespace std;

#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)

int INF = 1000000;
vector<int> a, b;
int n;

bool comp(int i, int j) {
  if(a[i] != a[j] ) {
    return a[i] < a[j];
  }
  return b[i] > b[j];
}

bool comp2(int i, int j ) {
  if(b[i] != b[j]) {
    return b[i] < b[j];
  }
  return a[i] > a[j];  
}

bool solve(int& ans) {
  ans = 0;
  vector<int> ix1(n), ix2(n);
  vector<int> ok1(n), ok2(n);
  rep(i, n) {
    ix1[i] = ix2[i] = i;
  }
  sort(all(ix1), comp);
  sort(all(ix2), comp2);

  int star = 0;
  int pos2 = 0;
  int pos1 = 0;
  while(true) {
    bool movable = false;
    while(pos2 < n && ok2[ix2[pos2]] == 1) {
      ++pos2;
    }
    if(pos2 >= n) {
      return true;
    }
    if(b[ix2[pos2]] <= star) {
      ++ans;
      if(ok1[ix2[pos2]] == 0) {
	star += 2;
      }else {
	star += 1;
      }
      ok2[ix2[pos2]] = 1;
      ok1[ix2[pos2]] = 1;
      ++pos2;
      movable = true;
    }else {
      int chosen = -1;
      for(int i = 0; i < n; ++i) {
	if(ok1[i] == 1) {
	  continue;
	}
	if(a[i] > star) {
	  continue;
	}

	if(chosen == -1 || b[chosen] <= b[i]) {
	  chosen = i;
	  movable = true;
	}
      }

      if(!movable) {
	return false;
      }else {
	ok1[chosen] = 1;
	++ans;
	++star;
      }
    }
  }
}

int main(){
  int t; scanf("%d\n", &t);
  for(int j = 1;j<=t;j++){
    cin >> n;
    a.clear(); a.resize(n);
    b.clear(); b.resize(n);
    rep(i, n) {
      cin >> a[i] >> b[i];
    }
    int ans;
    bool result = solve(ans);
    if(result) {
      cout << "Case #" << j << ": " << ans <<endl;
    }else {
      cout << "Case #" << j << ": " << "Too Bad" <<endl;
    }
    //    printf("Case #%d: %.9f\n", j, ans);
  }
  return 0;

}
