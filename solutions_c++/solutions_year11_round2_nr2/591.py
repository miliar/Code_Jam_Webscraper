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

bool check(double time, vector<LL> &pos, vector<LL> &num, UI d)
{
	double wall = -1.0e+7;
	REP(i, pos.size()) {
		if(pos[i] + time - max(wall, pos[i] - time) < (num[i]-1) * d) return false;
		wall = max(wall, pos[i] - time) + num[i] * d;
	}
	return true;
}

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {

		UI c, d; cin >> c >> d;
		vector<LL> pos(c);
		vector<LL> num(c);
		REP(i, c) {
			cin >> pos[i] >> num[i];
		}
		const double diff = 0.00000001;
		double l = 0, r = 1.0e+13, cent;
		while(r - l > diff) {
			cent = (l+r)/2;
//			cerr << cent << endl;
			if(check(cent, pos, num, d)) {
				r = cent;
			} else {
				l = cent;
			}
		}

		cout << "Case #" << casenum+1 << ": " << fixed << setprecision(8) << cent << endl;
	}

	return 0;
}
