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

#include <boost/random/mersenne_twister.hpp>
#include <boost/random/uniform_int_distribution.hpp>

typedef unsigned long long ULL;
typedef long long LL;
typedef unsigned long UL;
typedef unsigned int UI;
typedef unsigned short US;
typedef unsigned char UC;

#define RNG(v) (v).begin(), (v).end()
#define RRNG(v) (v).rbegin(), (v).rend()
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

	boost::random::mt19937 rng;

	UI cases; cin >> cases;
	REP(casenum, cases) {
		int N; ULL W, L; cin >> N >> W >> L;
		boost::random::uniform_int_distribution<ULL> randw(0, W);
		boost::random::uniform_int_distribution<ULL> randl(0, L);
		vector<ULL> r(N);
		vector<ULL> x(N), y(N);
		for(auto &v : r) { cin >> v; }
		vector<int> idx(N); iota(RNG(idx), 0);
		sort(RNG(idx), [&](int n1, int n2) { return r[n1] > r[n2]; });
		auto check = [&](int ii, ULL xx, ULL yy) -> bool {
			if(xx > W || yy > L) return false;
			REP(i, ii) {
				if((xx - x[idx[i]]) * (xx - x[idx[i]]) + (yy - y[idx[i]]) * (yy - y[idx[i]]) < (r[idx[i]] + r[idx[ii]]) * (r[idx[i]] + r[idx[ii]])) return false;
			}
			return true;
		};
		function<bool(int)> process = [&](int ii) -> bool {
//cerr << idx << endl;
			if(ii == N) return true;
			switch(ii) {
			case 0:
				x[idx[0]] = 0; y[idx[0]] = 0; return process(1);
			case 1:
				x[idx[1]] = W; y[idx[1]] = L; return process(2);
			default:
				REP(i, 100) {
//cerr << idx << ':' << i << endl;
					ULL xx = randw(rng), yy = randl(rng);
					if(check(ii, xx, yy)) {
						x[idx[ii]] = xx; y[idx[ii]] = yy;
						if(process(ii+1)) return true;
					}
				}
			}
			return false;
		};
		while(!process(0)) ;
		cout << "Case #" << casenum+1 << ":";
		REP(i, N) {
			cout << ' ' << x[i] << ' ' << y[i];
		}
		cout << endl;
	}

	return 0;
}
