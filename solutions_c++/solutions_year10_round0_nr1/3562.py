#include <iostream>
using namespace std;

int main(){
	int cadeia, vezes;
	unsigned long long snaps, minimo;

	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );

	cin >> vezes;
	for( int caso = 1; caso <= vezes; ++caso ){
		cin >> cadeia >> snaps;
		minimo = ( 1 << cadeia ) - 1;

		cout << "Case #" << caso << ": ";
		if( snaps < minimo )
			cout << "OFF" << endl;
		else if( snaps == minimo )
			cout << "ON" << endl;
		else{
			snaps -= minimo;
			if( snaps % ( 1 << cadeia ) == 0 )
				cout << "ON" << endl;
			else
				cout << "OFF" << endl;
		}
	}
}
