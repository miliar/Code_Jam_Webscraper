#include <iostream>
#include <iterator>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>

#include <cmath>

//#include <boost/math/common_factor.hpp>
//#include <boost/numeric/interval.hpp>
//#include <boost/dynamic_bitset.hpp>
#include "lib.hpp"

typedef unsigned long long ULL;
typedef long long LL;

using namespace std;
//using namespace boost
// common_factor
//using namespace boost::math;
// interval
//using namespace boost::numeric;
//using namespace boost::numeric::interval_lib::compare::certain;

struct pt
{
	int x, y;
	pt(int x, int y):x(x),y(y) {}
	bool operator<(const pt& p) const { return x < p.x || x == p.x && y < p.y; }
};

int main(void)
{
	int n;
	cin >> n;
	for(int nn = 0; nn < n; ++nn) {
		int result = 0;

		int h, w, r;
		cin >> h >> w >> r;

		map<pt, int> board;
		set<pt> candidate;

		int x,y;
		for(int i=0;i<r;++i) {
			cin >> y >> x;
			board[pt(x,y)]=-1;
		}

		candidate.insert(pt(1,1));
		board[pt(1,1)] = 1;

		while(candidate.size() != 0) {
//cerr << 'T' << endl;
			set<pt> c2;
			for(set<pt>::iterator vi = candidate.begin(); vi != candidate.end();++vi) {
//cerr << vi->x << ',' << vi->y <<endl;
				if(vi->x+2<=w && vi->y+1<=h && board[pt(vi->x+2,vi->y+1)] != -1) {
					board[pt(vi->x+2,vi->y+1)] = (board[pt(vi->x,vi->y)] + board[pt(vi->x+2,vi->y+1)]) % 10007;
					c2.insert(pt(vi->x+2,vi->y+1));
				}
				if(vi->x+1<=w && vi->y+2<=h && board[pt(vi->x+1,vi->y+2)] != -1) {
					board[pt(vi->x+1,vi->y+2)] = (board[pt(vi->x,vi->y)] + board[pt(vi->x+1,vi->y+2)]) % 10007;
					c2.insert(pt(vi->x+1,vi->y+2));
				}
			}
			candidate = c2;
		}

		cout << "Case #" << nn+1 << ": " << (board[pt(w,h)]%10007) << endl;
	}
	
	return 0;
}
