#include <cstdio>
#include <map>
#include <set>
#include <vector>
using namespace std;

static const int MAX = 12;
static const int MAXBOXES = 5;

int R, C;
char Field[ MAX ][ MAX + 1 ];

void Read()
{
	int i;
	scanf( "%d%d", &R, &C );
	for( i = 0; i < R; ++i )
	{
		scanf( "%s", Field[ i ] );
	}
}

struct sState
{
	int Count;
	int Row[ MAXBOXES ], Col[ MAXBOXES ];
	bool Dangerous;
};

bool operator <( const sState &state1, const sState &state2 )
{
	int i;
	for( i = 0; i < state1.Count; ++i )
	{
		if( state1.Row[ i ] < state2.Row[ i ] )
			return true;
		if( state1.Row[ i ] > state2.Row[ i ] )
			return false;
		if( state1.Col[ i ] < state2.Col[ i ] )
			return true;
		if( state1.Col[ i ] > state2.Col[ i ] )
			return false;
	}
	return false;
}

map< sState, int > State;
vector< sState > Queue;
int Head;

bool Empty( int row, int col, const sState &state )
{
	int i;
	if( !( 0 <= row && row < R &&
		    0 <= col && col < C ) )
		return false;
	if( Field[ row ][ col ] == '#' )
		return false;
	for( i = 0; i < state.Count; ++i )
	{
		if( state.Row[ i ] == row && state.Col[ i ] == col )
			return false;
	}
	return true;
}

bool Dangerous( const sState &state )
{
	int i;
	int queue[ MAXBOXES ];
	bool is_used[ MAXBOXES ];
	int head, tail;

	head = tail = 0;
	memset( is_used, 0, sizeof( is_used ) );

	queue[ tail++ ] = 0;
	is_used[ 0 ] = true;
	while( head != tail )
	{
		int index = queue[ head++ ];
		for( i = 0; i < state.Count; ++i )
		{
			if( is_used[ i ] )
				continue;
			int drow = abs( state.Row[ index ] - state.Row[ i ] );
			int dcol = abs( state.Col[ index ] - state.Col[ i ] );
			if( drow == 1 && dcol == 0 ||
				 drow == 0 && dcol == 1 )
			{
				is_used[ i ] = true;
				queue[ tail++ ] = i;
			}
		}
	}

	if( head != state.Count )
		return true;

	return false;
}

int Result;

void Work()
{
	int i, j;

	sState state, final_state;
	memset( &state, 0, sizeof( state ) );
	memset( &final_state, 0, sizeof( final_state ) );
	for( i = 0; i < R; ++i )
	{
		for( j = 0; j < C; ++j )
		{
			if( Field[ i ][ j ] == 'o' || Field[ i ][ j ] == 'w' )
			{
				state.Row[ state.Count ] = i;
				state.Col[ state.Count ] = j;
				++state.Count;
			}
			if( Field[ i ][ j ] == 'x' || Field[ i ][ j ] == 'w' )
			{
				final_state.Row[ final_state.Count ] = i;
				final_state.Col[ final_state.Count ] = j;
				++final_state.Count;
			}
		}
	}
	state.Dangerous = Dangerous( state );
	final_state.Dangerous = Dangerous( final_state );

	Result = -1;

	Head = 0;
	State.clear();
	Queue.clear();

	State.insert( make_pair( state, 0 ) );
	Queue.push_back( state );
	while( Head != ( int )Queue.size() )
	{
		sState state = Queue[ Head++ ];

		for( i = 0; i < state.Count; ++i )
		{
			for( j = 0; j < state.Count; ++j )
			{
				if( state.Row[ i ] == final_state.Row[ j ] &&
					 state.Col[ i ] == final_state.Col[ j ] )
					break;
			}
			if( j == state.Count )
				break;
		}
		if( i == state.Count )
		{
			Result = State[ state ];
			break;
		}

		for( i = 0; i < state.Count; ++i )
		{
			// Down
			if( Empty( state.Row[ i ] - 1, state.Col[ i ], state ) && Empty( state.Row[ i ] + 1, state.Col[ i ], state ) )
			{
				sState new_state = state;
				new_state.Row[ i ] += 1;
				new_state.Dangerous = Dangerous( new_state );
				if( ( !state.Dangerous || !new_state.Dangerous ) && State.find( new_state ) == State.end() )
				{
					State.insert( make_pair( new_state, State[ state ] + 1 ) );
					Queue.push_back( new_state );
				}
			}
			// Up
			if( Empty( state.Row[ i ] + 1, state.Col[ i ], state ) && Empty( state.Row[ i ] - 1, state.Col[ i ], state ) )
			{
				sState new_state = state;
				new_state.Row[ i ] -= 1;
				new_state.Dangerous = Dangerous( new_state );
				if( ( !state.Dangerous || !new_state.Dangerous ) && State.find( new_state ) == State.end() )
				{
					State.insert( make_pair( new_state, State[ state ] + 1 ) );
					Queue.push_back( new_state );
				}
			}
			// Right
			if( Empty( state.Row[ i ], state.Col[ i ] - 1, state ) && Empty( state.Row[ i ], state.Col[ i ] + 1, state ) )
			{
				sState new_state = state;
				new_state.Col[ i ] += 1;
				new_state.Dangerous = Dangerous( new_state );
				if( ( !state.Dangerous || !new_state.Dangerous ) && State.find( new_state ) == State.end() )
				{
					State.insert( make_pair( new_state, State[ state ] + 1 ) );
					Queue.push_back( new_state );
				}
			}
			// Left or so...
			if( Empty( state.Row[ i ], state.Col[ i ] + 1, state ) && Empty( state.Row[ i ], state.Col[ i ] - 1, state ) )
			{
				sState new_state = state;
				new_state.Col[ i ] -= 1;
				new_state.Dangerous = Dangerous( new_state );
				if( ( !state.Dangerous || !new_state.Dangerous ) && State.find( new_state ) == State.end() )
				{
					State.insert( make_pair( new_state, State[ state ] + 1 ) );
					Queue.push_back( new_state );
				}
			}
		}
	}
}

void Write( int t )
{
	printf( "Case #%d: %d\n", t, Result );
}

int T;

int main()
{
	int t;
	scanf( "%d", &T );
	for( t = 0; t < T; ++t )
	{
		Read();
		Work();
		Write( t + 1 );
	}
	return 0;
}
