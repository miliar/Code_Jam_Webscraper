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
typedef pair<int, int> pii;
const long double PI = 3.14159265358979323846;  



int main() {
	srand(513);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cerr << i << endl;
		
		int w, l, n;
		cin >> n >> w >> l;
		vector<pll> r(n);
		for (int j = 0; j < n; ++j) {
			cin >> r[j].first;
			r[j].second = j;
		}
		sort(r.begin(), r.end());
		reverse(r.begin(), r.end());
		vector<pair<ll, pll> > ans(n);
		int j = 0;
		while(j < n) {
			int h = 0;
			while(true) {
				++h;
				
				int r1 = rand();
				int r2 = rand();
				ll x = r1 * r2 % (w + 1);
				int r3 = rand();
				int r4 = rand();
				ll y = r3 * r4 % (l + 1);
				bool c = true;
				for (int k = 0; k < j; ++k) {
					if ((ans[k].second.first - x) * (ans[k].second.first - x) + (ans[k].second.second - y) * (ans[k].second.second - y) <
						(r[j].first + r[k].first) * (r[j].first + r[k].first)) {
							c = false;
							break;
					}
				}
				if (c) {
					ans[j] = make_pair(r[j].second, make_pair(x, y));
					break;
				}
				if (h == 100) {
					j = -1;
					break;
				}
			}
			++j;
		}
		cout << "Case #" << i + 1 << ":";
		sort(ans.begin(), ans.end());
		for (int j = 0; j < ans.size(); ++j)
			cout << " " << ans[j].second.first << " " << ans[j].second.second;
		cout << endl;
	}

	return 0;
}