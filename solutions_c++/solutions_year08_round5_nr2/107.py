#include <cstdio>
#include <queue>
#include <set>

using namespace std;

int R, C;
char m[20][20];
int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

int MakeState( int sx, int sy, int p1x, int p1y, int p1d, int p2x, int p2y, int p2d )
{
	int st;
	st = sx; st <<= 3; 
	st |= sy; st <<= 3;
	st |= p1x; st <<= 3;
	st |= p1y; st <<= 2;
	st |= p1d; st <<= 3;
	st |= p2x; st <<= 3;
	st |= p2y; st <<= 2;
	st |= p2d;
	return st;
}

void GetState( int st, int &sx, int &sy, int &p1x, int &p1y, int &p1d, int &p2x, int &p2y, int &p2d )
{
	p2d = st & 3; st >>= 2;
	p2y = st & 7; st >>= 3;
	p2x = st & 7; st >>= 3;
	p1d = st & 3; st >>= 2;
	p1y = st & 7; st >>= 3;
	p1x = st & 7; st >>= 3;
	sy = st & 7; st >>= 3;
	sx = st & 7;
}

int Valid( int x, int y )
{
	return x >= 0 && x < R && y >= 0 && y < C && m[x][y] != '#';
}

void GetWall( int x, int y, int d, int &wx, int &wy )
{
	while( Valid(x, y) )
	{
		x += dx[d];
		y += dy[d];
	}
	wx = x - dx[d];
	wy = y - dy[d];
}

void PrintState(int sx, int sy, int p1x, int p1y, int p1d, int p2x, int p2y, int p2d, int steps )
{
	printf("State = %d %d | %d %d %d | %d %d %d | %d\n", sx, sy, p1x, p1y, p1d, p2x, p2y, p2d, steps);
}

int go( int sx, int sy )
{
	int tx, ty;
	GetWall( sx, sy, 0, tx, ty );
	int p1x = tx;
	int p1y = ty;
	int p1d = 0;
	GetWall( sx, sy, 1, tx, ty );
	int p2x = tx;
	int p2y = ty;
	int p2d = 1;

	queue< pair<int, int> > q, q2;
	set< int > s;
	q.push( make_pair(0, MakeState( sx, sy, p1x, p1y, p1d, p2x, p2y, p2d ) ) );
	s.insert( MakeState( sx, sy, p1x, p1y, p1d, p2x, p2y, p2d ) );

	int found = -1;
	while( !q.empty() || !q2.empty() )
	{
		pair<int,int> p;
		if( !q.empty() )
		{
			p = q.front();
			q.pop();
		}
		else
		{
			p = q2.front();
			q2.pop();
		}

		int steps = p.first;
		GetState( p.second, sx, sy, p1x, p1y, p1d, p2x, p2y, p2d );

		if( m[sx][sy] == 'X' && (found == -1 || steps < found ))
		{
			found = steps;
			continue;
		}

		if( found != -1 && steps >= found )
			continue;

		for(int i = 0; i < 4; i++)
		{
			if( p1x == sx && p1y == sy && p1d == i && p2x != -1)
			{
				int newst = MakeState( p2x, p2y, p1x, p1y, p1d, p2x, p2y, p2d );
				if( s.count( newst ) == 0 )
				{
					s.insert( newst );
					q2.push( make_pair( steps + 1, newst ) );
				}
			}

			if( p2x == sx && p2y == sy && p2d == i && p1x != -1)
			{
				int newst = MakeState( p1x, p1y, p1x, p1y, p1d, p2x, p2y, p2d );
				if( s.count( newst ) == 0 )
				{
					s.insert( newst );
					q2.push( make_pair( steps + 1, newst ) );
				}
			}

			if( Valid( sx + dx[i], sy + dy[i] ) )
			{
				int newst = MakeState( sx+dx[i], sy+dy[i], p1x, p1y, p1d, p2x, p2y, p2d );
				if( s.count( newst ) == 0 )
				{
					s.insert( newst );
					q2.push( make_pair( steps + 1, newst ) );
				}
			}

			int wx, wy;
			GetWall( sx, sy, i, wx, wy );
			if( p1x != wx || p1y != wy || p1d != i )
			{
				int newst = MakeState( sx, sy, p1x, p1y, p1d, wx, wy, i );
				if( s.count( newst ) == 0 )
				{			
					s.insert( newst );
					q.push( make_pair( steps, newst ) );
				}
			}

			if( p2x != wx || p2y != wy || p2d != i )
			{
				int newst = MakeState( sx, sy, wx, wy, i , p2x, p2y, p2d);
				if( s.count( newst ) == 0 )
				{
					s.insert( newst );
					q.push( make_pair( steps, newst ) );
				}
			}

		}
	}
	return found;
}

int main()
{
	int K;
	scanf("%d", &K);
	for(int k = 1; k <= K; k++)
	{
		scanf("%d %d", &R, &C);
		for(int i = 0; i < R; i++)
			scanf("%s", m[i]);

		int iX, iY;
		for(int i = 0; i < R; i++)
			for(int j = 0; j < C; j++)
				if( m[i][j] == 'O' )
				{
					iX = i;
					iY = j;
				}
		
		int res = go( iX, iY);
		printf("Case #%d: ", k);
		if( res == -1 )
			printf("THE CAKE IS A LIE\n");
		else
			printf("%d\n", res );
	}
}