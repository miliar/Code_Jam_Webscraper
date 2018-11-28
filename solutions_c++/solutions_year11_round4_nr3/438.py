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
#define REPV(type, v, e) for(type v = 0; v < e; ++v)
#define REPV_(type, v, s, e) for(type v = s; v < e; ++v)

using namespace std;

template<class Integer>
inline boost::iterator_range< boost::range_detail::integer_iterator<Integer> >
IR(Integer first, Integer  last)
{ return boost::irange(first, last); }

template<typename T, typename OutputIterator>
inline T pshieve(T n, OutputIterator out) // type should be changable
{
	T count = 0;
	if(n<2) return count;
	*out++=2;
	++count;
	std::vector<bool> v(n/2);
	const T nn1 = static_cast<T>(std::sqrt(n));
	const T nn = max(nn1, n/nn1);
	T i;
	for(i=3;i<=nn;i+=2) {
		if(v[i/2-1]==false) {
			*out++=i;
			++count;
		}
		for(T j=i+i+i;j<=n;j+=i+i) {
			v[j/2-1]=true;
		}
	}
	for(;i<=n;i+=2) {
		if(v[i/2-1]==false) {
			*out++=i;
			++count;
		}
	}
	return count;
}

int main(void)
{
	ios_base::sync_with_stdio(false);

	vector<ULL> primes;
	pshieve(1000ULL, back_inserter(primes));

	UI cases; cin >> cases;
	REP(casenum, cases) {

		ULL n; cin >> n;
		vector<ULL> counts(primes.size());
		REPV(ULL, i, n) {
			ULL ii = i+1;
			REPV(ULL, j, primes.size()) {
				ULL count = 0;
				while(ii % primes[j] == 0ULL) {
					ii /= primes[j];
					++count;
				}
				if(counts[j] < count) counts[j] = count;
			}
		}
		ULL minimum = count_if(RNG(counts), [&](ULL v) { return v > 0; });
		ULL maximum = (n>1ULL?1ULL:0ULL) + accumulate(RNG(counts), 0ULL);

		cout << "Case #" << casenum+1 << ": " << maximum - minimum << endl;
	}

	return 0;
}
