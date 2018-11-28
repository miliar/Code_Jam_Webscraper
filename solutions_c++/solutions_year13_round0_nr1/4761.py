#include <iostream>

using namespace std;

int main()
{
	char board[4][4];
	string inputline[4];
	string temp;
	int input;
	int cases;
	int i,j;
	int countX, countO, countB;

	cin>>input;

	cases = 1;
	while ( cases <= input )
	{
		countX=countO=countB=0;
		for ( i=0; i<4; i++)
			cin>>inputline[i];

		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				board[i][j] = inputline[i].at(j);
				if ( board[i][j] == 'X' )
					countX++;
				else if ( board[i][j] == 'O' )
					countO++;
				else if ( board[i][j] == '.' )
					countB++;
			}
		}

/*		cout<<"Case #"<<cases<<":\n";
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cout<<board[i][j]<<" ";
			}
			cout<<"\n";
		} */

		if ( countX < 3 && countO < 3 ) 
		{
			if ( countB == 0 )
				cout<<"Case #"<<cases<<": Draw\n";
			else
				cout<<"Case #"<<cases<<": Game has not completed\n";
		}
		else
		{
			for(i=0;i<4;i++)
			{
				if ( board[i][i] == 'X' || board[i][i] == 'T' )
				{
					if ( (board[i][0] == 'X' || board[i][0] == 'T') && \
						(board[i][1] == 'X' || board[i][1] == 'T') && \
						(board[i][2] == 'X' || board[i][2] == 'T') && \
						(board[i][3] == 'X' || board[i][3] == 'T') )
					{
						cout<<"Case #"<<cases<<": X won\n";
						break;
					}
					else if ( (board[0][i] == 'X' || board[0][i] == 'T') && \
						(board[1][i] == 'X' || board[1][i] == 'T') && \
						(board[2][i] == 'X' || board[2][i] == 'T') && \
						(board[3][i] == 'X' || board[3][i] == 'T') )
					{
						cout<<"Case #"<<cases<<": X won\n";
						break;
					}
					else if ( i == 0 )
					{
						if ( (board[0][0] == 'X' || board[0][0] == 'T') && \
							(board[1][1] == 'X' || board[1][1] == 'T') && \
							(board[2][2] == 'X' || board[2][2] == 'T') && \
							(board[3][3] == 'X' || board[3][3] == 'T') )
						{
							cout<<"Case #"<<cases<<": X won\n";
							break;
						}
					}
				}
				if ( board[i][i] == 'O' || board[i][i] == 'T' )
				{
					if ( (board[i][0] == 'O' || board[i][0] == 'T') && \
						(board[i][1] == 'O' || board[i][1] == 'T') && \
						(board[i][2] == 'O' || board[i][2] == 'T') && \
						(board[i][3] == 'O' || board[i][3] == 'T') )
					{
						cout<<"Case #"<<cases<<": O won\n";
						break;
					}
					else if ( (board[0][i] == 'O' || board[0][i] == 'T') && \
						(board[1][i] == 'O' || board[1][i] == 'T') && \
						(board[2][i] == 'O' || board[2][i] == 'T') && \
						(board[3][i] == 'O' || board[3][i] == 'T') )
					{
						cout<<"Case #"<<cases<<": O won\n";
						break;
					}
					else if ( i == 0 )
					{
						if ( (board[0][0] == 'O' || board[0][0] == 'T') && \
							(board[1][1] == 'O' || board[1][1] == 'T') && \
							(board[2][2] == 'O' || board[2][2] == 'T') && \
							(board[3][3] == 'O' || board[3][3] == 'T') )
						{
							cout<<"Case #"<<cases<<": O won\n";
							break;
						}
					}
				}
			}
			
			if ( i == 4 )
			{
				if ( (board[0][3] == 'X' || board[0][3] == 'T') && \
					(board[1][2] == 'X' || board[1][2] == 'T') && \
					(board[2][1] == 'X' || board[2][1] == 'T') && \
					(board[3][0] == 'X' || board[3][0] == 'T') )
					cout<<"Case #"<<cases<<": X won\n";
				else if ( (board[0][3] == 'O' || board[0][3] == 'T') && \
					(board[1][2] == 'O' || board[1][2] == 'T') && \
					(board[2][1] == 'O' || board[2][1] == 'T') && \
					(board[3][0] == 'O' || board[3][0] == 'T') )
					cout<<"Case #"<<cases<<": O won\n";
				else 
				{
					if ( countB == 0 )
						cout<<"Case #"<<cases<<": Draw\n";
					else
						cout<<"Case #"<<cases<<": Game has not completed\n";
				}
			}
		}

		cases = cases + 1;
	}

	return 0;
}
