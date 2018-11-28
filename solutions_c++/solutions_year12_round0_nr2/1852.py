#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<algorithm>
#include<cmath>
#include<set>
#include<queue>
#include<sstream>
#include<utility>

using std::pair;
using std::stringstream;
using std::next_permutation;
using std::sqrt;
using std::priority_queue;
using std::sort;
using std::stack;
using std::string;
using std::vector;
using std::cin;
using std::cout;
using std::endl;
using std::min;
using std::max;
using std::set;
using std::swap;
using std::random_shuffle;
using std::queue;
using std::sin;
using std::cos;
using std::make_pair;
using std::cos;
using std::cerr;

typedef long long ll; 
typedef pair<ll, ll> pll;
const long double PI = 3.14159265358979323846;  

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		int n, s, p;
		cin >> n >> s >> p;
		int ok = 0, oks = 0;
		int sum;
		for (int j = 0; j < n; ++j) {
			cin >> sum;
			if (sum >= p + 2 * max(p - 1, 0))
				++ok;
			else
				if (sum >= p + 2 * max(p - 2, 0))
					++oks;
		}
		cout << "Case #" << i + 1 << ": " << ok + min(s, oks) << endl;
		std::cerr << i << endl;
	}
	return 0;
}
