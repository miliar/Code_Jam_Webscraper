#include <iostream>

// Represent X by 1, Y by -1 and empty by 0
// Use a vector to represent the board

using namespace std;

bool isX(char c);
bool isO(char c);

int main()
{
	int N=4;
	int numCase;
	cin >> numCase;
	int i, j, n;
	char row1[N], row2[N], row3[N], row4[N];


	for (i = 0; i < numCase; i++)
	{
		cin >> row1;
		cin >> row2;
		cin >> row3;
		cin >> row4;
		
		bool xWins=0, oWins=0, undecided=0;

		// Search for winner on each row
		if( isX(row1[0])&&isX(row1[1])&&isX(row1[2])&&isX(row1[3]) ||
			isX(row2[0])&&isX(row2[1])&&isX(row2[2])&&isX(row2[3]) ||
			isX(row3[0])&&isX(row3[1])&&isX(row3[2])&&isX(row3[3]) ||
			isX(row4[0])&&isX(row4[1])&&isX(row4[2])&&isX(row4[3]) ) {
				xWins=1;
		}
		
		if( isO(row1[0])&&isO(row1[1])&&isO(row1[2])&&isO(row1[3]) ||
			isO(row2[0])&&isO(row2[1])&&isO(row2[2])&&isO(row2[3]) ||
			isO(row3[0])&&isO(row3[1])&&isO(row3[2])&&isO(row3[3]) ||
			isO(row4[0])&&isO(row4[1])&&isO(row4[2])&&isO(row4[3]) ) {
				oWins=1;
		}
		
		// Search for winner on each col
		if( isX(row1[0])&&isX(row2[0])&&isX(row3[0])&&isX(row4[0]) ||
			isX(row1[1])&&isX(row2[1])&&isX(row3[1])&&isX(row4[1]) ||
			isX(row1[2])&&isX(row2[2])&&isX(row3[2])&&isX(row4[2]) ||
			isX(row1[3])&&isX(row2[3])&&isX(row3[3])&&isX(row4[3]) ) {
				xWins=1;
		}
		
		if( isO(row1[0])&&isO(row2[0])&&isO(row3[0])&&isO(row4[0]) ||
			isO(row1[1])&&isO(row2[1])&&isO(row3[1])&&isO(row4[1]) ||
			isO(row1[2])&&isO(row2[2])&&isO(row3[2])&&isO(row4[2]) ||
			isO(row1[3])&&isO(row2[3])&&isO(row3[3])&&isO(row4[3]) ) {
				oWins=1;
		}
				
		// Check diagonals
		if( isX(row1[0])&&isX(row2[1])&&isX(row3[2])&&isX(row4[3]) ||
			isX(row1[3])&&isX(row2[2])&&isX(row3[1])&&isX(row4[0]) ) {
				xWins=1;
		}
		
		if( isO(row1[0])&&isO(row2[1])&&isO(row3[2])&&isO(row4[3]) ||
			isO(row1[3])&&isO(row2[2])&&isO(row3[1])&&isO(row4[0]) ) {
				oWins=1;
		}
		
		////////// If no one won, check if the game is still undecided or not
		if(xWins==0 && oWins==0) {
			for(int j=0;j<N;j++) {
				if(row1[j]=='.' || row2[j]=='.' || row3[j]=='.' || row4[j]=='.') {
					undecided=1;
					break;
				}
			}
		}
		
		// Print outcome
		cout << "Case #" << (i+1) << ": ";
		if(xWins) {
			cout << "X won" << endl;
		}
		else if(oWins) {
			cout << "O won" << endl;
		}
		else if(undecided) {
			cout << "Game has not completed" << endl;
		}
		else {
			cout << "Draw" << endl;
		}
	}
	return 0;
}

bool isX(char c) {
	return c=='X' || c=='T';
}

bool isO(char c) {
	return c=='O' || c=='T';
}

