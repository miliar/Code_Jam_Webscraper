#include <iostream>
#include <sstream>
#include <boost/algorithm/string/trim.hpp>
#include <algorithm>

using namespace std;
using namespace boost;

string trim_leading_zero_copy(const string& s) {
	string::const_iterator f = s.begin();
	while(f != s.end()) {
		if(*f != '0') { break; }
		++f;
	}
	return string(f, s.end());
}

bool _solve(string &a) {
	for(string::reverse_iterator ri = a.rbegin(); ri != a.rend(); ++ri) {
		char ci = *ri;
		string::iterator i((ri+1).base());

		char p = '9' + 1;
		string::iterator j = a.end();
		for(string::iterator k = i + 1; k != a.end(); ++k) {
			if(*k <= ci) { continue; }
			if(*k < p) {
				j = k;
				p = *k;
			}
		}
		if(j == a.end()) { continue; }

		// -- i -- j --
		// target found
		swap(*i, *j);
		sort(i + 1, a.end());
		a = trim_leading_zero_copy(a);
		return true;
	}
	if(false) 
	for(string::reverse_iterator i = a.rbegin(); i != a.rend(); ++i) {
		for(string::reverse_iterator j = i + 1; j != a.rend(); ++j) {
			if(*i > *j) {
				// -- j -- i --
				// target found
				swap(*i, *j);
				string::iterator jj((j+1).base());
				sort(jj + 1, a.end());
				a = trim_leading_zero_copy(a);
				return true;
			}
		}
	}
	return false;
}

string solve(const string &_s) {
	string ret;
	ret = _s; if(_solve(ret)) { return ret; }
	ret = string("0") + _s; if (_solve(ret)) { return ret; }
	assert(false && "applying algorithm failed.");
	return "";
}

int _main(void) {
	string s;
	cin >> s;
	while(true) {
		cout << s << endl;
		char t;
		cin >> t;
		s = solve(s);
	}
	return 0;
}


int main(void) {
	int T = 0;
	if(!(cin >> T)) {
		assert(false && "parse");
		return -1;
	}

	string s;
	getline(cin, s);
	assert(s.empty());

	for(int i = 0; i < T; ++i) {
		string s;
		getline(cin, s);
		trim(s);
		cout << "Case #" << (1+i) << ": " << solve(s) << "\n";
	}
	return 0;
}
