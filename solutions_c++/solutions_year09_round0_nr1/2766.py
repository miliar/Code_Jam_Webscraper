#include <boost/regex.hpp>

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	int L, D, N;
	cin >> L >> D >> N;
	
	vector<string> words;
	for ( int i = 0 ; i < D; i++ ) {
		string s;
		cin >> s;
		words.push_back( s );
	}
	
	for ( int tcase = 0; tcase < N; tcase += 1 ) {
		string s;
		cin >> s;
		
		// construct the regex
		for ( unsigned i = 0; i < s.size(); i += 1 ) 
			if ( s[i] == '(' )
				s[i] = '[';
			else if ( s[i] == ')' )
				s[i] = ']';
		boost::regex r(s);
		
		// test
		int total = 0;
		for ( unsigned i = 0; i < words.size(); i += 1 ) {
			if ( regex_match( words[i], r ) )
				total++;
		}
		
		cout << "Case #" << (tcase+1) << ": " << total << endl;
	}
	
	return 0;
}
