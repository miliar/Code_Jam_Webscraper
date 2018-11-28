#include <map>
#include <set>
#include <math.h>
#include <deque>
#include <stack>
#include <queue>
#include <vector>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <stdio.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rep(i,s,m) for(int i=s;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define PI = (2.0 * acos(0.0));
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)
#define sz 10010

int di[] = { -1, 0, 1, 0 };
int dj[] = { 0, 1, 0, -1 };
int n, m;
pair<ll, int> arrN[111];
pair<ll, int> arrM[111];
map<pair<pair<int, int> , pair<ll, ll> > , ll> dp;

ll fun(int curN, int curM, ll firstN, ll firstM) {
	if (curN == n || curM == m)
		return 0;
	if (dp.find(make_pair(make_pair(curN, curM), make_pair(firstN, firstM)))
			!= dp.end())
		return dp[make_pair(make_pair(curN, curM), make_pair(firstN, firstM))];
	ll cost = 0;
	if (arrN[curN].second == arrM[curM].second) {
		cost = min(firstN, firstM);
	}

	ll x = max(fun(curN + 1, curM, arrN[curN + 1].first, firstM - cost), fun(
			curN, curM + 1, firstN - cost, arrM[curM + 1].first)) + cost;
	return dp[make_pair(make_pair(curN, curM), make_pair(firstN, firstM))] = x;
}

int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			cin >> arrN[i].first >> arrN[i].second;
		for (int i = 0; i < m; i++)
			cin >> arrM[i].first >> arrM[i].second;
		dp.clear();
		printf("Case #%i: ", t + 1);
		cout << fun(0, 0,arrN[0].first,arrM[0].first) << endl;
	}
	return 0;
}
