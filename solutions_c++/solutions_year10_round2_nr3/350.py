#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long LL;

template<typename T> inline int sz(const T& x) { return (int)x.size(); }

int table[26];

int solve_bf(int n) {
	if(table[n] >= 0)
		return table[n];

	--n;
	int am = 0;

	for(int S = 0; S < (1<<n); ++S) {

		set<int> nums;
		for(int j = 0, k = 2; j < n; ++j,++k) {
			if( S&(1<<j) ) {
				nums.insert(k);
			}
		}

		int N = n+1;

		while(N != 1) {
			set<int>::iterator it = nums.find(N);
			if( it == nums.end() )
				goto DONE;

			N = sz(nums);
			nums.erase(nums.upper_bound(N), nums.end());
		}

		++am;
		DONE:
		continue;
	}

	table[n+1] = am;
	return am;
}


int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	memset(table, -1, sizeof table);

	int TC; cin >> TC;
	for(int tc = 1; tc <= TC; ++tc) {
		cout << "Case #" << tc << ": ";

		int n; cin >> n;


		int ans = solve_bf(n)%100003;

		cout << ans << '\n';
	}

	return 0;
}
