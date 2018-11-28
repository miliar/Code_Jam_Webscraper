#include <iostream>
using namespace std;
int main ( int argc, char * argv[] )
{
	const int px = 0, po = 1, pt = 2, horiz = 0, vert = 1;
#define index(x) ( x == 'X' ? px : x == 'O' ? po : pt )
	int n;
	cin >> n;
	for ( int tc = 1 ; tc <= n ; tc++ )
	{
		int num[2][3][5] = {{{0}}};
		char b[4][4];
		int complete = 1;
		for ( int i = 0 ; i < 4 ; i ++ )
		{
			for ( int j = 0 ; j < 4 ; j++ )
			{
				while ( cin >> b[i][j] , b[i][j] == '\n' || b[i][j] == '\r' )
					;
				if ( b[i][j] == '.' )
					complete = 0;
				else
				{
					num[horiz][index(b[i][j])][i]++;
					num[vert][index(b[i][j])][j]++;
					if ( i == j )
					{
						num[horiz][index(b[i][j])][4]++;
					}
					if ( i == 3 - j )
					{
						num[vert][index(b[i][j])][4]++;
					}
				}
			}
		}
		char won = 0;
		for ( int i = 0 ; i < 5 && ! won ; i++ )
		{
			for ( int dir = 0 ; dir < 2 ; dir ++ )
			{
//				cout << "num[ " << dir << " ][ " << 'X' << " ][ " << i << " ] = " << num[dir][index('X')][i] << endl;
//				cout << "num[ " << dir << " ][ " << 'T' << " ][ " << i << " ] = " << num[dir][index('T')][i] << endl;
//				cout << "num[ " << dir << " ][ " << 'O' << " ][ " << i << " ] = " << num[dir][index('O')][i] << endl;
				if ( num[dir][index('X')][i] + num[dir][index('T')][i] == 4 )
				{
					won = 'X';
					break;
				}
				else if ( num[dir][index('O')][i] + num[dir][index('T')][i] == 4 )
				{
					won = 'O';
					break;
				}

			}
		}
		cout << "Case #" << tc << ": ";
		if ( won )
		{
			cout << won << " won";
		}
		else if ( complete )
		{
			cout << "Draw";
		}
		else
			cout << "Game has not completed";
		cout << endl;
	}
}
		

