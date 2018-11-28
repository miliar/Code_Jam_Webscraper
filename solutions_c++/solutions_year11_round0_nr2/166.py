// C++0x (GCC 4.6.1 20110325 (prerelease), -std=c++0x option)
#include <iostream>
#include <iomanip>
#include <vector>
#include <array>
#include <unordered_map>
#include <unordered_set>
#include <tuple>
#include <functional>
#include <cassert>
#include <sstream>

using namespace std;

template<class T>
string join(const T &t,const string &delim) {
	stringstream rv(stringstream::out);
	bool first=true;
	for(auto x:t) {
		if(first) {
			rv << x;
			first = false;
		} else {
			rv << delim << x;
		}
	}
	return rv.str();
}

int main() {
	int T; cin >> T;
	for(int K=1;K<=T;K++) {
		int C; cin >> C;
		vector<string> combinations(C);
		for(int i=0;i<C;i++)
			cin >> combinations[i];
		int D; cin >> D;
		vector<string> destroy(D);
		for(int i=0;i<D;i++)
			cin >> destroy[i];
		int N; cin >> N;
		string elts; cin >> elts;
		
		vector<char> s;
		
		auto transform = [&](char c,char d) -> char {
			for(string cc:combinations)
				if( (cc[0]==c && cc[1]==d) || (cc[0]==d && cc[1]==c) )
					return cc[2];
			return 0;
		};
		
		auto willDestroy = [&](char t) {
			for(char c:s)
				for(string dd:destroy)
					if( (dd[0]==c && dd[1]==t) || (dd[0]==t && dd[1]==c) )
						return true;
			return false;
		};
		
		for(char c:elts) {
			char t;
			while(s.size()>0 && (t=transform(s.back(),c)) ) {
				s.pop_back();
				c=t;
			}
			if(willDestroy(c))
				s.clear();
			else
				s.push_back(c);
		}
		
		cout << "Case #" << K << ": [" << join(s,", ") << "]" << endl;
	}
	return 0;
}