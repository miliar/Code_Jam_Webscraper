#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int N;
char robot[101];

char opposite_robot( char c )
{
	if( c == 'O' ) return 'B';
	if( c == 'B' ) return 'O';
}

int direction( int d )
{
	if( d > 0 ) return 1;
	if( d < 0 ) return -1;
	return 0;
}

int next_target_index( int idx, char c )
{
	for (int i = idx+1; i < N; i++ )
	{
		if( robot[i] == c ) return i;
	}
	return -1;
}

int main()
{
	int T, kase, i, idx, cur_position[128], target[101];
	int total_time, my_target_pos, opp_target_pos, my_direction, opp_direction, my_diff, opp_diff ;
	char my_robot, opp_robot ;

	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );

	scanf( "%d", &T );

	for ( kase = 1; kase <= T; kase++ )
	{
		scanf( "%d", &N );

		for ( i = 0; i < N; i++ )
		{
			scanf( " %c %d", &robot[i], &target[i] );
		}

		total_time = 0;
		cur_position['B'] = cur_position['O'] = 1;
		opp_target_pos = 1;

		for ( i = 0; i < N; i++ )
		{
			my_robot = robot[i];
			opp_robot = opposite_robot( my_robot );
			
			my_target_pos = target[i];

			idx = next_target_index( i, opp_robot );
			if( idx != -1 )
				opp_target_pos = target[idx];

			my_diff = my_target_pos - cur_position[my_robot];
			opp_diff = opp_target_pos - cur_position[opp_robot];

			my_direction = direction( my_diff );
			opp_direction = direction( opp_diff );
			
			while( my_target_pos != cur_position[my_robot] )
			{
				cur_position[my_robot] += my_direction;
				
				if( cur_position[opp_robot] != opp_target_pos )
					cur_position[opp_robot] += opp_direction;

				total_time++ ; // time increase for walking
			}

			total_time++ ; // time increase for pressing button
			if( cur_position[opp_robot] != opp_target_pos )
				cur_position[opp_robot] += opp_direction; // approaching of opp_robot while pressing button of my_robot

		}

		printf( "Case #%d: %d\n", kase, total_time );
	}
	return 0;
}