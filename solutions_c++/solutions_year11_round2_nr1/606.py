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

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {

		UL n; cin >> n;
		vector<string> table(n); for(auto &v : table) { cin >> v; }
		vector<long double> wp(n), owp(n), oowp(n);
		REP(i, n) {
			int num = 0, won = 0;
			REP(j, n) {
				if(table[i][j] == '1') {
					++num; ++won;
					int num2 = 0, won2 = 0;
					REP(k, n) {
						if(i != k) {
							if(table[k][j] == '0') { ++num2; ++won2; }
							else if(table[k][j] == '1') { ++num2; }
						}
					}
					owp[i] += (long double)won2/num2;
				}else if(table[i][j] == '0') {
					++num;
					int num2 = 0, won2 = 0;
					REP(k, n) {
						if(i != k) {
							if(table[k][j] == '0') { ++num2; ++won2; }
							else if(table[k][j] == '1') { ++num2; }
						}
					}
					owp[i] += (long double)won2/num2;
				}
			}
			wp[i] = (long double)won/num;
			owp[i] /= num;
		}
		REP(i, n) {
			int num = 0;
			REP(j, n) {
				if(table[i][j] != '.') {
					++num;
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= num;
		}

		cout << "Case #" << casenum+1 << ":" << endl;
		REP(i, n) {
			cout << fixed << setprecision(12) << 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i] << endl;
		}
	}

	return 0;
}
