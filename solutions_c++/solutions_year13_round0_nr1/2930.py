
#include <iostream>

#include <vector>
#include <string>

using namespace std;

int tests;
vector<string> board( 4 );


int main()
{
	cin >> tests;

	for( int curTest=0; curTest<tests; ++curTest )
	{
		cin >> board[0] >> board[1] >> board[2] >> board[3];

		bool include_emp = false;
		for( int i=0; i<board.size(); ++i )
		{
			for( int j=0; j<board[i].size(); ++j )
			{
				if ( board[i][j] == '.' )
				{
					include_emp = true;
				}
			}
		}

		int p = -1;
		for( int pi=0; pi<2; ++pi )
		{
			const auto kPC = ( pi ? 'O' : 'X' );
			bool ok = false;
			// row
			for( int i=0; i<4; ++i )
			{
				ok = true;
				for( int x=0; x<4; ++x )
					if ( board[i][x]!=kPC && board[i][x]!='T' ) ok = false;
				if ( ok ) { p = pi; }
			}
			// col
			for( int i=0; i<4; ++i )
			{
				ok = true;
				for( int x=0; x<4; ++x )
					if ( board[x][i]!=kPC && board[x][i]!='T' ) ok = false;
				if ( ok ) { p = pi; }
			}
			// diag
			for( int i=0; i<4; ++i )
			{
				ok = true;
				for( int x=0; x<4; ++x )
					if ( board[x][x]!=kPC && board[x][x]!='T' ) ok = false;
				if ( ok ) { p = pi; }

				ok = true;
				for( int x=0; x<4; ++x )
					if ( board[x][3-x]!=kPC && board[x][3-x]!='T' ) ok = false;
				if ( ok ) { p = pi; }
			}
		}

		cout << "Case #" << (curTest+1) << ": ";
		if ( p == -1 )
		{
			if ( include_emp )
			{
				cout << "Game has not completed";
			}
			else
			{
				cout << "Draw";
			}
		}
		else
		{
			cout << (p?"O":"X") << " won";
		}
		cout << endl;
	}

	return 0;
}

