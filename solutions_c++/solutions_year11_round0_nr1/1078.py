#include<iostream>

using namespace std;
const int MAXN = 1111;
char c[ MAXN ];
int pos[ MAXN ];

void move( int &cur, int pos )
{
	if( cur < pos )
		cur++;
	if( cur > pos )
		cur--;
}

int main()
{
	freopen( "input.txt","rt", stdin );
	freopen( "output.txt","wt", stdout );

	int tests;
	cin >> tests;
	for( int t = 1; t <= tests; t++ )
		{
			int n;
			cin >> n;
			memset( c, 0, sizeof( c ) );
			memset( pos, 0, sizeof( pos ) );
			for( int i = 0; i < n; i++  )
				cin >> c[ i ] >> pos[ i ];

			int pO = 0, pB = 0;
			int posO = 1, posB = 1;
			int res = 0;

			while( pO != n || pB != n )
			{
			res++;
			while( pO != n && c[ pO ] != 'O' )
				pO++;

			while( pB != n && c[ pB ] != 'B' )
				pB++;

			if( pO < pB || pB == n )
				{
				if( posO != pos[ pO ]  )
					move( posO, pos[ pO ] );
				else
					pO++;

				if( pB != n && posB != pos[ pB ] )
					move( posB, pos[ pB ] );
				}

			if( pB < pO ||  pO == n )
				{
				if( posB != pos[ pB ]  )
					move( posB, pos[ pB ] );
				else
					pB++;

				if( pO != n && posO != pos[ pO ] )
					move( posO, pos[ pO ] );

				}
			}

			cout << "Case #" << t << ": " << res << endl;
		}

	return 0;
}