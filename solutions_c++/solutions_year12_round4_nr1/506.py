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
		ULL N; cin >> N; vector<ULL> d(N), l(N), idx(N);
		REP(i, N) {
			cin >> d[i] >> l[i]; idx[i] = N;
		}
		int minidx = 0;
		ULL D; cin >> D;
		bool flag = D <= 2 * d[0];
		REP_(i, 1, N) {
			if(d[i] <= 2 * d[0]) {
				idx[i] = 0; minidx = i;
			}
			else break;
		}
		REP_(i, 1, N) {
//cerr << "i:" << i << endl;
			if(idx[i] != N) {
//cerr << "can:" << idx[i] << ':' << d[i] << ':' << d[idx[i]] <<  endl;
				if(D <= d[i] +  min(l[i], d[i] - d[idx[i]])) {
//cerr << "reach" << endl;
					flag = true;
					break;
				}
				REP_(j, minidx+1, N) {
					if(d[j] <= d[i] + min(l[i], d[i] - d[idx[i]])) {
//cerr << "i->j:" << i << ',' << j << endl;
						idx[j] = i; minidx = j;
					} else break;
				}
			}
		}
		if(flag) {
			cout << "Case #" << casenum+1 << ": YES" << endl;
		} else {
			cout << "Case #" << casenum+1 << ": NO" << endl;
		}
	}

	return 0;
}
