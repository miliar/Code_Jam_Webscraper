#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define beg 10000000
#define pb push_back
#define mp make_pair
#define sz size()
#define iss istringstream
#define oss ostringstream
#define pf pop_front()
#define nd second
#define st first
#define fr(i, n) for(int i = 0; i < (int)n; i++)
#define LL long long
#define vi vector<int>
#define pii pair<int, int>
#define vs vector<string>

using namespace std;

int M;
int nodes[10010];
int change[10010];
int dp[10010][2];

int solve(int node, int V) {
	int& ref = dp[node][V];
	if(ref != -1) return ref;
	ref = beg;
	if(node >= (M + 1)/2) {
		if(nodes[node] == V) return ref = 0;
		else return ref = beg;
	}
	if(nodes[node] == V) ref <?= solve(2*node, V) + solve(2*node + 1, V);
	else ref <?= min(solve(2*node, V), solve(2*node + 1, V));
	if(change[node]) {
		if(nodes[node] == V) ref <?= min(solve(2*node, V), solve(2*node + 1, V)) + 1;
		else ref <?= solve(2*node, V) + solve(2*node + 1, V) + 1;
	}
	return ref;
}

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int tests;
	cin >> tests;
	fr(test, tests) {
		cin >> M;
		int V;
		cin >> V;
		memset(nodes, -1, sizeof(nodes));
		memset(change, -1, sizeof(change));
		memset(dp, -1, sizeof(dp));
		for(int i = 1; i <= (M-1)/2; i++) cin >> nodes[i] >> change[i];
		for(int i = (M + 1)/2; i <= M; i++) cin >> nodes[i];
		int ans = solve(1, V);
		if(ans >= beg) {
			cout << "Case #" << test + 1 << ": IMPOSSIBLE" << endl;
			continue;
		}
		cout << "Case #" << test + 1 << ": " << ans << endl;
	}
	return 0;
}
