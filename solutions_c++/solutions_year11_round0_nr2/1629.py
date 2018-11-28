
#include <iostream>
#include <set>
#include <map>
#include <utility>
#include <string>
#include <algorithm>
#include <iterator>

using namespace std;

typedef pair< char, char > p_t;
typedef map< p_t, char > c_t;
typedef set< p_t > d_t;

void check_multiset( const std::string& r, const multiset<char>& m )
{
	multiset<char> m2;
	for (size_t i = 0; i < r.length(); ++i)
		m2.insert( r[i] );
	if ( m != m2 )
		throw 0;
}

string solve( const c_t& c, const d_t& d, const string& s )
{
	multiset<char> m;
	string r;
	for ( int i = 0; i < (int)s.length(); ++i ) {
		char ch = s[i];
		if ( ! r.empty() ) {
			c_t::const_iterator it;
			it = c.find( p_t( ch, r[ r.length() - 1 ] ) );
			if ( it != c.end() ) {
				m.erase( m.find( r[ r.length() - 1 ] ) );
				r[ r.length() - 1 ] = it->second;
				m.insert( r[ r.length() - 1 ] );
			}
			else {
				char chp;
				for ( chp = 'A'; chp <= 'Z'; ++chp )
					if ( d.count( p_t( ch, chp ) ) > 0 && m.count( chp ) > 0 )
						break;
				if ( chp > 'Z' ) {
					r.push_back( ch );
					m.insert( ch );
				}
				else {
					r.clear();
					m.clear();
				}
			}
			check_multiset( r, m );
		}
		else {
			r.push_back( ch );
			m.insert( ch );
		}
	}
	return r;
}

int main()
{
	int TC;
	cin >> TC;
	for ( int tc = 1; tc <= TC; ++tc ) {
		int C, D, N;
		cin >> C;
		c_t c;
		for ( int i = 0; i < C; ++i ) {
			string s;
			cin >> s;
			if ( s.length() != 3 ) throw 0;
			if ( c.count( p_t( s[0], s[1] ) ) > 0 ) throw 0;
			c[ p_t( s[0], s[1] ) ] = s[2];
			if ( s[0] != s[1] )
				c[ p_t( s[1], s[0] ) ] = s[2];
		}
		cin >> D;
		d_t d;
		for ( int i = 0; i < D; ++i ) {
			string s;
			cin >> s;
			if ( s.length() != 2 ) throw 0;
			if ( d.count( p_t( s[0], s[1] ) ) > 0 ) throw 0;
			d.insert( p_t( s[0], s[1] ) );
			if ( s[0] != s[1] )
				d.insert( p_t( s[1], s[0] ) );
		}
		cin >> N;
		string s;
		cin >> s;
		if ( s.length() != N ) throw 0;
		cerr << "test " << tc << " - " << C << " " << D << " " << N << endl;
		string r = solve( c, d, s );
		cout << "Case #" << tc << ": [";
		for ( int i = 0; i < (int)r.length(); ++i ) {
			cout << r[i];
			if ( i < ((int)r.length()) - 1 )
				cout << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}
