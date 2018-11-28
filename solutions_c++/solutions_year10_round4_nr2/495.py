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
#include <cstring>

using namespace std;

int p;
int m[2048];
int prices[2048];

int memo[2048][16];

int dp(int pos, int left){
	if (memo[pos][left] != -1) return memo[pos][left];
	int& ans = memo[pos][left];

	if (pos >= (1 << p)){
		int i = pos - (1 << p);
		if (left >= m[i]) ans = 0;
		else ans = 0x3f3f3f3f;
		//cout << "single team: " << endl;
		//cout << "dp(" << pos << "," << left << ") = " << ans << endl;
		return ans;
	}
	if (left > 0) ans = dp(pos,left-1);
	else ans = 0x3f3f3f3f;
	ans = min(ans,min(dp(2*pos,left)+dp(2*pos+1,left),dp(2*pos,left+1)+dp(2*pos+1,left+1)+prices[pos]));
	//cout << "dp(" << pos << "," << left << ") = " << ans << endl;
	return ans;
}

int main(){
	int ttt; cin >> ttt;
	for (int zzz = 1; zzz <= ttt; zzz++){
		cin >> p;
		//cout << "p = " << p << endl;
		for (int i = 0; i < (1<<p); i++){
			cin >> m[i];
			m[i] = p - m[i];
		}
		for (int i = p-1; i >= 0; i--){
			for (int j = 0; j < (1 << i); j++){
				cin >> prices[(1<<i) + j];
			}
		}
		
		memset(memo,-1,sizeof(memo));
		cout << "Case #" << zzz << ": " << dp(1,0) << endl;
	}
	return 0;
}
