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
#include<cstring>
#include<bitset>
#include<sstream>
#include<time.h>
#include<numeric>
#include<functional>

using namespace std;
#define _CRT_SECURE_NO_WARNINGS
#define INF  ((1 << 31) - 1)
#define LLINF  ((ll)((1LL << 63) - 1))
#define eps (1e-9)
#define million 1000000
#define PI 3.14159265358979323846
#define sz(v) ((int)(v).size())
#define MP make_pair
#define PB push_back
#define all(v) (v).begin(), (v).end()
typedef long long ll;

int dp[102][300][4];

int D, I, M, n;
vector<int> x;

int solve(int suffix, int last, int mode) {
	if (suffix == 0)
		return 0;
	int & res = dp[suffix][last][mode];
	if (res >= 0)
		return res;
	res = INF;
	res = min(res, D + solve(suffix - 1, last, 0));
	for (int i = 0; i < 256; ++i) 
		if (abs(i - last) <= M)
			res = min(res, abs(x[n - suffix] - i) + solve(suffix - 1, i, 0));
	if (mode == 0)
		for (int i = 0; i < 256; ++i) 
			if (abs(i - last) <= M) {
				res = min(res, I + solve(suffix, i, 2 - (i < last)));
			}
	if (mode == 1) {
		for (int i = 0; i < 256; ++i) 
			if (abs(i - last) <= M && i < last) {
				res = min(res, I + solve(suffix, i, 2 - (i < last)));
			}
	}
	if (mode == 2) {
		for (int i = 0; i < 256; ++i) 
			if (abs(i - last) <= M && i > last) {
				res = min(res, I + solve(suffix, i, 2 - (i < last)));
			}
	}
	return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int id = 0 ;id < T; ++id) {
		cerr << id << " ";
		cout <<	"Case #" << id + 1 << ": ";
		memset(dp, -1, sizeof(dp));
		cin >> D >>I>> M >> n;
		x.clear();
		for (int i = 0; i < n; ++i) {
			int y;
			cin >> y;
			x.push_back(y);
		}
		int res = INF;
		for (int i = 0; i < 256; ++i)
			res = min(res, solve(n, i, 0));
		cout << res << "\n";
	}
	return 0;
}