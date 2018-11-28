#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string> 
#include <algorithm>
#include <utility>
#include <numeric>
#include <iostream> 
#include <sstream> 
#include <cmath>
#include <ctime>

using namespace std; 

typedef long long ll;
typedef vector<bool> VB;
typedef vector<int> VI;

#define SZ(c) ((int) (c).size())
#define ALL(c) (c).begin(), (c).end()

const int INF = 1000000000;

const int N = 10001;
int n;
bool v;
bool gates[N];
bool changeable[N];
bool t[N];
int memo[N][2];

int solve(int at, bool val) {
	if (val == t[at])
		return 0;
	if (at > (n - 1) / 2) 
		return INF;
	int &res = memo[at][val];
	if (res != -1)
		return res;
	res = INF;
	if (gates[at] == val)
		res = solve(2 * at, val) + solve(2 * at + 1, val);
	else
		res = min(solve(2 * at, val), solve(2 * at + 1, val));
	if (changeable[at]) {
		bool g = !gates[at];
		if (g == val) 
			res = min(res, 1 + solve(2 * at, val) + solve(2 * at + 1, val));
		else
			res = min(res, 1 + min(solve(2 * at, val), solve(2 * at + 1, val)));
	}  
	return res;
}

int main() {
	int nCases;
	cin >> nCases;
	for (int c = 1; c <= nCases; ++c) {
		cin >> n >> v;
		for (int i = 1; i <= (n - 1) / 2; ++i)
			cin >> gates[i] >> changeable[i];
		for (int i = (n - 1) / 2 + 1; i <= n; ++i)
			cin >> t[i];
		for (int i = (n - 1) / 2; i >= 1; --i)
			if (gates[i])
				t[i] = t[2 * i] && t[2 * i + 1];
			else
				t[i] = t[2 * i] || t[2 * i + 1];
		printf("Case #%d: ", c);
		memset(memo, -1, sizeof(memo));
		int res = solve(1, v);
		if (res < INF)
			cout << res << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
