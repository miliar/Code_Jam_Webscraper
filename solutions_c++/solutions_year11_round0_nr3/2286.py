#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
//#include <list>
#include <set>
#include <sstream>

#include <cstdio>
#include <cstring>
#include <climits>
#include <cassert>

#define FOR(i,s,n) for (int i = (int)(s); i < (int)(n); ++i)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define cerr if (0) cerr

using namespace std;

int main()
{
  int T, N;

  cin >> T;

  REP(i, T) {
    cin >> N;

    vector<int> ary(N);
    REP(j, N) cin >> ary[j];

    sort(ALL(ary));

    int ans = -1;
    REP(j, N-1) {
      // 0 ~ j, j+1 ~ N-1
      int head = ary[0];
      int tail = ary[j+1];
      int sum  = tail;
      FOR(k, 1, j) { head ^= ary[k]; }
      FOR(k, j+2, N) { tail ^= ary[k]; sum += ary[k]; }
      
      if (head == tail) {
	if (ans < sum) {
	  ans = sum;
	}
      }
    }

    cout << "Case #" << i+1 << ": ";
    if (ans > 0) cout << ans << endl;
    else         cout << "NO" << endl;
  }

  return 0;
}

