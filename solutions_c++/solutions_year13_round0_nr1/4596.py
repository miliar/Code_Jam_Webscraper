#include<cstdio>
using namespace std;
int main ()
{
	char x[5][5];
	int y[4][2], z[4][2], wl[2], wp[2];
	
	int t, puste = 0, ans = 0;
	scanf ( "%d", &t );
	
	for ( int k = 1; k <= t; k ++ )
	{
		for ( int a = 0; a < 4; a ++ )
				for ( int c = 0; c < 2; c ++ )
				{
					y[a][c] = 0; z[a][c] = 0;
					wl[c] = 0; wp[c] = 0;
				}
		puste = 0; ans = 0;
		
		printf ( "Case #%d: ", k );
		
		for ( int i = 0; i < 4; i ++ )
		{
			scanf ( " %s", x[i] );
// 			printf ( "u: %c\n", x[i][0] );
			for ( int j = 0; j < 4; j ++ )
			{
				char u = x[i][j];
				if ( u == 'X' or u == 'T' ) 
				{
					y[i][1] ++; //rzad
					z[j][1] ++; //kolumna
					if ( i == j ) wl[1] ++;
					if ( i + j == 3 ) wp[1] ++;
				}
				if ( u == 'O' or u == 'T' ) 
				{
					y[i][0] ++;
					z[j][0] ++;
					if ( i == j ) wl[0] ++;
					if ( i + j == 3 ) wp[0] ++;
				}
				if ( u == '.' ) puste ++;
			}
		}
		for ( int i = 0; i < 4; i ++ )
		{
			if ( z[i][1] == 4 or y[i][1] == 4 or wp[1] == 4 or wl[1] == 4 ) 
			{
				puts ( "X won" );
				ans = 1;
				break;
			}
			if ( z[i][0] == 4 or y[i][0] == 4 or wp[0] == 4 or wl[0] == 4 ) 
			{
				puts ( "O won" );
				ans = 1;
				break;
			}
		}
		if ( !ans )
		{
			if ( puste ) puts ( "Game has not completed" );
			else puts ( "Draw" );
		}
	}
	return 0;
}