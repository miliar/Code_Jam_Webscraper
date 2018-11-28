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

		UI r, c, d; cin >> r >> c >> d;
		vector<vector<UI>> table(r, vector<UI>(c, d));
		for(auto &v1 : table) {
			string s; cin >> s;
			REP(i, c) {
				v1[i] += (s[i] - '0');
			}
		}
		UI k = min(r,c); bool flag = false;
		while(k >= 3) {
			REP(i, r-k+1) {
				REP(j, c-k+1) {
					ULL sx = 0;
					ULL sy = 0;
					ULL sum = 0;
					REP(ii, k) {
						REP(jj, k) {
							if((ii == 0 || ii == k - 1) && (jj == 0 || jj == k - 1)) continue;
							sx += ii * table[i+ii][j+jj];
							sy += jj * table[i+ii][j+jj];
							sum += table[i+ii][j+jj];
						}
					}
//cerr << k << ':' << sx << ':' << sy << ':' << sum << endl;
					if(2 * sx == (k-1)*sum && 2*sy == (k-1)*sum) {
						flag = true;
						break;
					}
				}
				if(flag) break;
			}
			if(flag) break;
			--k;
		}

		if(k >= 3) {
			cout << "Case #" << casenum+1 << ": " << k << endl;
		} else {
			cout << "Case #" << casenum+1 << ": IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
