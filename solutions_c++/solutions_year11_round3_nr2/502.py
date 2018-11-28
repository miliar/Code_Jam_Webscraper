#include <iostream>
#include <vector>
#include <map>
#include <climits>

using namespace std;

typedef long long ll;

int l;
ll t;
int n;
int c;
vector<int> a;
map<int, map<int, map<ll, ll> > > prev;

ll dist(int ci, ll ct, int cl){
	if(ci == n) return ct;
	ll & res = prev[ci][cl][ct];
	if(res == 0L){
		ll no_boost = dist(ci+1, ct+2*a[ci%c], cl);
		ll boost = LLONG_MAX;
		if(cl < l && ct + 2*a[ci%c] > t){
			if(ct >= t){
				boost = dist(ci+1, ct+a[ci%c], cl+1);
			}else{
				ll ub = t - ct;
				ll b = a[ci%c] - ub/2;
				boost = dist(ci+1, ct+ub+b, cl+1);
			}
		}
		res = min(boost, no_boost);
	}
	return res;
}

void solve(ll tc){
	cin >> l >> t >> n >> c;
	a.clear();
	prev.clear();
	for(int i = 0; i < c; i++){
		int ai;
		cin >> ai;
		a.push_back(ai);
	}
	ll res = dist(0, 0, 0);
	cout << "Case #" << tc << ": " << res << endl;
}

int main(){
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		solve(i+1);
	}
	return 0;
}
