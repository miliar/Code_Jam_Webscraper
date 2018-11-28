#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <limits>
#include <functional>
#include <iterator>
#include <sstream>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i = (a), _b = b; i != _b; ++i)
#define REP(i, N) FOR(i, 0, N)
#define ALL(x) (x).begin(), (x).end()
#define RALL(x) (x).rbegin(), (x).rend()
#define REMOVE(C, V) (C).erase(remove(ALL(C), (V)), (C).end())

#define pb(x) push_back(x)
#define mp(a, b) make_pair(a, b)
#define sz() size()
#define len() length()
#define cs() c_str()

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef vector<bool> VB;
typedef long long LL;
typedef unsigned long long ULL;

const int BASE = 10000, mn = 512;

int dp[mn][mn];

int calc(const string &s1, const string &s2, int pos1, int pos2) {
	if (pos1 >= s1.len() || pos2 >= s2.len() || s1[pos1] != s2[pos2])
		return 0;

	if (dp[pos1][pos2] != -1)
		return dp[pos1][pos2];

	if (pos2 == s2.length() - 1)
		return 1;

	int ret = 0;
	FOR (i, pos1 + 1, s1.len()) {
		if (s1[i] == s2[pos2 + 1]) {
			ret += calc(s1, s2, i, pos2 + 1);
			ret %= BASE;
		}
	}
	return dp[pos1][pos2] = ret;
}

int main() {
	int N;
	cin >> N;

// cin.get();

	FOR (kase, 1, N + 1) {
		string str;
		getline(cin, str);

if (str.len() == 0) {
	--kase;
	continue;
}

		string str2 = "welcome to code jam";
		memset(dp, -1, sizeof(dp));

		int ret = 0;
		REP (i, str.len()) {
			ret += calc(str, str2, i, 0);
			ret %= BASE;
		}
		cout << "Case #" << kase << ": " << setw(4) << setfill('0') << ret << endl;
	}
}
