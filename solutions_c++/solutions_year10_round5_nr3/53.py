#include <set>
#include <map>
#include <cstdio>
#include <algorithm>
using namespace std;

int n;
map < int , int > mp;
set < pair < int , int > > st;

void read() {
	int x , y;

	st.clear();
	mp.clear();
	
	scanf ( "%d" , &n );
	while ( n -- ) {
		scanf ( "%d%d" , &x , &y );
		mp[x] = y;
		st.insert ( make_pair ( -y , x ) );
	}
}

void solve() {
	set < pair < int , int > >::iterator it;
	int ans = 0;
	int x , y;

	while ( -(*st.begin()).first >= 2 ) {
		++ ans;
		y = -(*st.begin()).first;
		x = (*st.begin()).second;

//		printf ( "%d   %d %d\n" , ans , y , x );
		
		st.erase ( st.begin() );
		
		it = st.lower_bound ( make_pair ( -mp[x - 1] , x - 2 ) );
		if ( (*it).first == -mp[x - 1] && (*it).second == x - 1 )
			st.erase ( *it );

		it = st.lower_bound ( make_pair ( -mp[x + 1] , x ) );
		if ( (*it).first == -mp[x + 1] && (*it).second == x + 1 )
			st.erase ( *it );
		
		mp[x] -= 2;
		mp[x - 1] ++;
		mp[x + 1] ++;
		
		st.insert ( make_pair ( -mp[x] , x ) );
		st.insert ( make_pair ( -mp[x - 1] , x - 1 ) );
		st.insert ( make_pair ( -mp[x + 1] , x + 1 ) );
/*
		for ( set< pair < int , int > >::iterator it = st.begin(); it != st.end(); it++)
			printf ( "%d %d\n" , (*it).first , (*it).second );
		printf ( "\n\n" );
	*/

	}

	printf ( "%d\n" , ans );
}

int main() {
	int i , cases;

	scanf ( "%d" , &cases );
	for (i = 1; i <= cases; i++) {
		printf ( "Case #%d: " , i );
		read();
		solve();

		fflush ( stdout );

	//	return 0;
	}

	return 0;
}
