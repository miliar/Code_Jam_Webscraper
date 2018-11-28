#include <iostream>
#include <iterator>
#include <algorithm>
#include <string>
#include <vector>
#include <utility>
#include <queue>
#include <map>
#include <sstream>

#include <cmath>

// Boost library can be retrieved from http://www.boost.org/
// I uses 1.40.0

#include <boost/foreach.hpp>
#include <boost/array.hpp>
#include "boost/tuple/tuple.hpp"
#include "boost/tuple/tuple_comparison.hpp"
#include "boost/tuple/tuple_io.hpp"
#include "boost/algorithm/minmax_element.hpp"
#include <boost/math/common_factor.hpp>
#include <boost/numeric/interval.hpp>
#include "lib.hpp"

#define foreach         BOOST_FOREACH
#define reverse_foreach BOOST_REVERSE_FOREACH

typedef unsigned long long ULL;
typedef long long LL;
typedef unsigned long UL;
typedef unsigned int UI;
typedef unsigned char UC;

using namespace std;
using namespace boost;
using namespace boost::math;
using namespace boost::numeric;
using namespace boost::numeric::interval_lib::compare::certain;

int main(void)
{
	int n;
	cin >> n; cin.ignore();
	for(int nn = 0; nn < n; ++nn) {
		ULL result = 0;
		map<char, int> table;
		string s;
		int num = 0;

		getline(cin, s); 
		foreach(char c, s) {
			if(table.count(c)) {
			} else {
				++num;
				if(num == 1) table[c] = 1;
				else if(num == 2) table[c] = 0;
				else table[c] = num-1;
			}
		}
		if(num == 1) num = 2;
		foreach(char c, s) {
			result = result * num + table[c];
		}

		cout << "Case #" << nn+1 << ": " << result << endl;
	}
	
	return 0;
}
