#include <iostream>
#include <vector>
#include <string>

using namespace std;

int count( vector<string> board, int N, char c )
{
	int k = 0;

	for ( int y=0; y<N; y++ )
	{
		bool f = false;
		int st;
		for ( int x=0; x<=N; x++ )
			if ( x < N  &&
				 board[y][x] == c )
			{
				if ( ! f )
					f = true,
					st = x;
			}
			else
			{
				if ( f )
					f = false,
					k = max( k, x-st );
			}
	}

	for ( int x=0; x<N; x++ )
	{
		bool f = false;
		int st;
		for ( int y=0; y<=N; y++ )
			if ( y < N  &&
				 board[y][x] == c )
			{
				if ( ! f )
					f = true,
					st = y;
			}
			else
			{
				if ( f )
					f = false,
					k = max( k, y-st );
			}
	}

	for ( int ty=-N+1; ty<N; ty++ )
	{
		bool f = false;
		int st;
		for ( int x=0; x<=N; x++ )
		{
			int y = ty + x;
			if ( 0<=x  &&  x < N  &&
				 0<=y  &&  y < N  &&
				 board[y][x] == c )
			{
				if ( ! f )
					f = true,
					st = x;
			}
			else
			{
				if ( f )
					f = false,
					k = max( k, x-st );
			}
		}
	}

	for ( int ty=-N+1; ty<N; ty++ )
	{
		bool f = false;
		int st;
		for ( int x=0; x<=N; x++ )
		{
			int y = ty +N-1 - x;
			if ( 0<=x  &&  x < N  &&
				 0<=y  &&  y < N  &&
				 board[y][x] == c )
			{
				if ( ! f )
					f = true,
					st = x;
			}
			else
			{
				if ( f )
					f = false,
					k = max( k, x-st );
			}
		}
	}



	return k;
}

int main()
{
	int T;  cin >> T;
	for ( int t=0; t<T; t++ )
	{
		int N, K;
		cin >> N >> K;

		vector<string> board( N );

		for ( int y=0; y<N; y++ )
			cin >> board[y];

		for ( int y=0; y<N; y++ )
		{
			for ( int x=N-1; x>=0; x-- )
				if ( board[y][x] == '.' )
				{
					int t = x-1;
					for ( ; t>=0; t-- )
						if ( board[y][t] != '.' )
							break;
					if ( t >= 0 )
						board[y][x] = board[y][t],
						board[y][t] = '.';
				}
		}

		int bk = count( board, N, 'B' );
		int rk = count( board, N, 'R' );

		cout << "Case #" << (t+1) << ": ";

		if ( bk >= K  &&  rk >= K )
			cout << "Both" << endl;
		else if ( bk >= K )
			cout << "Blue" << endl;
		else if ( rk >= K )
			cout << "Red" << endl;
		else
			cout << "Neither" << endl;

		//for ( int i=0; i<N; i++ )
		//	cout << board[i] << endl;
		//cout << bk << " " << rk << endl;
		//cout << endl;
	}

	return 0;
}



