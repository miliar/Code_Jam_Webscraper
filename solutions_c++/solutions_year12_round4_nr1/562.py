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
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; ++i) {
		int n;
		scanf("%d\n", &n);
		vector<pll> data(n), data2(n);
		int d, l, D;
		for (int j = 0; j < n; ++j) {
			scanf("%d %d\n", &d, &l);
			data[j].first = d;
			data[j].second = l;
			/*data2[j].first = d + l;
			data2[j].second = d;*/
		}
		//sort(data2.begin(), data2.end());
		scanf("%d\n", &D);
		ll x = 2 * data[0].first;
		int jj = 1;
		//cerr << j << endl;
		//int left = 0;
		vector<int> aa(n);
		for (int j = 0; j < n; ++j)
			aa[j] = data[j].first;
		aa[0] = x;
		int in = 0;
		while ((jj < n) && (in < n)) {
			if (data[jj].first <= aa[in]) {
				/*while (data[jj].second + data2[left].first < data[jj].first)
					++left;*/
				/*for (int k = 0; k < jj; ++k)
					if (data[k].first + data[k].second >= data[jj].first)*/
				x = max((ll)x, min(data[jj].first * 2 - data[in].first, data[jj].first + data[jj].second));
				aa[jj] = x;
				++jj;
			}
			else
				++in;
		}
		if (x >= D)
			cout << "Case #" << i + 1 << ": YES" << endl;
		else
			cout << "Case #" << i + 1 << ": NO" << endl;
	}

	return 0;
}