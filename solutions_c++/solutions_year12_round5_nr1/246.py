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
int l[22];
vector<pair<int, int> > p;

bool solve() {
  sort(all(p));
  reverse(all(p));
}

int main(){
  int t; scanf("%d\n", &t);
  for(int j = 1;j<=t;j++){
    int n;
    cin >> n;
    rep(i, n){
      cin >> l[i];
    }
    p.clear(); p.resize(n);
    rep(i, n) {
      int a; cin >> a;
      p[i] = mp(a, -i);
    }
    solve();
    cout << "Case #" << j << ": ";
    rep(i, n) {
      if(i == n-1) {
	printf("%d", -p[i].second);
      }else {
	printf("%d ", -p[i].second);
      }
    }
    cout << endl;
  }
  return 0;

}
