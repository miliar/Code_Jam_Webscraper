#include <fstream>
#include <string>
#include <list>
#include <map>
#include <set>
#include <vector>
#include <iostream>

using namespace std;

int test_word( list< string > &dict, string &test, string word ) {
	for( list< string >::iterator it=dict.begin(); it!=dict.end(); ) {
		if( it->length() != word.length() ) {
			it = dict.erase( it );
			continue;
		}
		++it;
	}

	int res = 0;
	if( dict.size() == 1 ) {
		return 0;
	}
	for( string::const_iterator c=test.begin(); c!=test.end(); ++c ) {
		// seek if word can have this letter
		bool found = false;
		for( list< string >::iterator it=dict.begin(); it!=dict.end(); ) {
			if( it->find( *c ) != string::npos ) {
				found = true;
				break;
			}
			++it;
		}
		if( !found ) {
			continue;
		}

		size_t pos = word.find( *c );
		if( string::npos == pos ) {
			// no match, remove words with this letter
			++res;
			for( list< string >::iterator it=dict.begin(); it!=dict.end(); ) {
				if( string::npos != it->find( *c ) ) {
					it = dict.erase( it );
					continue;
				}
				++it;
			}
		} else {
			size_t oldpos = 0;
			// match, remove words without this letter on all found positions or with it on other
			do {
				for( list< string >::iterator it=dict.begin(); it!=dict.end(); ) {
					if( pos != it->find( *c, oldpos ) ) {
						it = dict.erase( it );
						continue;
					}
					++it;
				}
				if( pos == string::npos ) {
					break;
				}
				oldpos = pos + 1;
				pos = word.find( *c, pos+1 );
			} while( true );
		}
		if( dict.size() <= 1 ) {
			break;
		}
	}
	return res;
}

string do_case( const vector< string > &dict , string &test ) {
	cout << "-------- Testing " << test << endl;
	string res = "";
	int best = -1;

	for( size_t i=0; i<dict.size(); ++i ) {
		int val = test_word( list<string>(dict.begin(),dict.end()), test, dict[i] );
		cout << dict[i] << ": " << val << endl;
		if( val > best ) {
			best = val;
			res = dict[i];
		}
	}

	return res;
}

int main() {
	ifstream in( "b_in.txt" );
	ofstream out( "b_out.txt" );

	size_t cases_count;
	in >> cases_count;

	for( size_t i=1; i<=cases_count; ++i ) {
		size_t n, m;
		in >> n >> m;

		vector< string > dict;
		vector< string > tests;

		for( size_t j=0; j<n; ++j ) {
			string str;
			in >> str;
			dict.push_back( str );
		}

		out << "Case #" << i << ":";
		for( size_t j=0; j<m; ++j ) {
			string str;
			in >> str;
			out << " " << do_case( dict, str );
		}

		out << endl;
	}

	return 0;
}
