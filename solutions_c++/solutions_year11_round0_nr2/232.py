#include <iostream>
#include <sstream>

#include <iterator>

#include <algorithm>
#include <numeric>
#include <utility>
#include <limits>

#include <string>

#include <vector>
#include <deque>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>

#include <tuple>
#include <initializer_list>

#include <cmath>
#include <cstdio>

// Boost library can be retrieved from http://www.boost.org/
// I uses 1.46.1

#include <boost/range/irange.hpp>
#include <boost/range/iterator_range.hpp>

typedef unsigned long long ULL;
typedef long long LL;
typedef unsigned long UL;
typedef unsigned int UI;
typedef unsigned short US;
typedef unsigned char UC;

#define RNG(v) (v).begin(), (v).end()

using namespace std;

template<class Integer>
inline boost::iterator_range< boost::range_detail::integer_iterator<Integer> >
IR(Integer first, Integer  last)
{ return boost::irange(first, last); }

int main(void)
{
	ios_base::sync_with_stdio(false);

	vector<char> be = { 'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F' };
	map<char, int> rbe;
	for(auto i : IR(0U,be.size())) {
		rbe.insert(make_pair(be[i], i));
	}

	UI t; cin >> t;
	for(UI i=0;i<t;++i) {
		map<pair<char, char>, char> comb;
		UI c; cin >> c;
		for(auto j : IR(0U,c)) {
			string s; cin >> s;
			comb.insert(make_pair(make_pair(s[0],s[1]), s[2]));
			comb.insert(make_pair(make_pair(s[1],s[0]), s[2]));
		}
		multimap<char, char> opposed;
		UI d; cin >> d;
		for(auto j : IR(0U,d)) {
			string s; cin >> s;
			opposed.insert(make_pair(s[0],s[1]));
			opposed.insert(make_pair(s[1],s[0]));
		}
		UI n; cin >> n;
		string s; cin >> s;

//		for(auto val: comb) { cerr << val.first.first << ',' << val.first.second << ':' << val.second << endl; }
//		for(auto val: opposed) { cerr << val.first << ':' << val.second << endl; }

		string result;
		vector<int> count(be.size());
		for(auto ch:s) {
//cerr << result << ':' << ch << endl;
			if(!result.empty()) {
				if(comb.count(make_pair(result.back(), ch))) {
					char nch = comb[make_pair(result.back(), ch)];
					--count[rbe[result.back()]];
					result.back() = nch;
				} else {
					bool cleared = false;
//for(auto vv: count) { cerr << vv; } cerr << endl;
					for(auto check: boost::make_iterator_range(opposed.equal_range(ch))) {
						if(count[rbe[check.second]]) {
							result.clear();
							fill(RNG(count), 0);
							cleared = true;
							break;
						}
					}
					if(!cleared) {
						result.push_back(ch);
						++count[rbe[result.back()]];
					}
				}
			} else {
				result.push_back(ch);
				++count[rbe[result.back()]];
			}
		}

		cout << "Case #" << i+1 << ": [";
		bool flag = false;
		for(auto v:result) { if(flag) cout << ", "; cout << v; flag = true; }
		cout << ']' << endl;
	}

	return 0;
}
