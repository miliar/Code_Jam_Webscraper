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
		ULL n, pd, pg; cin >> n >> pd >> pg;
		string s;

		if(pd == 0) {
			if(pg != 100) s = "Possible";
			else s = "Broken";
		} else {
			ULL d2 = 0, d5 = 0, pd_ = pd;
			if(pd_ % 2 == 0) { ++d2; pd_ /= 2; }
			if(pd_ % 2 == 0) { ++d2; pd_ /= 2; }
			if(pd_ % 5 == 0) { ++d5; pd_ /= 5; }
			if(pd_ % 5 == 0) { ++d5; pd_ /= 5; }

			ULL nn = 1 * (d2 == 2 ? 1 : d2 == 1 ? 2 : 4) * (d5 == 2 ? 1 : d5 == 1 ? 5 : 25);
//cerr << "nn: " << nn << endl;
			if(nn > n) {
				s = "Broken";
			} else {
				ULL w = pd * nn / 100;
//cerr << "w: " << w << endl;
				if(w != 0 && pg == 0) s = "Broken";
				else {
					if(w != nn && pg == 100) { s = "Broken"; }
					else { s = "Possible"; }
				}
			}
		}

		cout << "Case #" << casenum+1 << ": " << s << endl;
	}

	return 0;
}
