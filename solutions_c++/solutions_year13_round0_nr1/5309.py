#include <iostream>
#include <string>

using namespace std;

//global
char board[5][6];

bool winrow(char c)
{
	for(int k=0; k<4; k++)
		if ( board[k][0] == c && 
		     board[k][1] == c && 
			 board[k][2] == c && 
			 board[k][3] == c)
			return true;
	
	return false;
}


bool wincol(char c)
{
	for(int k=0; k<4; k++)
		if ( board[0][k] == c && 
		     board[1][k] == c && 
			 board[2][k] == c && 
			 board[3][k] == c)
			return true;
	
	return false;
}

bool windiag(char c)
{
	if ( board[0][0] == c && 
		 board[1][1] == c && 
		 board[2][2] == c && 
		 board[3][3] == c)
			return true;
			
	if ( board[0][3] == c && 
		 board[1][2] == c && 
		 board[2][1] == c && 
		 board[3][0] == c)
			return true;
	
	return false;
}


bool finddot(){
	for(int k=0; k<4; k++)
		for(int j=0; j<4; j++){
			if (board[k][j] == '.'){
				return true;
			}
		}
		
	return false;
}

void findt(int &x, int &y){
	for(int k=0; k<4; k++)
		for(int j=0; j<4; j++){
			if (board[k][j] == 'T'){
				x = k;
				y = j;
				return;
			}
		}
		
	return;
}


int main () 
{
  int T;

  int tx, ty;
  
  
  cerr << "Hello World" << endl;
  cin >> T;
  cin.getline(board[5],6);
  
  cerr << T << " test cases" << endl;

  //MAIN PROCESS LOOP
  for(int i=1; i<=T; i++)  
  {
	cerr << "Case #" << i << endl;
	// read input
	for (int k=0; k<5; k++){
		cin.getline(board[k],6);
		//cerr << "%" << board[k] << endl;
	}
	// initialize
	tx = ty = -1;	
	
	// output input
	cerr << "board" << endl;
	for (int k=0; k<4; k++)
		cerr << board[k] << endl;
	findt(tx, ty);
	cerr << "T at " << tx << ", " << ty << endl;
	cerr << "dotd = " << boolalpha << finddot() << endl;
	
	
	// Process
	cout << "Case #" << i << ": ";
	
	if (tx != -1) { board[tx][ty] = 'X'; } 
	if (winrow('X') || wincol('X') || windiag('X') ){
		cout << "X won" << endl;
	}
	else { 
	    if (tx != -1) { board[tx][ty] = 'O'; } 
		if (winrow('O') || wincol('O') || windiag('O') ){
		cout << "O won" << endl;
		
	    } 
	    else if ( finddot() ) {
		   cout << "Game has not completed" << endl;
	    }
	    else{
		   cout << "Draw" << endl;
	    }
	}
	// answer
    cerr << endl;
  }
}
