#include <cstdio>
#include <memory>

const int MAX = 15;
const int MAXQUEUE = MAX * MAX * MAX * MAX * MAX * MAX * 7;

int R, C;
char Map[ MAX ][ MAX ];

void Read()
{
	int i, j;
	scanf( "%d%d", &R, &C );
	for( i = 0; i < R; ++i )
	{
		for( j = 0; j < C; ++j )
		{
			scanf( " %c", &Map[ i ][ j ] );
		}
	}
}

int StartI, StartJ;
int FinishI, FinishJ;
int Head, Tail;
int Result;
int TopPortal[ MAX ][ MAX ];
int BottomPortal[ MAX ][ MAX ];
int LeftPortal[ MAX ][ MAX ];
int RightPortal[ MAX ][ MAX ];
bool IsUsed[ MAX ][ MAX ][ MAX ][ MAX ][ MAX ][ MAX ];
int Length[ MAX ][ MAX ][ MAX ][ MAX ][ MAX ][ MAX ];
int Queue[ MAXQUEUE ];

inline void Add( int player_i, int player_j, int yellow_i, int yellow_j, int blue_i, int blue_j, int step )
{
	if( !IsUsed[ player_i ][ player_j ][ yellow_i ][ yellow_j ][ blue_i ][ blue_j ] )
	{
		if( Tail >= MAXQUEUE )
			puts( "OVERFLOW!!!!!!!!!!!!!!!!" );
		IsUsed[ player_i ][ player_j ][ yellow_i ][ yellow_j ][ blue_i ][ blue_j ] = true;
		Queue[ Tail++ ] = player_i;
		Queue[ Tail++ ] = player_j;
		Queue[ Tail++ ] = yellow_i;
		Queue[ Tail++ ] = yellow_j;
		Queue[ Tail++ ] = blue_i;
		Queue[ Tail++ ] = blue_j;
		Queue[ Tail++ ] = step;
	}
}

inline void Get( int &player_i, int &player_j, int &yellow_i, int &yellow_j, int &blue_i, int &blue_j, int &step )
{
	player_i = Queue[ Head++ ];
	player_j = Queue[ Head++ ];
	yellow_i = Queue[ Head++ ];
	yellow_j = Queue[ Head++ ];
	blue_i = Queue[ Head++ ];
	blue_j = Queue[ Head++ ];
	step = Queue[ Head++ ];
}

inline void MoveTo( int player_i, int player_j, int yellow_i, int yellow_j, int blue_i, int blue_j, int step )
{
	Add( player_i, player_j, yellow_i, yellow_j,                             blue_i, blue_j,                                 step );
	Add( player_i, player_j, TopPortal[ player_i ][ player_j ], player_j,    blue_i, blue_j,                                 step );
	Add( player_i, player_j, BottomPortal[ player_i ][ player_j ], player_j, blue_i, blue_j,                                 step );
	Add( player_i, player_j, player_i, LeftPortal[ player_i ][ player_j ],   blue_i, blue_j,                                 step );
	Add( player_i, player_j, player_i, RightPortal[ player_i ][ player_j ],  blue_i, blue_j,                                 step );

	Add( player_i, player_j, yellow_i, yellow_j,                             TopPortal[ player_i ][ player_j ], player_j,    step );
	Add( player_i, player_j, TopPortal[ player_i ][ player_j ], player_j,    TopPortal[ player_i ][ player_j ], player_j,    step );
	Add( player_i, player_j, BottomPortal[ player_i ][ player_j ], player_j, TopPortal[ player_i ][ player_j ], player_j,    step );
	Add( player_i, player_j, player_i, LeftPortal[ player_i ][ player_j ],   TopPortal[ player_i ][ player_j ], player_j,    step );
	Add( player_i, player_j, player_i, RightPortal[ player_i ][ player_j ],  TopPortal[ player_i ][ player_j ], player_j,    step );

	Add( player_i, player_j, yellow_i, yellow_j,                             BottomPortal[ player_i ][ player_j ], player_j, step );
	Add( player_i, player_j, TopPortal[ player_i ][ player_j ], player_j,    BottomPortal[ player_i ][ player_j ], player_j, step );
	Add( player_i, player_j, BottomPortal[ player_i ][ player_j ], player_j, BottomPortal[ player_i ][ player_j ], player_j, step );
	Add( player_i, player_j, player_i, LeftPortal[ player_i ][ player_j ],   BottomPortal[ player_i ][ player_j ], player_j, step );
	Add( player_i, player_j, player_i, RightPortal[ player_i ][ player_j ],  BottomPortal[ player_i ][ player_j ], player_j, step );

	Add( player_i, player_j, yellow_i, yellow_j,                             player_i, LeftPortal[ player_i ][ player_j ],   step );
	Add( player_i, player_j, TopPortal[ player_i ][ player_j ], player_j,    player_i, LeftPortal[ player_i ][ player_j ],   step );
	Add( player_i, player_j, BottomPortal[ player_i ][ player_j ], player_j, player_i, LeftPortal[ player_i ][ player_j ],   step );
	Add( player_i, player_j, player_i, LeftPortal[ player_i ][ player_j ],   player_i, LeftPortal[ player_i ][ player_j ],   step );
	Add( player_i, player_j, player_i, RightPortal[ player_i ][ player_j ],  player_i, LeftPortal[ player_i ][ player_j ],   step );

	Add( player_i, player_j, yellow_i, yellow_j,                             player_i, RightPortal[ player_i ][ player_j ],  step );
	Add( player_i, player_j, TopPortal[ player_i ][ player_j ], player_j,    player_i, RightPortal[ player_i ][ player_j ],  step );
	Add( player_i, player_j, BottomPortal[ player_i ][ player_j ], player_j, player_i, RightPortal[ player_i ][ player_j ],  step );
	Add( player_i, player_j, player_i, LeftPortal[ player_i ][ player_j ],   player_i, RightPortal[ player_i ][ player_j ],  step );
	Add( player_i, player_j, player_i, RightPortal[ player_i ][ player_j ],  player_i, RightPortal[ player_i ][ player_j ],  step );
}

inline void MoveToCheck( int player_i, int player_j, int yellow_i, int yellow_j, int blue_i, int blue_j, int step )
{
	if( 0 <= player_i && player_i < R && 
		 0 <= player_j && player_j < C && 
		 Map[ player_i ][ player_j ] == '.' )
		MoveTo( player_i, player_j, yellow_i, yellow_j, blue_i, blue_j, step );
}

#ifdef _DEBUG
int First[ MAX ][ MAX ];
#endif

void Work()
{
	int i, j, k;

	// Вычисляем, куда попадают порталы
	for( i = 0; i < R; ++i )
	{
		for( j = 0; j < C; ++j )
		{
			if( Map[ i ][ j ] == 'O' )
			{
				StartI = i;
				StartJ = j;
				Map[ i ][ j ] = '.';
			}
			if( Map[ i ][ j ] == 'X' )
			{
				FinishI = i;
				FinishJ = j;
				Map[ i ][ j ] = '.';
			}
			if( Map[ i ][ j ] == '.' )
			{
				for( k = i; k >= 0 && Map[ k ][ j ] != '#'; --k )
					;
				TopPortal[ i ][ j ] = k + 1;
				for( k = i; k < R && Map[ k ][ j ] != '#'; ++k )
					;
				BottomPortal[ i ][ j ] = k - 1;
				for( k = j; k >= 0 && Map[ i ][ k ] != '#'; --k )
					;
				LeftPortal[ i ][ j ] = k + 1;
				for( k = j; k < C && Map[ i ][ k ] != '#'; ++k )
					;
				RightPortal[ i ][ j ] = k - 1;
			}
		}
	}

	// Го
	Result = -1;
	MoveTo( StartI, StartJ, TopPortal[ StartI ][ StartJ ], StartJ, TopPortal[ StartI ][ StartJ ], StartJ, 0 );
	while( Head != Tail )
	{
		int player_i, player_j, yellow_i, yellow_j, blue_i, blue_j, step;
		Get( player_i, player_j, yellow_i, yellow_j, blue_i, blue_j, step );
		if( player_i == FinishI && player_j == FinishJ )
		{
			Result = step;
			break;
		}
		++step;
		MoveToCheck( player_i - 1, player_j, yellow_i, yellow_j, blue_i, blue_j, step );
		MoveToCheck( player_i + 1, player_j, yellow_i, yellow_j, blue_i, blue_j, step );
		MoveToCheck( player_i, player_j - 1, yellow_i, yellow_j, blue_i, blue_j, step );
		MoveToCheck( player_i, player_j + 1, yellow_i, yellow_j, blue_i, blue_j, step );
		if( player_i == blue_i && player_j == blue_j )
			MoveTo( yellow_i, yellow_j, yellow_i, yellow_j, blue_i, blue_j, step );
		if( player_i == yellow_i && player_j == yellow_j )
			MoveTo( blue_i, blue_j, yellow_i, yellow_j, blue_i, blue_j, step );
	}
	
	// Очистить IsUsed
#ifdef _DEBUG
	memset( First, -1, sizeof( First ) );
#endif
	for( Head = 0; Head < Tail; )
	{
		int player_i, player_j, yellow_i, yellow_j, blue_i, blue_j, step;
		Get( player_i, player_j, yellow_i, yellow_j, blue_i, blue_j, step );
		IsUsed[ player_i ][ player_j ][ yellow_i ][ yellow_j ][ blue_i ][ blue_j ] = false;
#ifdef _DEBUG
		if( First[ player_i ][ player_j ] == -1 || First[ player_i ][ player_j ] > step )
			First[ player_i ][ player_j ] = step;
#endif
	}

#ifdef _DEBUG
	for( i = 0; i < R; ++i )
	{
		for( j = 0; j < C; ++j )
		{
			printf( " %4d", First[ i ][ j ] );
		}
		puts( "" );
	}
#endif
}

void Write( int i )
{
	if( Result == -1 )
		printf( "Case #%d: THE CAKE IS A LIE\n", i );
	else
		printf( "Case #%d: %d\n", i, Result );
}

int main()
{
	int i, n;
	scanf( "%d", &n );
	for( i = 1; i <= n; ++i )
	{
		Read();
		Work();
		Write( i );
	}
	return 0;
}
