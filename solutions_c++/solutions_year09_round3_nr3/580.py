#include <iostream>
#include <iterator>
#include <algorithm>
#include <string>
#include <vector>
#include <utility>
#include <map>
#include <sstream>

#include <cmath>

// Boost library can be retrieved from http://www.boost.org/
// I uses 1.40.0

#include <boost/foreach.hpp>
#include <boost/array.hpp>

#define foreach         BOOST_FOREACH
#define reverse_foreach BOOST_REVERSE_FOREACH

typedef unsigned long long ULL;
typedef long long LL;
typedef unsigned long UL;
typedef unsigned int UI;
typedef unsigned char UC;

using namespace std;
using namespace boost;

int main(void)
{
	int n;
	cin >> n;
	for(int nn = 0; nn < n; ++nn) {

		int p, q;
		cin >> p >> q;
		vector<int> v;
		for(int i=0;i<q;++i) {
			int j;
			cin >> j;
			v.push_back(j-1);
		}
		sort(v.begin(), v.end());
		ULL tres = 10000000;
		do {
			ULL t = 0;
			vector<int> w(p);
			foreach(int &i,w) { i = 1; }
			foreach(int i,v) {
				w[i] = 0;
				int j = i-1;
				while(j>=0 && w[j]) {
					++t;
					--j;
				}
				j = i+1;
				while(j<p && w[j]) {
					++t;
					++j;
				}
			}
			if(tres > t) tres = t;
		} while(next_permutation(v.begin(), v.end()));

		cout << "Case #" << nn+1 << ": " << tres << endl;
	}
	
	return 0;
}
