#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <numeric>
#define beg 10000000
#define pb push_back
#define mp make_pair
#define sz(x) (int)x.size()
#define ss stringstream
#define pf pop_front()
#define nd second
#define st first
#define fr(i, n) for(int i = 0; i < (int)n; i++)
#define LL long long
#define vi vector<int>
#define pii pair<int, int>
#define vii vector<pii >
#define vs vector<string>
#define LD long double

using namespace std;

//always reset global variables!

int dp[1000][20];
string s = "welcome to code jam";

void solveCase(int Case) {
	cout << "Case #" << Case << ": ";
	memset(dp, 0, sizeof(dp));
	string T;
	getline(cin, T);
	fr(i, sz(T) + 1) dp[i][sz(s)] = 1;
	for(int pos = sz(T) - 1; pos >= 0; pos--) fr(i, sz(s)) {
		dp[pos][i] += dp[pos + 1][i];
		if(T[pos] == s[i]) dp[pos][i] += dp[pos + 1][i + 1];
		dp[pos][i] %= 10000;
	}
	string ans = "0000";
//	cout << dp[0][0] << endl;
	ans[3] += dp[0][0] % 10;
	dp[0][0] /= 10;
	ans[2] += dp[0][0] % 10;
	dp[0][0] /= 10;
	ans[1] += dp[0][0] % 10;
	dp[0][0] /= 10;
	ans[0] += dp[0][0] % 10;
	dp[0][0] /= 10;
	cout << ans << endl;
}

int main() {
	int n;
	cin >> n;
	string temp;
	getline(cin, temp);
	fr(i, n) solveCase(i + 1);
	return 0;
}
