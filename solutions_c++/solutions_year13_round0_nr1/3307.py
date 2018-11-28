
#include <iostream>

using namespace std;

char* solve( char board[ 4 ][ 4 ] )
{
	char* X = "X won";
	char* Y = "O won";
	char* I = "Game has not completed";
	char* D = "Draw";
	// Rows
	for ( int vr = 0; vr < 4; ++vr ) {
		bool b = true;
		for ( int c = 0; c < 4; ++c )
			b = b && ( board[ vr ][ c ] == 'X' || board[ vr ][ c ] == 'T' );
		if ( b )
			return X;
	}
	for ( int vr = 0; vr < 4; ++vr ) {
		bool b = true;
		for ( int c = 0; c < 4; ++c )
			b = b && ( board[ vr ][ c ] == 'O' || board[ vr ][ c ] == 'T' );
		if ( b )
			return Y;
	}
	// Columns
	for ( int vc = 0; vc < 4; ++vc ) {
		bool b = true;
		for ( int r = 0; r < 4; ++r )
			b = b && ( board[ r ][ vc ] == 'X' || board[ r ][ vc ] == 'T' );
		if ( b )
			return X;
	}
	for ( int vc = 0; vc < 4; ++vc ) {
		bool b = true;
		for ( int r = 0; r < 4; ++r )
			b = b && ( board[ r ][ vc ] == 'O' || board[ r ][ vc ] == 'T' );
		if ( b )
			return Y;
	}
	// Diagonals
	{
		bool b = true;
		for ( int v = 0; v < 4; ++v )
			b = b && ( board[ v ][ v ] == 'X' || board[ v ][ v ] == 'T' );
		if ( b )
			return X;
	}
	{
		bool b = true;
		for ( int v = 0; v < 4; ++v )
			b = b && ( board[ v ][ v ] == 'O' || board[ v ][ v ] == 'T' );
		if ( b )
			return Y;
	}
	{
		bool b = true;
		for ( int v = 0; v < 4; ++v )
			b = b && ( board[ v ][ 3 - v ] == 'X' || board[ v ][ 3 - v ] == 'T' );
		if ( b )
			return X;
	}
	{
		bool b = true;
		for ( int v = 0; v < 4; ++v )
			b = b && ( board[ v ][ 3 - v ] == 'O' || board[ v ][ 3 - v ] == 'T' );
		if ( b )
			return Y;
	}
	// Rest
	for ( int r = 0; r < 4; ++r )
		for ( int c = 0; c < 4; ++c )
			if ( board[ r ][ c ] == '.' )
				return I;
	return D;
}

int main()
{
	int TC;
	cin >> TC;
	for ( int tc = 1; tc <= TC; ++tc ) {
		char board[ 4 ][ 4 ];
		for ( int r = 0; r < 4; ++r )
			for ( int c = 0; c < 4; ++c )
				cin >> board[ r ][ c ];
		cout << "Case #" << tc << ": " << solve( board ) << endl;
	}
	return 0;
}
