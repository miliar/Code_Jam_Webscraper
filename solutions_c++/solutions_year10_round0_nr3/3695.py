#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>

#define FOR(i,b,n) for(int i = b; i < n; i++)
#define REP(i,n) FOR(i,0,n)
using namespace std;

typedef long long ll;

int main(){
  int t;
  ll r, k, n, current;
  
  cin >> t;

  REP(q, t){
    cin >> r >> k >> n;
    vector<int> g;
    g.clear();

    REP(i, n){
      int a;
      cin >> a;
      g.push_back(a);
    }

    ll ans = 0;

    current = 0;
    REP(i, r){
      ll cnt = 0;
      ll start = current;
      while(true){
	if(cnt + g[current] > k) break;
	cnt += g[current];
	current = (current + 1) % n;
	if(current == start) break;
      }
      ans += cnt;
    }

    cout << "Case #" << (q + 1) << ": " << ans << endl;
  }

  return 0;
}
