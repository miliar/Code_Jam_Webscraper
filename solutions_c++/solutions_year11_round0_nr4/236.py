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

	UI t; cin >> t;
	for(UI i=0;i<t;++i) {
		UI n; cin >> n;
		vector<UI> v(n); for(auto &val:v){cin>>val;--val;}
		vector<char> flag(n);
		UI result = 0;
		for(auto idx : IR(0U,n)) {
			if(!flag[idx]) {
				flag[idx] = 1;
				UI count = 1, idx_ = v[idx];
				while(!flag[idx_]) {
					flag[idx_] = 1; idx_ = v[idx_]; ++count;
				}
				if(count>1) result += count;
			}
		}
		cout << "Case #" << i+1 << ": " << result << endl;
	}

	return 0;
}
