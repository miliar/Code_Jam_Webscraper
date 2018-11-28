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
#include<complex>

using namespace std;
#define INF  ((1 << 29) - 1)
#define eps 1e-9
#define PI 3.14159265358979323846
#define sz(v) ((int)(v).size())
#define MP make_pair
#define PB push_back
#define all(v) (v).begin(), (v).end()
typedef long long ll;

int p;
vector<int> first_in_level;
vector<int> cost, m;
int f(int l, int s){
	return first_in_level[l] + s; 
}
ll dp[20][20][5500];
ll calc(int l, int k, int s){
	if (dp[l][k][s] != -1LL) return dp[l][k][s];
	ll &res = dp[l][k][s];
	if (l == 0){
		int cur_pos = 2 * s;
		int allow = min(m[cur_pos], m[cur_pos + 1]);
		if (k > allow) res = (ll)INF * INF;
		if (k < allow) res = 0;
		if (k == allow) res = cost[f(l, s)];
		return res;
	}
	res = (ll)INF * INF;
	ll cur_cost = cost[f(l, s)];
	ll non = calc(l-1, k + 1, 2 * s) + calc(l - 1, k + 1, 2 * s + 1);
	ll take = cur_cost + calc(l - 1, k, 2 * s) + calc(l - 1, k, 2 * s + 1);
	res = min(res, non);
	res = min(res, take);
	return res;
}
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("largesubmit.txt", "w", stdout);
	int T;
	cin >> T;
	for (int it = 1; it <= T; ++it){
		int x;
		//memset(dp, -1, sizeof(dp));
		for (int i = 0; i < 14; ++i)
			for (int j = 0; j < 14; ++j)
				for (int k = 0; k < 1200; ++k)
					dp[i][j][k] = -1LL;
		cin >> p;
		m.clear();
		cost.clear();
		first_in_level.clear();
		for (int i = 0; i < (1 << p); ++i){
			scanf("%d", &x);
			m.push_back(x);
		}
		for (int i = 0; i < (1 << p) - 1; ++i){
			scanf("%d", &x);
			cost.push_back(x);
		}
		int cur_match = 0;
		for (int j = 0; j < p; ++j){
			if (j) cur_match += (1 << (p - j));
			first_in_level.push_back(cur_match);
		}
		int res = calc(p - 1, 0, 0);
		printf("Case #%d: %d\n", it, res);
	}
	return 0;
}