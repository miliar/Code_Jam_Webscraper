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

inline bool in(int k, int x, int y)
{
	return 0<=x && x<2*k-1 && 0<=y && y<2*k-1;
}

inline pair<int, int> flipX(int x, int y, int pos)
{
	return make_pair(2*pos-x,y);
}

inline pair<int, int> flipY(int x, int y, int pos)
{
	return make_pair(x,2*pos-y);
}

inline bool okX(vector<vector<int> > &table, int k, int x, int y, int pos)
{
	if(table[y][x] < 0) return true;
	pair<int,int> p = flipX(x, y, pos);
	if(!in(k,p.first,p.second)) return true;
	if(table[p.second][p.first]<0) return true;
	return table[p.second][p.first] == table[y][x];
}

inline bool okY(vector<vector<int> > &table, int k, int x, int y, int pos)
{
	if(table[y][x] < 0) return true;
	pair<int,int> p = flipY(x, y, pos);
	if(!in(k,p.first,p.second)) return true;
	if(table[p.second][p.first]<0) return true;
	return table[p.second][p.first] == table[y][x];
}

template<typename T>
inline T absdiff(T t1, T t2)
{
	return t1 > t2 ? t1 - t2 : t2 - t1;
}

inline int res(int n1, int n2)
{
	return n1*n1-n2*n2;
}

int main(void)
{
	int num_problem;
	cin >> num_problem;
	for(int idx_problem = 0; idx_problem < num_problem; ++idx_problem) {

		int k;
		cin >> k;

		int result = res(3*k-2, k);

		vector<vector<int> > table(2*k-1, vector<int>(2*k-1, -1));
		for(int i=0;i<k;++i) {
			for(int j=0;j<=i;++j) {
				cin >> table[i][k-i-1+j*2];
			}
		}
		for(int i=k;i<2*k-1;++i) {
			for(int j=0;j<2*k-1-i;++j) {
				cin >> table[i][i-k+1+j*2];
			}
		}

		for(int i=0;i<2*k-1;++i) {
			for(int j=0;j<2*k-1;++j) {
				bool flag = true;
				for(int x=0;x<2*k-1;++x) {
					for(int y=0;y<2*k-1;++y) {
						if(!okX(table, k, x, y, i) || !okY(table, k, x, y, j)) {
							flag = false;
							break;
						}
					}
					if(!flag) break;
				}
				if(flag) {
					int newk=absdiff(k-1, i)+absdiff(k-1,j)+k;
					if(res(newk, k)<result) result = res(newk,k);
				}
			}
		}

		cout << "Case #" << idx_problem+1 << ": " << result << endl;
	}
	
	return 0;
}
