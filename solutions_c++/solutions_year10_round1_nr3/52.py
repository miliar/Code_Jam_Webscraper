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

using namespace std;
typedef long long ll;

int a1, a2, b1, b2;

int calc(ll a, ll b){
	if (a == 0 || b == 0) return 0;
	double golden = (sqrt(5.0)+1.0)/2.0;
	int low = (int) (a/golden);
	if (low >= b) low = b;
	int high = (int) ceil(a*golden);
	if (high == low) high++;
	if (high > b) high = b+1;
	int ans = low + (b-high+1);
	//cout << "calc(" << a << "," << b << ") = " << ans << endl;
	return ans;
}

int main(){
	int t; cin >> t;
	for (int zzz = 1; zzz <= t; zzz++){
		cin >> a1 >> a2 >> b1 >> b2;
		ll ans = 0;
		for (ll i = a1; i <= a2; i++){
			ans += calc(i,b2)-calc(i,b1-1);
		}
		cout << "Case #" << zzz << ": " << ans << endl;
	}
	return 0;
}
