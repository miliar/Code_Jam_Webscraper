#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <algorithm>
#include <utility>
#include <cassert>

using namespace std;
typedef long long ll;

int d, i, m, n;
int arr[256];

ll memo[256][512];

ll min(ll a, ll b){
	if (a < b) return a;
	return b;
}

ll max(ll a, ll b){
	if (a > b) return a;
	return b;
}

ll dp(int pos, int val){
	if (pos == n) return 0;
	if (memo[pos][val] != -1) return memo[pos][val];
	//cout << "dp(" << pos << ", " << val << ")" << endl;
	ll& ret = memo[pos][val];
	ret = d + dp(pos+1,val);
	if (val < arr[pos]){
		for (int v = val+1; v <= min(arr[pos]-1,val+m); v++){
			ret = min(ret, i + dp(pos,v));
		}
	}
	else if (val > arr[pos]){
		for (int v = val-1; v >= max(arr[pos]+1,val-m); v--){
			ret = min(ret, i + dp(pos,v));
		}
	}
	for (int v = max(0,val-m); v <= min(255,val+m); v++){
		assert(abs(v-val) <= m);
		ret = min(ret, abs(v-arr[pos]) + dp(pos+1,v));
	}
	if (abs(val-arr[pos]) <= m) ret = min(ret, dp(pos+1,arr[pos]));
	//cout << "dp(" << pos << ", " << val << ") = " << ret << endl;
	return ret;
}

int main(){
	int t; cin >> t;	
	for (int zzz = 1; zzz <= t; zzz++){
		cin >> d >> i >> m >> n;
		//cout << "here: zzz = " << zzz << endl;
		for (int v = 0; v < n; v++)
			cin >> arr[v];
		memset(memo,-1,sizeof(memo));
		ll ans = dp(0,0);
		for (int v = 0; v < 256; v++){
			ans = min(ans,dp(0,v));
		}
		cout << "Case #" << zzz << ": " << ans << endl;
	}
	return 0;
}
