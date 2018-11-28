// C++0x (GCC 4.6.1 20110325 (prerelease), -std=c++0x option, and using boost libraries)
//
// G++ compiler, C++0x standard library: http://gcc.gnu.org/
// Boost library: http://www.boost.org/
//
// Copyright 2011 William Matthews.  All rights reserved.
// By sumitting code to Google Code Jam, rights to use the code are
// granted in accordance with the Google Code Jam Terms and Conditions. 

#include <algorithm>
#include <array>
#include <cassert>
#include <functional>
#include <iostream>
#include <iomanip>
#include <map>
#include <regex>
#include <set>
#include <sstream>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include <boost/lexical_cast.hpp>

using namespace std;
using boost::lexical_cast;

template<class I>
inline string join(const string &delim,I first,I last) {
	ostringstream rv;
	if(first!=last)
		rv << *first++;
	while(first!=last)
		rv << delim << *first++;
	return rv.str();
}
template<class C>
inline string join(const string &delim,const C &t) {
	return join(delim,t.begin(),t.end());
}
template<class F,class I>
inline auto vmap(F f,I first,I last) -> vector<decltype(f(*first))> {
	vector<decltype(f(*first))> rv;
	while(first!=last)
		rv.emplace_back(f(*first++));
	return rv;
}
template<class F,class C>
inline auto vmap(F f,const C &c) -> decltype(vmap(f,c.begin(),c.end())) {
	return vmap(f,c.begin(),c.end());
}

int main() {
	int _NCases; cin >> _NCases;
	for(int _Case=1;_Case<=_NCases;++_Case) {
		cout << "Case #" << _Case << ": "; cout.flush();
		uint64_t N;
		size_t PD,PG;
		cin >> N >> PD >> PG;
		size_t dmin=100/__gcd(PD,100ul);
		if(dmin<=N && ((PG!=100 && PG!=0) || PD==PG))
			cout << "Possible" << endl;
		else
			cout << "Broken" << endl;
	}
	return 0;
}