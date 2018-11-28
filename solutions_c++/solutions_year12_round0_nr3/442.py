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

using namespace std;

#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)
#define UNIQUE(a) (a).erase(unique((a).begin(), (a).end()), (a).end())

int INF = 1000000;
typedef long long ll;

int count_digit(int a) {
  int ret = 0;
  while(a > 0) {
    ++ret;
    a /= 10;
  }
  return ret;
}

int calc_next(int now, int mult) {
  int top = now % 10;
  int tail = now / 10;
  return top*mult+tail;
}

ll solve(int a, int b, int d) {
  int mult = 1;
  rep(i, d-1) {
    mult *= 10;
  }
  //  cout << a << " " << b << " " << d << " " <<  mult << endl;

  ll ans = 0;
  for(int i = a; i <= b; ++i) {
    int now = i;
    vector<ll> cand;
    rep(j, d) {
      //      cout << i << " " << now << " " << endl;
      if(i < now && now <= b) {
	cand.pb(now);
      }
      now = calc_next(now, mult);
    }
    sort(all(cand));
    UNIQUE(cand);
    ans += cand.size();
  }
  return ans;
}

int main(){
  int t; scanf("%d\n", &t);

  for(int j = 1; j<=t; j++){
    int a, b; cin >> a >> b;
    int d = count_digit(a);
    ll ans = solve(a, b, d);
    cout << "Case #" << j << ": " << ans <<endl;
  }
  return 0;

}
