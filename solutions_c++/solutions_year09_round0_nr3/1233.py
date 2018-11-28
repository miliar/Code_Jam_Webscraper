/**
 * Qualification Round 2009
 * g++ 3.4.5
 */
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef vector<II> VII;

template<typename T> inline int sz(const T& x) { return (int)x.size(); }

const int MOD = 10000;


int solve(string& T, string& W) {
	int L[sz(W)][sz(T)];
	memset(L, 0, sizeof L);

	if( T[0] == W[0] )
		L[0][0] = 1;

	for(int i = 1; i < sz(T); ++i) {
		L[0][i] = L[0][i-1] + (T[i]==W[0] ? 1 : 0);
		L[0][i] %= MOD;
	}

	for(int j = 1; j < sz(W); ++j) {
		for(int i = 1; i < sz(T); ++i) {
			L[j][i] = L[j][i-1] + (T[i]==W[j] ? L[j-1][i-1] : 0);
			L[j][i] %= MOD;
		}
	}

	return L[sz(W)-1][sz(T)-1];
}


int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	int N;
	cin >> N;
	cin.ignore(100,'\n');

	string word("welcome to code jam");

	for(int t = 1; t <= N; ++t) {
		string text;
		getline(cin, text);

		int ans = solve(text, word);
		cout << "Case #" << t << ": ";

		ostringstream oss;
		oss << "000000" << ans;
		string out(oss.str());
		cout << out.substr( sz(out)-4, 4) << '\n';
	}


	return 0;
}
