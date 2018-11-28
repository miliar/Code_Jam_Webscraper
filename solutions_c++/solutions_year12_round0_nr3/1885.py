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
int a, b;
string sa, sb;




int count(int i) {
	if (i % 10000 == 0)
		cerr << i << endl;
	stringstream ss;
	ss << i;
	string s = ss.str();
	string si = s;
	int res = 0;
	vector<string> cand;
	for (int i = 0; i < s.size() - 1; ++i) {
		s = s.back() + s;
		s.pop_back();
		if ((sa <= s) && (s <= sb) && (s > si)) {
			cand.push_back(s);
		}
	}
	sort(cand.begin(), cand.end());
	for (int i = 0; i + 1 < cand.size(); ++i)
		if (cand[i] != cand[i + 1])
			++res;
	if (cand.size() != 0)
		++res;
	return res;
}


int solve() {
	int res = 0;
	for (int i = a; i <= b; ++i)
		res += count(i);
	return res;
}


int main() {
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cin >> a >> b;
		stringstream ssa, ssb;
		ssa << a;
		sa = ssa.str();
		ssb << b;
		sb = ssb.str();
		cout << "Case #" << i + 1 << ": " << solve() << endl;
		std::cerr << i << endl;
	}
	return 0;
}
