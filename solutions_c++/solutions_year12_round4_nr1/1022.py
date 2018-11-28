
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>


using namespace std;

typedef long long lli;

int main(){
  int tc;
  cin >> tc;
  for(int tid = 1; tid <= tc; tid++){
    int n; cin >> n;
    vector< pair<lli,lli > > tab(n+1);
    for(int i=0; i<n; i++){
      cin >> tab[i].first >> tab[i].second;
    }
    cin >> tab[n].first;
    vector< lli > dp(n,-1);
    dp[0] = tab[0].first;
    bool flg = false;
    for(int i=0; i<n; i++){
      if( dp[i] == -1 )continue;
      lli d = dp[i] + tab[i].first;
      if( d >= tab[n].first ){ flg = true; break; }
      for(int j=i+1; j<n; j++){
	if( tab[j].first > d )break;
	lli ds = tab[j].first - tab[i].first;
	dp[j] = max(dp[j], min(ds, tab[j].second));
      }
    }
    cout << "Case #" << tid << ": ";
    if( flg )cout << "YES" << endl;
    else cout << "NO" << endl;

  }
  return 0;
}
