#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <vector>
#include <string>
#include <utility>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <ctype.h>
#include <sstream>
#include <bitset>
#include <deque>

using namespace std;

int acercar ( int ini , int dest , int dist ) {
	if ( abs ( ini - dest ) <= dist ) return dest;
	return ( ini < dest ? ini+dist : ini-dist );
}

int solve ( deque<pair<int,int> >& a, deque<pair<int,int> >& b , int &cura, int &curb)
{
	if ( a.empty() ) {
		int dist = abs ( curb - b.front().second ) + 1;
		curb = b.front().second;
		b.pop_front();
		return dist;
	}
	
	if ( b.empty() ) {
		int dist = abs ( cura - a.front().second ) + 1;
		cura = a.front().second;
		a.pop_front();
		return dist;
	}
	
	if ( a.front().first > b.front().first )
		return solve ( b , a , curb , cura );
	
	int dist = abs ( cura - a.front().second );
	cura = a.front().second;
	curb = acercar ( curb , b.front().second, dist+1 );
	a.pop_front();
	
	return dist+1;
}

int main ()
{
	//freopen ( "A.in", "r" , stdin );
	//freopen ( "A.out", "w" , stdout );
	
	int ncases;
	cin >> ncases;
	
	for ( int i = 0; i < ncases; ++i )
	{
		int ans = 0;
		deque <pair<int,int> > a , b;
		int cura = 1, curb = 1;
		
		int n, idx;
		string str;
		cin >> n;
		for ( int j = 0; j < n; ++j ) {
			cin >> str >> idx;
			if ( str == "B" ) b.push_back ( make_pair ( j , idx ) );
			else a.push_back ( make_pair ( j , idx ) );
		}
		
		while ( true ) {
			if ( a.empty() && b.empty() ) break;
			ans += solve ( a , b , cura , curb );
		}
		
		printf ( "Case #%d: %d\n", i+1,  ans );
	}
	
	return 0;
}
