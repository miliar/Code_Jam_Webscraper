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

int INF = 1000000;

vector<double> p;

double solve(int a, int b) {
  double ans = b+2;

  double pall = 1.f;
  rep(i, a) {
    pall *= p[i];
  }

  double ans2 = (b-a+1) * pall + (b-a+1+b+1) * (1.0-pall);
  ans = min(ans, ans2);
  
  double pnow = 1.f;
  rep(i, a) { //suppose a-i time delete i.e. i char remains
    double buf = 0.f;
    buf += a-i;
    buf += (b-i+1) * (pnow);
    buf += ((b-i+1)+(b+1)) * (1-pnow);
    ans = min(ans, buf);

    pnow *= p[i];
  }
  return ans;
}

int main(){
  int t; scanf("%d\n", &t);
  for(int j = 1;j<=t;j++){
    int a, b; cin >> a >> b;
    p.clear(); p.resize(a);
    rep(i, a) {
      cin >> p[i];
    }
    double ans = solve(a, b);
    printf("Case #%d: %.9f\n", j, ans);
    //    cout << "Case #" << j << ": " << ans <<endl;
  }
  return 0;

}
