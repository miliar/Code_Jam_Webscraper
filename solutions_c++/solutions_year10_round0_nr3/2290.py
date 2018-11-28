
/**
 *
 *  Time-stamp:<2010/05/08 09:49:44>
 **/

#include <functional>
#include <algorithm>
#include <iostream>
#include <complex>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <cctype>
#include <queue>
#include <cmath>
#include <set>
#include <map>
using namespace std;

#define For(i, s, n) for(int i = (int)(s); i < (int)(n); ++i)
#define rep(i, n) For(i, 0, n)
#define iter(c) __typeof((c).begin())
#define each(c, i) for(iter(c) i = (c).begin(); i != (c).end(); ++i)
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define mp make_pair

typedef long long LL;
typedef complex<double> point;

int main()
{
  int t, R, k, N, head;
  LL ans, tmp;
  vector<int> que;

  cin >> t;
  rep(cnt, t) {
    ans = head = 0;
    cin >> R >> k >> N;
    que.clear(); que.resize(N);
    rep(i, N) cin >> que[i];

    while(R--) {
      int start = head;
      for(tmp = 0; tmp + que[head] <= k; ) {
        tmp += que[head];
        head = (head + 1) % N;
        if(head == start) break;
      }
      ans += tmp;
    }
    cout << "Case #" << cnt+1 << ": ";
    cout << ans << endl;
  }

  return 0;
}


