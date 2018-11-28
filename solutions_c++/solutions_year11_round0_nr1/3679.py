#include <iostream>
#include <string>

using namespace std;

int iabs( int a ) { return ( a >= 0 ) ? ( a ) : ( -a ); }
int imax( int a, int b ) { return ( a >= b ) ? a : b; }

int solve()
{
	int ot = 0, bt = 0, op = 1, bp = 1;
	int steps;
	cin >> steps;
	for( int s = 1; s <= steps; ++s )
	{
		string color;
		cin >> color;
		int np;
		cin >> np;
		if( "O" == color )
		{
			ot = 1 + imax( ot + iabs( op - np ), bt );
			op = np;
		}
		else
		{
			bt = 1 + imax( bt + iabs( bp - np ), ot );
			bp = np;
		}
	}
	return imax( bt, ot );
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int tests;
	cin >> tests;
	for( int t = 1; t <= tests; ++t )
		cout << "Case #" << t << ": " << solve() << endl;
	return 0;
}