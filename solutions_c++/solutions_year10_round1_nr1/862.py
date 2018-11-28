#include <iostream>
#include <sstream>

#include <iterator>

#include <algorithm>
#include <numeric>
#include <utility>

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

#define foreach         BOOST_FOREACH
#define reverse_foreach BOOST_REVERSE_FOREACH

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

typedef vector<string> Board;

int main(void)
{
	int n;
	cin >> n;
	for(int nn = 0; nn < n; ++nn) {
		int n, k;
		cin >> n >> k; cin.ignore();
		Board bd(n);
		for(int i=0;i<n;++i) {
			getline(cin, bd[i]);
		}

		for(int i=0;i<n;++i) {
			int pos = n-1;
			for(int j=n-1;j>=0;--j) {
				if(bd[i][j] != '.') {
					if(pos != j) {
						bd[i][pos--] = bd[i][j];
						bd[i][j] = '.';
					} else pos--;
				}
			}
		}

		bool rr = false, bb = false;
		//H
		foreach(string &s, bd) {
			int r = 0, b = 0;
			char c = '.';
			foreach(char ch, s) {
				if(c == ch) {
					if(c == 'R') {
						++r;
						if(r >= k) rr = true;
					} else if(c == 'B') {
						++b;
						if(b >= k) bb = true;
					}
				} else {
					if(ch == 'R') r = 1;
					else if(ch == 'B') b = 1;
				}
				c = ch;
				if(rr && bb) break;
			}
		}

		//V
		for(int i=0;i<n;++i) {
			int r = 0, b = 0;
			char c = '.';
			for(int j=0;j<n;++j) {
				char ch = bd[j][i];
				if(c == ch) {
					if(c == 'R') {
						++r;
						if(r >= k) rr = true;
					} else if(c == 'B') {
						++b;
						if(b >= k) bb = true;
					}
				} else {
					if(ch == 'R') r = 1;
					else if(ch == 'B') b = 1;
				}
				c = ch;
				if(rr && bb) break;
			}
		}

		// /
		for(int i=k-1;i<n;++i) {
			int r = 0, b = 0;
			char c = '.';
			for(int j=0;j<=i;++j) {
				char ch = bd[i-j][j];
				if(c == ch) {
					if(c == 'R') {
						++r;
						if(r >= k) rr = true;
					} else if(c == 'B') {
						++b;
						if(b >= k) bb = true;
					}
				} else {
					if(ch == 'R') r = 1;
					else if(ch == 'B') b = 1;
				}
				c = ch;
				if(rr && bb) break;
			}
		}
		for(int i=k-1;i<n;++i) {
			int r = 0, b = 0;
			char c = '.';
			for(int j=0;j<=i;++j) {
				char ch = bd[n-j-1][n-i+j-1];
				if(c == ch) {
					if(c == 'R') {
						++r;
						if(r >= k) rr = true;
					} else if(c == 'B') {
						++b;
						if(b >= k) bb = true;
					}
				} else {
					if(ch == 'R') r = 1;
					else if(ch == 'B') b = 1;
				}
				c = ch;
				if(rr && bb) break;
			}
		}

		// 
		for(int i=k-1;i<n;++i) {
			int r = 0, b = 0;
			char c = '.';
			for(int j=0;j<=i;++j) {
				char ch = bd[n-i-1+j][j];
				if(c == ch) {
					if(c == 'R') {
						++r;
						if(r >= k) rr = true;
					} else if(c == 'B') {
						++b;
						if(b >= k) bb = true;
					}
				} else {
					if(ch == 'R') r = 1;
					else if(ch == 'B') b = 1;
				}
				c = ch;
				if(rr && bb) break;
			}
		}
		for(int i=k-1;i<n;++i) {
			int r = 0, b = 0;
			char c = '.';
			for(int j=0;j<=i;++j) {
				char ch = bd[j][n-i+j-1];
				if(c == ch) {
					if(c == 'R') {
						++r;
						if(r >= k) rr = true;
					} else if(c == 'B') {
						++b;
						if(b >= k) bb = true;
					}
				} else {
					if(ch == 'R') r = 1;
					else if(ch == 'B') b = 1;
				}
				c = ch;
				if(rr && bb) break;
			}
		}


		const char *result = rr&&bb ? "Both" : rr ? "Red" : bb ? "Blue" : "Neither";
		cout << "Case #" << nn+1 << ": " << result << endl;
	}
	
	return 0;
}
