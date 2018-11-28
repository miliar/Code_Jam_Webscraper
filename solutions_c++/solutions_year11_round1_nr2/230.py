
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <cassert>

using namespace std;

bool has_letter( const string& w, char c )
{
	return find( w.begin(), w.end(), c ) != w.end();
}

void get_words_with_letter_and_no_letter( const list< string >& la, char c, list< string >& ly, list< string >& ln )
{
	ly.clear();
	ln.clear();
	for ( list<string>::const_iterator it = la.begin(); it != la.end(); ++it ) {
		if ( has_letter( *it, c ) )
			ly.push_back( *it );
		else
			ln.push_back( *it );
	}
}
/*
void get_words_with_no_letter( const list< string >& la, char c, list< string >& lb )
{
	lb.clear();
	for ( list<string>::const_iterator it = la.begin(); it != la.end(); ++it ) {
		if ( ! has_letter( *it, c ) )
			lb.push_back( *it );
	}
}*/

void get_letter_poss( const string& w, char c, vector<int>& p )
{
	p.clear();
	for ( int i = 0; i < (int)w.length(); ++i )
		if ( w[i] == c )
			p.push_back( i );
}

void filter_words_by_pos( const list<string>& la, const string& w, char c, list<string>& lb )
{
	vector<int> p1, p2;
	get_letter_poss( w, c, p2 );
	lb.clear();
	for ( list<string>::const_iterator it = la.begin(); it != la.end(); ++it ) {
		get_letter_poss( *it, c, p1 );
		if ( p1 == p2 )
			lb.push_back( *it );
	}
}

int points( const string& w, const vector< string >& ws, const string& L )
{
	list< string > wl, wly, wln;
	int pt = 0;
	copy( ws.begin(), ws.end(), back_inserter( wl ) );
	for ( int i = 0; i < (int)L.length(); ++i ) {
		get_words_with_letter_and_no_letter( wl, L[i], wly, wln );
		if ( wly.size() == 0 )
			continue;
		char ch = L[i];
		if ( has_letter( w, ch ) ) {
			filter_words_by_pos( wly, w, ch, wl );
		}
		else {
			++pt;
			wl.swap( wln );
		}
	}
	return pt;
}

int main()
{
	int T;
	cin >> T;
	for ( int tc = 1; tc <= T; ++tc ) {
		int n, m;
		cin >> n >> m;
		vector< string > D, L;
		D.resize( n );
		L.resize( m );
		vector< vector< string > > wsl;
		cerr << "Test " << tc << ": n = " << n << ", m = " << m << endl;
		for ( int i = 0; i < n; ++i ) {
			cin >> D[i];
			if ( D[i].length() >= wsl.size() ) {
				wsl.resize( D[i].length() + 1 );
			}
			wsl[ D[i].length() ].push_back( D[i] );
		}
		for ( int i = 0; i < m; ++i )
			cin >> L[i];
		cout << "Case #" << tc << ":";
		for ( int j = 0; j < m; ++j ) {
			int s = 0, si = 0;
			for ( int i = 0; i < n; ++i ) {
				assert( D[i].length() < wsl.size() );
				int ts = points( D[i], wsl[ D[i].length() ], L[j] );
				if ( ts > s ) {
					s = ts;
					si = i;
				}
			}
			cout << " " << D[si];
		}
		cout << endl;
	}
	return 0;
}
