#include <stdlib.h>
#include <stdio.h>

int main()
{
	freopen( "A.in", "r", stdin );
	freopen( "A.out", "w", stdout );

	int t, n;
	int i, j;
	int op, bp;
	char col;
	int pos;
	int olopt, blopt;
	int time;

	for( scanf( "%d", &t ), i = 1; i <= t; ++i )
		{
		time = 0;
		olopt = blopt = 0;
		op = bp = 1;
		for( scanf( "%d", &n ), j = 0; j < n; ++j )
			{
			scanf( " %c %d", &col, &pos );
			if( col == 'O' )
				{
				if( (time - olopt) >= abs(pos - op) )
					{
					time += 1;
					}
				else{
					time += abs(pos - op) - (time - olopt) + 1;
					}//end if
				olopt = time;
				op = pos;
				}
			else{// 'B'
				if( (time - blopt) >= abs(pos - bp) )
					{
					time += 1;
					}
				else{
					time += abs(pos - bp) - (time - blopt) + 1;
					}//end if
				blopt = time;
				bp = pos;
				}//end if
			}//end for
		printf( "Case #%d: %d\n", i, time );
		}//end for

	return 0;
}
