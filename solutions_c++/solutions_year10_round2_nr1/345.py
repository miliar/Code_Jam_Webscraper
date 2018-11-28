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
#include <queue>
#include <stack>

#include <cmath>

// Boost library can be retrieved from http://www.boost.org/
// I uses 1.42.0

#include <boost/foreach.hpp>
#include <boost/algorithm/string/split.hpp>
#include <boost/algorithm/string/classification.hpp>
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
using namespace boost::algorithm;
//using namespace boost::math;
//using namespace boost::numeric;
//using namespace boost::numeric::interval_lib::compare::certain;

int main(void)
{
	int num_problem;
	cin >> num_problem;
	for(int idx_problem = 0; idx_problem < num_problem; ++idx_problem) {
		int result = 0;

		int n, m;
		set<string> sExists;
		cin >> n >> m; cin.ignore();
		for(int i=0;i<n;++i) {
			string s;
			getline(cin, s);
			sExists.insert(s);
		}
		for(int i=0;i<m;++i) {
			string s;
			getline(cin, s);
			vector<string> comp;
			split(comp, s, is_any_of("/"));
			string sCur;
			foreach(string sC, comp) {
				if(sC == "") continue;
				sCur += "/" + sC;
				if(!sExists.count(sCur)) {
					++result;
					sExists.insert(sCur);
				}
			}
		}

		cout << "Case #" << idx_problem+1 << ": " << result << endl;
	}
	
	return 0;
}
