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

int main(void)
{
	int num_problem;
	cin >> num_problem;
	for(int idx_problem = 0; idx_problem < num_problem; ++idx_problem) {
		int result = 0;

		ULL n,k,b,t;
		cin >> n >> k >> b >> t;
		vector<ULL> pos(n);
		foreach(ULL &temp, pos) { cin >> temp; }
		vector<ULL> vec(n);
		foreach(ULL &temp, vec) { cin >> temp; }
		vector<ULL> last(n);
		vector<bool> ok(n);
		if(k == 0) {
			cout << "Case #" << idx_problem+1 << ": " << 0 << endl;
			continue;
		}
		int cur = 0;
		for(UI i=0;i<n;++i) {
			last[i] = pos[i]+vec[i]*t;
			if(last[i] >= b) {
				ok[i] = true;
				++cur;
			}
		}
		if(cur < k) {
			cout << "Case #" << idx_problem+1 << ": " << "IMPOSSIBLE" << endl;
		} else {
			vector<int> cross(n);
			for(int i=0;i<n;++i) {
				for(int j=i+1;j<n;++j) {
					if(ok[i] && !ok[j]) {
						++cross[i];
					}
				}
			}
			vector<int> count;
			for(int i=0;i<n;++i) {
				if(ok[i]) count.push_back(cross[i]);
			}
			vector<int> psum(count.size());
			sort(count.begin(), count.end());
			partial_sum(count.begin(), count.end(), psum.begin());
if(k>count.size()) { cerr << "BAD" << endl; }
//			foreach(int temp, psum) { cerr << temp << ','; } cerr << endl;
			cout << "Case #" << idx_problem+1 << ": " << psum[k-1] << endl;
		}
	}
	
	return 0;
}
