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
// I uses 1.43.0

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
		int r;
		cin >> r;
		int count = 1, minx = 100, miny = 100, maxx = 0, maxy = 0;
		vector<vector<char> > table(102, vector<char>(102, 0));
		vector<vector<char> > table_(102, vector<char>(102, 0));
		for(int i=0;i<r;++i) {
			int x1,x2,y1,y2;
			cin >> x1 >> y1 >> x2 >> y2;
			if(x1>x2) swap(x1,x2);
			if(y1>y2) swap(y1,y2);
			for(int x=x1;x<=x2;++x)
				for(int y=y1;y<=y2;++y)
					table[y][x]=1;
			if(x1 < minx) minx=x1;
			if(maxx < x2) maxx=x2;
			if(y1 < miny) miny=y1;
			if(maxy < y2) maxy=y2;
		}

		while(count > 0) {
			count = 0;
			++result;
			int minx_ = 100, miny_ = 100, maxx_ = 0, maxy_ = 0;
			for(int x=minx;x<=maxx;++x) {
				for(int y=miny;y<=maxy;++y) {
					if(table[y][x]) {
						if(!table[y-1][x] && !table[y][x-1]) {
							table_[y][x] = 0;
						} else {
							table_[y][x] = 1;
							if(x < minx_) minx_=x;
							if(maxx_ < x) maxx_=x;
							if(y < miny_) miny_=y;
							if(maxy_ < y) maxy_=y;
							++count;
						}
					} else {
						if(table[y-1][x] && table[y][x-1]) {
							table_[y][x] = 1;
							if(x < minx_) minx_=x;
							if(maxx_ < x) maxx_=x;
							if(y < miny_) miny_=y;
							if(maxy_ < y) maxy_=y;
							++count;
						} else {
							table_[y][x] = 0;
						}
					}
				}
			}
			swap(table_, table);
		}

		cout << "Case #" << idx_problem+1 << ": " << result << endl;
	}
	
	return 0;
}
