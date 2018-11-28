#include <iostream>
#include <set>
using namespace std;
const int mn = 110 , mq = 1101;
string names[ mn ] , query [ mq ];
int n , q ;
int solve ( int st ) {
	int res = 0;
	set < string > S;
	for ( int i=st;i<q;i++ ) {
		if ( S.count ( query[i] ) ) continue;
		if ( S.size() == n - 1  ) {
			res = 1 + solve ( i );
			break;
		} else
		S.insert ( query[i] );
	}
	return res;
}
char buff[ 110 ];
int main() {
	int t;
	scanf ( "%d" ,  &t );
	for ( int kase = 1 ; kase <= t ; kase ++ ) {
		scanf ( "%d" , &n );
		getchar ();
		for ( int i=0;i<n;i++ ) {
			gets ( buff );
			names[i] = buff;
		}
		scanf ( "%d" , &q );
		getchar ();
		for ( int i=0;i<q;i++ ) {
			gets ( buff );
			query[i] = buff;
		}
		cout << "Case #" << kase <<": " << solve ( 0 ) << endl;
	}
	return 0;
}
