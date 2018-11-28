#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
using namespace std;
static const double EPS = 1e-10;
typedef long long ll;

string solve(ll N, ll D, ll G){
	if(G == 100){
		if(D == 100) return "Possible";
		else return "Broken";
	}
	if(G == 0){
		if(D > 0) return "Broken";
		else return "Possible";
	}
	
	for(ll i = 1; i <= D; i++){
		if(D % i == 0LL && 100LL % i == 0LL && 100LL/i <= N){
			ll n = 100LL/i;
			ll w = n*D/100LL;
			return "Possible";
		}
	}
	return "Broken";
	
}

int main(){
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++){
		ll n, d, g;
		cin >> n >> d >> g;
		cout << "Case #" << i << ": " << solve(n, d, g) << endl;
	}
	return 0;
}
