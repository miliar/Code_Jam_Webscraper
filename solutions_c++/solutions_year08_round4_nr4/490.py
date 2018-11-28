#include <iostream>
#include <iterator>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

#include <cmath>

//#include "lib.hpp"

typedef unsigned long long ULL;
typedef long long LL;

using namespace std;

int main(void)
{
	int n;
	cin >> n;
	for(int nn = 0; nn < n; ++nn) {
		int result = 500000;
		int k;
		string s;

		cin >> k;
		cin.ignore(500, '\n');
		getline(cin, s);

		string::iterator send = s.begin();
		while('a' <= *send && *send <= 'z') ++send;

		vector<int> v(k);
		for(int i=0;i<k;++i) v[i]=i;

		do {
			string s2; s2.resize(send - s.begin());
			for(int i = 0; i < s2.size()/k; i++) {
				for(int j = 0; j < k; ++j ) {
					s2[i*k+j] = s[i*k+v[j]];
				}
			}
//cerr << s2 << endl;
			char c = ' '; int t = 0;
			for(string::iterator si = s2.begin(); si != s2.end(); ++si) {
				if(*si != c) ++t;
				c = *si;
			}
			if(result > t) result = t;
		} while(next_permutation(v.begin(), v.end()));

		cout << "Case #" << nn+1 << ": " << result << endl;
	}
	
	return 0;
}
