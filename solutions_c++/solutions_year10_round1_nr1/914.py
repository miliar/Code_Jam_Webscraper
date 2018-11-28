#include <stdio.h>


char tab[50][52];

int main()
{
	freopen( "A.in", "r", stdin );
	freopen( "A.out", "w", stdout );

	int t;
	int n, k;
	int i, r, c, cc, rr;
	int p;
	int red, blue;
	int rred, rblue;
	int mred, mblue;
	int ared, ablue;
	char *ans;

	scanf( "%d", &t );

	for( i = 1; i <= t; ++i )
		{
		scanf( "%d%d\n", &n, &k );
		for( r = 0; r < n; ++r )
			{
			gets( tab[r] );
			}//end for
		for( r = 0; r < n; ++r )
			{
			p = n - 1;
			for( c = n-1; c >= 0; --c )
				{
				while( p >= 0 && tab[r][p] == '.' )
					{
					--p;
					}//end while
				if( p < 0 )
					{
					break;
					}//end if
				tab[r][c] = tab[r][p];
				if( p < c )
					{
					tab[r][p] = '.';
					}//end if
				--p;
				}//end for
			}//end for

		ared = ablue = 0;

		// --
		mred = mblue = 0;
		for( r = n-1; r >= 0; --r )
			{
			red = blue = 0;
			rred = rblue = 0;
			for( c = n-1; c >= 0; --c )
				{
				if( tab[r][c] == 'R' )
					{
					++red;
					blue = 0;
					if( red > rred )
						{
						rred = red;
						}//end if
					}
				else if( tab[r][c] == 'B' )
					{
					++blue;
					red = 0;
					if( blue > rblue )
						{
						rblue = blue;
						}//end if
					}
				else{
					red = blue = 0;
					}//end if
				}//end for
			if( rred > mred )
				{
				mred = rred;
				}//end if
			if( rblue > mblue )
				{
				mblue = rblue;
				}//end if
			}//end for
		if( mred > ared )
			{
			ared = mred;
			}//end if
		if( mblue > ablue )
			{
			ablue = mblue;
			}//end if

		// ||
		mred = mblue = 0;
		for( c = n-1; c >= 0; --c )
			{
			red = blue = 0;
			rred = rblue = 0;
			for( r = n-1; r >= 0; --r )
				{
				if( tab[r][c] == 'R' )
					{
					++red;
					blue = 0;
					if( red > rred )
						{
						rred = red;
						}//end if
					}
				else if( tab[r][c] == 'B' )
					{
					++blue;
					red = 0;
					if( blue > rblue )
						{
						rblue = blue;
						}//end if
					}
				else{
					red = blue = 0;
					}//end if
				}//end for
			if( rred > mred )
				{
				mred = rred;
				}//end if
			if( rblue > mblue )
				{
				mblue = rblue;
				}//end if
			}//end for
		if( mred > ared )
			{
			ared = mred;
			}//end if
		if( mblue > ablue )
			{
			ablue = mblue;
			}//end if

		// /.
		mred = mblue = 0;
		for( c = n - k; c >= 0; --c )
			{
			red = blue = 0;
			rred = rblue = 0;
			for( r = n-1, cc = c; cc < n; --r, ++cc )
				{
				if( tab[r][cc] == 'R' )
					{
					++red;
					blue = 0;
					if( red > rred )
						{
						rred = red;
						}//end if
					}
				else if( tab[r][cc] == 'B' )
					{
					++blue;
					red = 0;
					if( blue > rblue )
						{
						rblue = blue;
						}//end if
					}
				else{
					red = blue = 0;
					}//end if
				}//end for
			if( rred > mred )
				{
				mred = rred;
				}//end if
			if( rblue > mblue )
				{
				mblue = rblue;
				}//end if
			}//end for
		if( mred > ared )
			{
			ared = mred;
			}//end if
		if( mblue > ablue )
			{
			ablue = mblue;
			}//end if

		// '/
		mred = mblue = 0;
		for( r = k-1; r < n-1; ++r )
			{
			red = blue = 0;
			rred = rblue = 0;
			for( c = 0, rr = r; rr >= 0; ++c, --rr )
				{
				if( tab[rr][c] == 'R' )
					{
					++red;
					blue = 0;
					if( red > rred )
						{
						rred = red;
						}//end if
					}
				else if( tab[rr][c] == 'B' )
					{
					++blue;
					red = 0;
					if( blue > rblue )
						{
						rblue = blue;
						}//end if
					}
				else{
					red = blue = 0;
					}//end if
				}//end for
			if( rred > mred )
				{
				mred = rred;
				}//end if
			if( rblue > mblue )
				{
				mblue = rblue;
				}//end if
			}//end for
		if( mred > ared )
			{
			ared = mred;
			}//end if
		if( mblue > ablue )
			{
			ablue = mblue;
			}//end if

		// \' /
		mred = mblue = 0;
		for( c = n - k; c >= 0; --c )
			{
			red = blue = 0;
			rred = rblue = 0;
			for( r = 0, cc = c; cc < n; ++r, ++cc )
				{
				if( tab[r][cc] == 'R' )
					{
					++red;
					blue = 0;
					if( red > rred )
						{
						rred = red;
						}//end if
					}
				else if( tab[r][cc] == 'B' )
					{
					++blue;
					red = 0;
					if( blue > rblue )
						{
						rblue = blue;
						}//end if
					}
				else{
					red = blue = 0;
					}//end if
				}//end for
			if( rred > mred )
				{
				mred = rred;
				}//end if
			if( rblue > mblue )
				{
				mblue = rblue;
				}//end if
			}//end for
		if( mred > ared )
			{
			ared = mred;
			}//end if
		if( mblue > ablue )
			{
			ablue = mblue;
			}//end if

		// .\ /
		mred = mblue = 0;
		for( r = 1; r <= n - k; ++r )
			{
			red = blue = 0;
			rred = rblue = 0;
			for( c = 0, rr = r; rr < n; ++c, ++rr )
				{
				if( tab[rr][c] == 'R' )
					{
					++red;
					blue = 0;
					if( red > rred )
						{
						rred = red;
						}//end if
					}
				else if( tab[rr][c] == 'B' )
					{
					++blue;
					red = 0;
					if( blue > rblue )
						{
						rblue = blue;
						}//end if
					}
				else{
					red = blue = 0;
					}//end if
				}//end for
			if( rred > mred )
				{
				mred = rred;
				}//end if
			if( rblue > mblue )
				{
				mblue = rblue;
				}//end if
			}//end for
		if( mred > ared )
			{
			ared = mred;
			}//end if
		if( mblue > ablue )
			{
			ablue = mblue;
			}//end if

		if( ablue >= k )
			{
			if( ared >= k )
				{
				ans = "Both";
				}
			else{
				ans = "Blue";
				}//end if
			}
		else{
			if( ared >= k )
				{
				ans = "Red";
				}
			else{
				ans = "Neither";
				}//end if
			}//end if
		printf( "Case #%d: %s\n", i, ans );
		}//end for

	return 0;
}
