#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

template <class A, class B> void CONV(A& x, B& y) { stringstream s; s << x; s >> y; }
typedef long long LL;
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORE(i, v) FOR(i, 0, v.size())
#define FORU(i, a) for (int i = a; ; ++i)
#define SORT(v) sort(v.begin(), v.end())
#define SET(a, n) memset(a, n, sizeof a)

string s = "welcome to code jam", text;
int dp[500][19];

int go(int ptext, int ps) {
	if (ps == s.size()) return 1;
	if (ptext == text.size()) return 0;
	if (dp[ptext][ps] != -1) return dp[ptext][ps];
	int res = go(ptext+1, ps);
	if (text[ptext] == s[ps]) res += go(ptext+1, ps+1);
	res %= 10000;
	return dp[ptext][ps] = res;
}

int main() {
	int n;
	cin >> n;
	cin.get();
	FOR(i, 0, n) {
        getline(cin, text);
        SET(dp, -1);
		cout << "Case #" << i+1 << ": " << setw(4) << setfill('0') << go(0, 0) << endl;
	}
}
