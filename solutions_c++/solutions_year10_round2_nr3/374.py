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
#include <queue>
#include <stack>

#include <cmath>

// Boost library can be retrieved from http://www.boost.org/
// I uses 1.42.0

#include <boost/foreach.hpp>
//#include <boost/math/common_factor.hpp>
//#include <boost/numeric/interval.hpp>
//#include "lib.hpp"

#define foreach  BOOST_FOREACH
#define rforeach BOOST_REVERSE_FOREACH

typedef unsigned long long ULL;
typedef long long LL;
typedef unsigned long UL;
typedef unsigned int UI;
typedef unsigned short US;
typedef unsigned char UC;

using namespace std;
//using namespace boost::math;
//using namespace boost::numeric;
//using namespace boost::numeric::interval_lib::compare::certain;

UI comb(UI n, UI r)
{
	if(n < 0 || r > n || r < 0) return 0;
	if(r > n - r) r = n - r;
	ULL result = 1;
	for(UI i = 1; i <=r; ++i) {
		result = (result * n / i) % 100003ULL;
		--n;
	}
	return result;
}

const int LIM = 501;
UI table[LIM][LIM];
bool table_[LIM][LIM];

UI pure(UI n, UI k)
{
	if(table_[n][k]) return table[n][k];
	if(k == 1) {
		table[n][k] = 1; table_[n][k] = true;
		return 1;
	}
	ULL result = 0;
	for(UI l=1;l<=k-1;++l) {
		result += pure(k,l) * comb(n-k-1, k-1-l);
		result %= 100003ULL;
	}
	table[n][k] = result; table_[n][k] = true;
	return result;
}

int main(void)
{
	int num_problem;
	cin >> num_problem;
	for(int idx_problem = 0; idx_problem < num_problem; ++idx_problem) {
		UI result = 0;

		UI n;
		cin >> n;
		for(UI i=1;i<=n-1;++i) {
			result += pure(n, i);
			result %= 100003U;
		}

		cout << "Case #" << idx_problem+1 << ": " << result << endl;
	}
	
	return 0;
}
