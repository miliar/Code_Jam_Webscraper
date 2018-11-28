#include <iostream.h>
#include <fstream.h>

// Code Jam 2013
// Qualification Round
// Problem A. Tic-Tac-Toe-Tomek



int main(int argc, char *argv[])
{
	int T;
	int t;
	char c;
	
	bool banyemptycell;
	bool bxwon;
	bool bowon;
	
	char board[16];
	
	int i;
	int j;
	int k;
	
	ifstream inFile;
	
	//inFile.open("test.in");
	if ( argc < 2 )
	{
		cout << "No input file given!" << endl;
		exit(1);
	}
	inFile.open(argv[1]);
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> T;
	
	for (t=0;t<T;t++)
	{
		banyemptycell = 0;
		bxwon = 0;
		bowon = 0;
		
		// read board
		for (i=0;i<16;i++)
		{
			inFile >> board[i];
			
			// check for empty board
			if ( board[i] == '.' )
			{
				banyemptycell = 1;
			}
		}
		
		// check rows
		for (i=0;i<16;i+=4)
		{
			// check X's
			k = 0;
			for (j=0;j<4;j++)
			{
				if ( (board[i+j] == 'X') || (board[i+j] == 'T') )
				{
					k++;
				}
				if ( k==4 )
				{
					bxwon = 1;
					// no performance optimizations needed
				}
			}
			
			// check O's
			k = 0;
			for (j=0;j<4;j++)
			{
				if ( (board[i+j] == 'O') || (board[i+j] == 'T') )
				{
					k++;
				}
				if ( k==4 )
				{
					bowon = 1;
					// no performance optimizations needed
				}
			}
		}
		
		
		// check columns
		for (i=0;i<4;i++)
		{
			// check X's
			k = 0;
			for (j=0;j<4;j++)
			{
				if ( (board[i+j*4] == 'X') || (board[i+j*4] == 'T') )
				{
					k++;
				}
				if ( k==4 )
				{
					bxwon = 1;
					// no performance optimizations needed
				}
			}
			
			// check O's
			k = 0;
			for (j=0;j<4;j++)
			{
				if ( (board[i+j*4] == 'O') || (board[i+j*4] == 'T') )
				{
					k++;
				}
				if ( k==4 )
				{
					bowon = 1;
					// no performance optimizations needed
				}
			}
		}
		
		
		// check diagonals
		
		// check X's - first diagonal
		k = 0;
		for (i=0;i<16;i+=5)
		{
			if ( (board[i] == 'X') || (board[i] == 'T') )
			{
				k++;
			}
			if ( k==4 )
			{
				bxwon = 1;
				// no performance optimizations needed
			}		
		}
		
		// check X's - second diagonal
		k = 0;
		for (i=3;i<13;i+=3)
		{
			if ( (board[i] == 'X') || (board[i] == 'T') )
			{
				k++;
			}
			if ( k==4 )
			{
				bxwon = 1;
				// no performance optimizations needed
			}		
		}
		
		// check O's - first diagonal
		k = 0;
		for (i=0;i<16;i+=5)
		{
			if ( (board[i] == 'O') || (board[i] == 'T') )
			{
				k++;
			}
			if ( k==4 )
			{
				bowon = 1;
				// no performance optimizations needed
			}		
		}
		
		// check O's - second diagonal
		k = 0;
		for (i=3;i<13;i+=3)
		{
			if ( (board[i] == 'O') || (board[i] == 'T') )
			{
				k++;
			}
			if ( k==4 )
			{
				bowon = 1;
				// no performance optimizations needed
			}		
		}
		
		
		for (i=0;i<4;i++)
		{
			// check X's
			k = 0;
			for (j=0;j<4;j++)
			{
				if ( (board[i+j*4] == 'X') || (board[i+j*4] == 'T') )
				{
					k++;
				}
				if ( k==4 )
				{
					bxwon = 1;
					// no performance optimizations needed
				}
			}
			
			// check O's
			k = 0;
			for (j=0;j<4;j++)
			{
				if ( (board[i+j*4] == 'O') || (board[i+j*4] == 'T') )
				{
					k++;
				}
				if ( k==4 )
				{
					bowon = 1;
					// no performance optimizations needed
				}
			}
		}
		
		
		cout << "Case #" << t+1 << ": ";
		
		if  (bxwon)
		{
			cout << "X won";
		}
		else if ( bowon )
		{
			cout << "O won";
		}
		else if ( banyemptycell )
		{
			cout << "Game has not completed";
		}
		else
		{
			cout << "Draw";
		}
		cout << endl;
		
	}
		
		
	
	inFile.close();
	return 0;
}