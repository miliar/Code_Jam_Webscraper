#include <iostream>
#include <vector>
using namespace std;

void main2() {
	int n,t,move = 0, opos = 1, bpos = 1, ox = 0, bx = 0, x = 1;
	vector<int> o1, o2, b1, b2;
	bool flag;
	char c;
	cin >> n;
	for ( int i = 0; i < n; i++ ) {
		cin >> c;
		if ( c == 'O' ) {
			cin >> t;
			o1.push_back( t );
			o2.push_back( i );
		} else {
			cin >> t;
			b1.push_back( t );
			b2.push_back( i );
		}
	}

	while ( ox + bx < n ) {
		flag = 1;
		if( ox < o1.size() ) {
		if( opos < o1[ox] ) {
			opos++;
		} else if( opos > o1[ox] ) {
			opos--;
		} else if( o2[ox] == x - 1 ){
			x++;
			ox++;
			flag = 0;
		}
		}
		if( bx < b1.size() ) {
		if( bpos < b1[bx] ) {
			bpos++;
		} else if( bpos > b1[bx] ) {
			bpos--;
		} else if( b2[bx] == x - 1 && flag ){
			x++;
			bx++;
		}
		}
		move++;
	}

	cout << move << endl;
}

int main() {
	int T;
	cin >> T;
	for( int i = 0; i < T; i++ ) {
		cout << "Case #" << i + 1 << ": ";
		main2();
	}
	return 0;
}
