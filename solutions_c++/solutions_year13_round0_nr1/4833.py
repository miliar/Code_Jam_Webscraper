#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

int ctr = 1;

int checkGameOverRow( string &s ) {
	int xctr = 0;
	int octr = 0;
	int dctr = 0;
	int tctr = 0;

	for ( int i = 0; i < 4; i++ ) {
		if ( s[i] == 'X' ) {
			xctr++;
		} else if ( s[i] == 'O' ) {
			octr++;
		} else if ( s[i] == '.' ) {
			dctr++;
		} else if( s[i] == 'T' ) {
			tctr++;
		}
	}

	if ( xctr == 4 || (xctr == 3 && tctr == 1 ) ) {
		return 1;
	} else if ( octr == 4 || (octr == 3 && tctr == 1 ) ) {
		return 2;
	} else if ( dctr != 0 ) {
		return 3;
	}
}

int checkGameOverCol( vector<string> &b, int col ) {
	int xctr = 0;
	int octr = 0;
	int dctr = 0;
	int tctr = 0;

	for ( int i = 0; i < 4; i++ ) {
		if ( b[i][col] == 'X' ) {
			xctr++;
		} else if ( b[i][col] == 'O' ) {
			octr++;
		} else if ( b[i][col] == '.' ) {
			dctr++;
		} else if( b[i][col] == 'T' ) {
			tctr++;
		}
	}

	if ( xctr == 4 || (xctr == 3 && tctr == 1 ) ) {
		return 1;
	} else if ( octr == 4 || (octr == 3 && tctr == 1 ) ) {
		return 2;
	} else if ( dctr != 0 ) {
		return 3;
	}
}
void decision( vector<string> &b ) {
	
	bool emptyCell = false;
						// checking rows for game end 
	for ( int i = 0; i < 4; i++ ) {
		int dec = checkGameOverRow(b[i]);
		
		if ( dec == 1 ) {
			cout << "Case #" << ctr << ": X won" << endl; 	
			return;
		} else if ( dec == 2 ) {
			cout << "Case #" << ctr << ": O won" << endl; 	
			return;
		} else if ( dec == 3 ) {
			emptyCell = true; 
		}
	}

						// checking cols for game end 
	for ( int i = 0; i < 4; i++ ) {
		int dec = checkGameOverCol(b, i);
		
		if ( dec == 1 ) {
			cout << "Case #" << ctr << ": X won" << endl; 	
			return;
		} else if ( dec == 2 ) {
			cout << "Case #" << ctr << ": O won" << endl; 	
			return;
		} else if ( dec == 3 ) {
			emptyCell = true; 
		}
	}
						// checking diagonals for game end
						// diag 1	
	int xctr = 0;
	int octr = 0;
	int tctr = 0;

	for ( int i = 0; i < 4; i++ ) {

		if ( b[i][i] == 'X' ) {
			xctr++;
		} else if( b[i][i] == 'O' ) {
			octr++;
		} else if ( b[i][i] == 'T' ) {
			tctr++;
		}
	}

	if ( xctr == 4 || ( xctr == 3 && tctr == 1 ) ) {
		cout << "Case #" << ctr << ": X won" << endl; 	
		return;
	} else if ( octr == 4 || ( octr == 3 && tctr == 1 ) ) {
		cout << "Case #" << ctr << ": O won" << endl; 	
		return;
	} 

						// diag 2
	xctr = 0;
	octr = 0;
	tctr = 0;

	int j = 3;
	for ( int i = 0; i < 4; i++ ) {

		if ( b[i][j] == 'X' ) {
			xctr++;
		} else if( b[i][j] == 'O' ) {
			octr++;
		} else if ( b[i][j] == 'T' ) {
			tctr++;
		}

		j--;
	}

	if ( xctr == 4 || ( xctr == 3 && tctr == 1 ) ) {
		cout << "Case #" << ctr << ": X won" << endl; 	
		return;
	} else if ( octr == 4 || ( octr == 3 && tctr == 1 ) ) {
		cout << "Case #" << ctr << ": O won" << endl; 	
		return;
	} 

	if ( emptyCell ) {
		cout << "Case #" << ctr << ": Game has not completed" << endl; 	
		return;
	} else {
		cout << "Case #" << ctr << ": Draw" << endl;
	}
}

int main()
{
	int t;
	cin >> t;

	for ( int i = 0; i < t; i++ ) {
		vector<string> b;

		for ( int j = 0; j < 4; j++ ) {
			string s;
			cin >> s;
			
			b.push_back(s);
		}
		
		decision(b);
		ctr++;
	}


	return 0;
}
