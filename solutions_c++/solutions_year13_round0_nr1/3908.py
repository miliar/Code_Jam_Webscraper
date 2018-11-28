
#include <iostream>
#include <cstdio>
#include <string.h>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;

#define fr( i , c , n ) for( int i = (c) ; i < (n) ;i++ )
#define clr( a , c ) memset( a , c , sizeof a )
#define P pair<int , int>
#define ULL unsigned long long

string board[4];
int main()
{
	int T;
	cin >> T;
	fr( t , 1 , T+1 )
	{
		fr( i , 0 , 4 )
			cin >> board[i];
		bool Owins = false;
		bool Xwins = false;

		fr( i , 0 , 4 )
		{
			bool Ook = true;
			bool Xok = true;
			fr( j , 0 , 4 )
			{
				if( board[i][j] == 'O' || board[i][j] == '.' )
					Xok = false;
				if( board[i][j] == 'X' || board[i][j] == '.' )
					Ook = false;
			}

			Owins = Ook;
			Xwins = Xok;
			if( Owins || Xwins ) break;
		}

		if( !( Owins || Xwins ) )
		fr( j , 0 , 4 )
		{
			bool Ook = true;
			bool Xok = true;
			fr( i , 0 , 4 )
			{
				if( board[i][j] == 'O' || board[i][j] == '.' )
					Xok = false;
				if( board[i][j] == 'X' || board[i][j] == '.' )
					Ook = false;
			}

			Owins = Ook;
			Xwins = Xok;
			if( Owins || Xwins ) break;
		}

		if( !( Owins || Xwins ) )
		{
			bool Ookm = true;
			bool Xokm = true;
			bool Ooks = true;
			bool Xoks = true;
			fr( i , 0 , 4 )
		{
			
			if( board[i][i] == 'O' || board[i][i] == '.' )
				Xokm = false;
			if( board[i][i] == 'X' || board[i][i] == '.' )
				Ookm = false;
			if( board[i][3-i] == 'O' || board[i][3-i] == '.' )
				Xoks = false;
			if( board[i][3-i] == 'X' || board[i][3-i] == '.' )
				Ooks = false;
		}
			Owins = Ookm || Ooks;
			Xwins = Xokm || Xoks;
		}

		if( Owins )
		{
			printf("Case #%d: O won\n" , t );
			continue;
		}
		else if( Xwins )
		{
			printf("Case #%d: X won\n" , t );
			continue;
		}

		bool finished = true;
		fr( i , 0 , 4 )
			fr( j , 0 , 4 )
			if( board[i][j] == '.' )
			{
				finished = false;
				break;
			}
		if( !finished )
		{
			printf("Case #%d: Game has not completed\n" , t );
			continue;
		}
		else
			printf("Case #%d: Draw\n" , t );
	}
	return 0;
}