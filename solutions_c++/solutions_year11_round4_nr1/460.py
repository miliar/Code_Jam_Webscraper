// Using C++0x mode in g++ 4.6.0

#include <iostream>
#include <sstream>
#include <iomanip>

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
// I used 1.46.1

#include <boost/range/irange.hpp>
#include <boost/range/iterator_range.hpp>

typedef unsigned long long ULL;
typedef long long LL;
typedef unsigned long UL;
typedef unsigned int UI;
typedef unsigned short US;
typedef unsigned char UC;

#define RNG(v) (v).begin(), (v).end()
#define REP(v, e) for(UI v = 0U; v < e; ++v)
#define REP_(v, s, e) for(UI v = s; v < e; ++v)
#define REPV(v, e) for(v = 0; v < e; ++v)
#define REPV_(v, s, e) for(v = s; v < e; ++v)

using namespace std;

template<class Integer>
inline boost::iterator_range< boost::range_detail::integer_iterator<Integer> >
IR(Integer first, Integer  last)
{ return boost::irange(first, last); }

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {
		UI x, s, r, t, n; cin >> x >> s >> r >> t >> n;
		vector<UI> len(n), speed(n);
		UI len0 = x;
		REP(i, n) {
			UI 	b, e, w; cin >> b >> e >> w;
			len[i] = e - b;
			speed[i] = s + w;
			len0 -= len[i];
		}
		if(len0) {
			len.push_back(len0);
			speed.push_back(s);
		}
		vector<UI> index(len.size()); iota(RNG(index), 0);
		sort(RNG(index), [&](UI i1, UI i2) { return speed[i1] < speed[i2]; });
		double tt = t, result = 0;
		REP(i, index.size()) {
			UI ii = index[i];
			UI leni = len[ii], speedi = speed[ii];
//cerr << i << ':' << result << ':' << leni << ':' << speedi << endl;
			if(tt > 0) {
				double speed_ = speedi + (r - s);
				if(leni / speed_ >= tt) {
					result += tt + (leni - tt * speed_) / speedi;
					tt = 0;
				} else {
					result += leni / speed_;
					tt -= leni / speed_;
				}
			} else {
				result += double(leni)/speedi;
			}
		}

		cout << "Case #" << casenum+1 << ": " << fixed << setprecision(12) << result << endl;
	}

	return 0;
}
