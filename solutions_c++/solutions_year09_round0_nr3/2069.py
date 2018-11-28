#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include<iostream>
#include<fstream>
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
#define _CRT_SECURE_NO_WARNINGS
#define INF  ((1 << 31) - 1)
#define LLINF  ((ll)((1LL << 63) - 1))
#define eps 0.00000001
#define million 1000000
#define PI 3.14159265358979323846
#define sz(v) ((int)(v).size())
#define MP make_pair
#define PB push_back
#define all(v) (v).begin(), (v).end()
typedef long long ll;

const string pattern = "welcome to code jam";

void out(int x) {
	x %= 10000;
	int p = 1000;
	for (int i = 0; i < 4; ++i) {
		cout << x / p;
		x %= p;
		p /= 10;
	}
	cout << "\n";
}

int dp[510][50];
string s;

int solve(int pos, int used) {
	if (pos >= s.size()) {
		if (used == 19) return 1;
		else return 0;
	}
	if (used >= 19) return 1;
	if (dp[pos][used] >= 0) return dp[pos][used];
	int res = 0;
	for (int i = pos; i < s.size(); ++i) {
		if (s[i] == pattern[used]) 
			res = (res + solve(i + 1, used + 1)) % 10000;
	}
	return dp[pos][used] = res % 10000;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	getline(cin, s);
	for (int id = 0; id < n; ++id) {
		cerr << id;
		memset(dp, -1, sizeof(dp));
		cout << "Case #" << id + 1 << ": ";
		getline(cin, s);
		int res = solve(0, 0);
		out(res);
	}
	return 0;
}