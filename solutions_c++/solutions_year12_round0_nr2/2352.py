#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<cstdio>
#include<string>
using namespace std;
#define P pair<int, int>
vector<P> adj[31];
int s[101], n, p;
int dp[101][101];
int solve(int i, int j){
	if(i == n){
		if(j)
			return -2;
		return 0;
	}
	int &res = dp[i][j];
	if(res != -1)
		return res;
	res = 0;
	int x1 = 0, x2 = solve(i + 1, j);
	if(j)
		x1 = solve(i + 1, j - 1);
	for(int k = 0; k < adj[s[i]].size(); k++){
		if(adj[s[i]][k].second - adj[s[i]][k].first == 2){
			if(j)
				res = max(res, x1 + ((adj[s[i]][k].second >= p) ? 1 : 0));
		}else
			res = max(res, x2 + ((adj[s[i]][k].second >= p) ? 1 : 0));
	}
	return res;
}
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	for(int i = 0; i < 11; i++){
		for(int j = i; j <= i + 2 && j < 11; j++){
			for(int k = j; k <= i + 2 && k < 11; k++){
				adj[i + j + k].push_back(P(i, k));
			}
		}
	}
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		int sr;
		cin >> n >> sr >> p;
		for(int i = 0; i < n; i++)
			cin >> s[i];
		memset(dp, -1, sizeof dp);
		int ans = solve(0, sr);
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}

