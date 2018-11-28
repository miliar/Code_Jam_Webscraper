// gcc version 4.8.1 20130328 (prerelease) (GCC) at http://www.drangon.org/mingw/
// with -std=c++11

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
// 1.52 is used

#pragma GCC diagnostic ignored "-Wconversion"
#include <boost/range/irange.hpp>
#include <boost/range/iterator_range.hpp>
#pragma GCC diagnostic warning "-Wconversion"

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

map<char, int> table = { {'X', 0 }, {'O', 1 }, {'T', 2 } };

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases; cin.ignore(numeric_limits<streamsize>::max(), '\n');
	REP(casenum, cases) {
		string result;
		int num = 0;
		int counter[4+4+2][3] = { 0 };
		REP(i, 4) {
			string s;
			getline(cin, s);
			REP(j, 4) {
				if(s[j] == '.') continue;
				int t = table[s[j]];
				++num;
				++counter[  i][t];
				++counter[4+j][t];
				if(  i == j) ++counter[8][t];
				if(3-i == j) ++counter[9][t];
			}
		}
		REP(i, 10) {
			if(counter[i][0] + counter[i][2] == 4) result = "X won";
			if(counter[i][1] + counter[i][2] == 4) result = "O won";
		}
		if(!result.size()) {
			if(num == 16) result = "Draw";
			else result = "Game has not completed";
		}
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
		cout << "Case #" << casenum+1 << ": " << result << endl;
	}

	return 0;
}
