#include<iostream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>
#include<list>
#include<map>
#include<deque>
#include<stack>
#include<queue>
#include<string>
#include<sstream>
#include<time.h>
#include<numeric>
#include<functional>

using namespace std;
#define INF  ((1 << 31) - 1)
#define eps 1e-9
#define PI 3.14159265358979323846
#define sz(v) ((int)(v).size())
#define MP make_pair
#define PB push_back
#define all(v) (v).begin(), (v).end()
typedef long long ll;

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("1.out", "w", stdout);
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; ++tt){
		ll res = 0, r, k, n, tmp;
		cin >> r >> k >> n;
		vector<ll> v;
		for (int i = 0; i < n; ++i){
			scanf("%lld", &tmp);
			v.push_back(tmp);
		}
		vector<ll> cost, pos;
		for (int i = 0; i < n; ++i){
			ll cur_cost = v[i];
			int j = (i + 1) % n;
			while (j != i && cur_cost + v[j] <= k){
				cur_cost += v[j];
				j = (j + 1) % n;
			}
			cost.push_back(cur_cost);
			pos.push_back(j);
		}
		int cur_pos = 0;
		for (int i = 0; i < r; ++i){
			res += cost[cur_pos];
			cur_pos = pos[cur_pos];
		}
		printf("Case #%d: %lld\n", tt, res);
		cerr << tt << " of " << t << " tests pased\n";
	}
	cerr << "all tests passed\n";
	return 0;
}
