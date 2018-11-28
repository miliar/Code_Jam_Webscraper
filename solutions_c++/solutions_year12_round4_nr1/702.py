#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#include <sstream>
#include <complex>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long       li;
typedef vector<li>      vi;
typedef complex<double> pt;
typedef pair<pt, pt>    line;
typedef pair<li, li>    pi;
typedef vector<string>  vs;

#define rep(i,to)       for(li i=0;i<((li)to);i++)
#define foreach(it,set) for(__typeof((set).begin()) it=(set).begin();it!=(set).end();it++)
#define all(v)          v.begin(), v.end()

inline li bit(li n){ return 1LL<<n; }
template <class T> ostream& operator<<(ostream& os, vector<T> x){
  foreach(it, x) cout << *it << ' ';
  return os;
}
template <class T> inline void dbg(T x){
  // return;
  cerr << x << endl; 
}

li vx[8] = {1, -1, 0,  0, -1, 1,  1, -1};
li vy[8] = {0,  0, 1, -1, -1, 1, -1,  1};

void solve(li casenum){
  string ans = "NO";
  li n, dist;
  cin >> n;

  vi d(n), l(n);
  rep(i, n) cin >> d[i] >> l[i];
  cin >> dist;

  queue<pi> q;
  vector<li> mr(n, -1);

  q.push(make_pair(0, 0));
  while(!q.empty()){
    pi pos = q.front(); q.pop();
    li dpos = pos.first;
    li vind = pos.second;

    li mreach = dpos + 2 * min(d[vind] - dpos, l[vind]);

    // cout << dpos << " " << vind << " " << mreach << endl;
    if(mreach <= mr[vind]) continue;
    mr[vind] = mreach;

    if(mreach >= dist){
      ans = "YES";
      break;
    }

    for(int i=vind+1; d[i] <= mreach; i++){
      li ndpos = max(d[vind], d[i] - l[i]);
      if(ndpos + 2 * min(d[i] - ndpos, l[i]) <= mr[i]) continue;
      q.push(make_pair(ndpos, i));
    }
  }

  cout << "Case #" << casenum << ": " << ans << endl;
  return;
}

int main(){
  li t;
  cin >> t;
  rep(i, t) solve(i+1);
  return 0;
}
