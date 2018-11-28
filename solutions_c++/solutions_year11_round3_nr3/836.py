#include<iostream>
#include<vector>
#include<algorithm>

#define FOR(i,b,n) for(int i = b; i < n; i++)
#define REP(i,n) FOR(i,0,n)

using namespace std;

typedef long long ll;

int t, n;
ll l, h;

int main(){
  cin >> t;

  REP(Case, t){
    cin >> n >> l >> h;

    vector<int> V(n);
    REP(i, n)
      cin >> V[i];

    bool f = 0;
    ll ans;

    FOR(i, l, h + 1){
      f = 1;
      REP(j, n)
	if(V[j] % i && i % V[j])
	  f = 0;
      if(f){
	ans = i;
	break;
      }
    }

    cout << "Case #" << Case + 1 << ": ";
    if(f)
      cout << ans << endl;
    else
      cout << "NO" << endl;
  }
  return 0;
}
