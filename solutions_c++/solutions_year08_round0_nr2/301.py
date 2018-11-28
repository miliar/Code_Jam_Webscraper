#include <vector>
#include <set>
#include <string>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <iostream>
#include <cassert>
#include <cctype>
#include <cmath>
#include <map>
#include <deque>
#include <queue>
#include <algorithm>
#include <functional>

using namespace std;

#define DEP_A 3
#define ARR_A 1
#define DEP_B 4
#define ARR_B 2

typedef pair<int,int> PI;
typedef priority_queue<PI,vector<PI>,greater_equal<PI> > pq_t;

int turnaround, na, nb;
vector<PI> tripa;
vector<PI> tripb;
vector<PI> action;

int test( int ma, int mb ) {
	if( na == 0 && nb == 0 ) return 1;
	
	action.clear();
	for( int i = 0; i < na; ++i ) {
		action.push_back( PI( tripa[i].first, DEP_A ) );
		action.push_back( PI( tripa[i].second + turnaround, ARR_B ) );
	}
	for( int i = 0; i < nb; ++i ) {
		action.push_back( PI( tripb[i].first, DEP_B ) );
		action.push_back( PI( tripb[i].second + turnaround, ARR_A ) );
	}
	
	sort( action.begin(), action.end() );
	for( int i = 0; i < (int)action.size(); ++i ) {
		PI p = action[i];
		
		switch( p.second ) {
		case DEP_A:
			if( ma <= 0 ) return 0;
			--ma;
			break;
		case DEP_B:
			if( mb <= 0 ) return 0;
			--mb;
			break;
		case ARR_A:
			++ma;
			break;
		case ARR_B:
			++mb;
			break;
		}
	}
	
	return 1;
}

int conv( const string& s ) {
	int h, m;
	
	sscanf( s.c_str(), "%d:%d", &h, &m );
	return h*60+m;
}

int main() {
	int cases;
	cin >> cases;
	
	for( int caseid = 1; caseid <= cases; ++caseid ) {
		tripa.clear();
		tripb.clear();
	
		cin >> turnaround >> na >> nb;
		for( int i = 0; i < na; ++i ) {
			string s1, s2;
			cin >> s1 >> s2;
			int t1 = conv( s1 );
			int t2 = conv( s2 );
			assert( t1 != t2 );
			if( t1 > t2 ) {
				swap( t1, t2 );
			}
			tripa.push_back( PI(t1,t2) );
		}
		for( int i = 0; i < nb; ++i ) {
			string s1, s2;
			cin >> s1 >> s2;
			int t1 = conv( s1 );
			int t2 = conv( s2 );
			assert( t1 != t2 );
			if( t1 > t2 ) {
				swap( t1, t2 );
			}
			tripb.push_back( PI(t1,t2) );
		}
		
		int u = 0;
		int v = na+nb-1;
		int besta = na;
		int bestb = nb;
		while( u <= v ) {
			int w = (u+v)/2;
			int found = 0;
			for( int i = 0; i <= w; ++i ) {
				if( test( i, w-i ) ) {
					found = 1;
					if( w < besta+bestb ) {
						besta = i;
						bestb = w-i;
					}
					break;
				}
			}
			if( found ) {
				v = w-1;
			} else {
				u = w+1;
			}
		}
		cout << "Case #" << caseid << ": " << besta << ' ' << bestb << endl;
	}
	return 0;
}

