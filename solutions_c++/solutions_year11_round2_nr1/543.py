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
#include <boost/math/common_factor.hpp>

using namespace std;
using boost::lexical_cast;
using boost::math::gcd;
using boost::math::lcm;

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

template<class T>
class Memo {};
template<class RT,class... Args>
class Memo<RT(Args...)> {
public:
	Memo(function<RT(Args...)> f):_f(f),_t() {}
	Memo(const Memo &m):_f(m._f),_t(m._t) {}
	Memo(Memo &&m) {
		m.swap(*this);
	}
	RT operator()(const Args... args) {
		tuple<Args...> k{args...};
		auto i=_t.find(k);
		if(i==_t.end()) {
			RT rv=_f(args...);
			_t[k]=rv;
			return rv;
		} else {
			return i->second;
		}
	}
	Memo &operator=(const Memo &m) {
		Memo(m).swap(*this);
		return *this;
	}
	Memo &operator=(Memo &&m) {
		m.swap(*this);
		return *this;
	}
	void swap(Memo &m) {
		std::swap(_f,m._f);
		std::swap(_t,m._t);
	}
private:
	function<RT(Args...)> _f;
	map<tuple<Args...>,RT> _t;
};



int main() {
	int _NCases; cin >> _NCases;
	for(int _Case=1;_Case<=_NCases;++_Case) {
		cout << "Case #" << _Case << ":" << endl; cout.flush();
		size_t N; cin >> N;
		vector<string> A(N); for(string &s:A) cin >> s;
		vector<double> wins(N), games(N);
		vector<double> WP(N), OWP(N), OOWP(N);
		for(size_t i=0;i<N;i++) {
			double nmr=0.0,dnr=0.0;
			for(size_t j=0;j<N;j++) {
				if(A[i][j]=='1') nmr++;
				if(A[i][j]!='.') dnr++;
			}
			WP[i]=nmr/dnr;
			wins[i]=nmr;
			games[i]=dnr;
		}
		for(size_t i=0;i<N;i++) {
			double nmr=0.0,dnr=0.0;
			for(size_t j=0;j<N;j++) {
				if(A[i][j]=='1') {
					nmr+=wins[j]/(games[j]-1);
					dnr++;
				} else if(A[i][j]=='0') {
					nmr+=(wins[j]-1)/(games[j]-1);
					dnr++;
				}
			}
			OWP[i]=nmr/dnr;
		}
		for(size_t i=0;i<N;i++) {
			double nmr=0.0,dnr=0.0;
			for(size_t j=0;j<N;j++)
				if(A[i][j]!='.' && i!=j) {
					nmr+=OWP[j];
					dnr++;
				}
			OOWP[i]=nmr/dnr;
		}
		for(size_t i=0;i<N;i++) {
			cout << setprecision(10) << (0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i]) << endl;
		}
	}
	return 0;
}