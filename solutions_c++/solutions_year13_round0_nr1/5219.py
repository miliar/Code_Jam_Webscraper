#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

static const int kBoardSize = 4;
static const char kTomek = 'T';

typedef vector<char> charVec;
typedef vector<charVec> charVec2d;

void loadBoard(ifstream& fin, vector<vector<char> > data) {

}

int checkLeft(charVec2d data, int x, int y, char symbol) {
	if(x-1>=0) {
		if(data[x-1][y]==symbol || data[x-1][y]==kTomek) {
			return checkLeft(data,x-1,y,symbol)+1;
		}
		else {
			return 0;
		}
	}
	else {
		return 1;
	}
}

int checkUpLeft(charVec2d data, int x, int y, char symbol) {
	if((x-1>=0) &&(y-1>=0)){
		if(data[x-1][y-1]==symbol || data[x-1][y-1]==kTomek) {
			return checkUpLeft(data,x-1,y-1,symbol)+1;
		}
		else {
			return 0;
		}
	}
	else {
		return 1;
	}
}

int checkUp(charVec2d data, int x, int y, char symbol) {
	if(y-1>=0) {
		if(data[x][y-1]==symbol || data[x][y-1]==kTomek) {
			return checkUp(data,x,y-1,symbol)+1;
		}
		else {
			return 0;
		}
	}
	else {
		return 1;
	}
}

int checkUpRight(charVec2d data, int x, int y, char symbol) {
	if((x+1<kBoardSize) &&(y-1>=0)){
		if(data[x+1][y-1]==symbol || data[x+1][y-1]==kTomek) {
			return checkUpRight(data,x+1,y-1,symbol)+1;
		}
		else {
			return 0;
		}
	}
	else {
		return 1;
	}
}

int main() {
	//variables
	int numberOfGames;
	//load the input
	fstream fin;
	fin.clear();
	fin.open("input.txt");
	ofstream fout;
	fout.open("output.out");
	if(!fin.good()) {
		cout<<"File was bad"<<endl;
		return 0;
	}
		//get the number of boards, n
		fin>>numberOfGames;
		//create a vector of 2d char vectors
		vector<vector<vector<char> > > allBoards(numberOfGames,charVec2d(kBoardSize,charVec(kBoardSize)));
		//for n times get a board from the file and put it in a vector
		for(int i=0;i<numberOfGames;i++) {
			for(int row=0;row<kBoardSize;row++) {
				for(int col=0;col<kBoardSize;col++) {
					fin>>allBoards[i][col][row];
				}
			}
		}
/*		//test: print the boards
		for(int i=0;i<numberOfGames;i++) {
			for(int row=0;row<kBoardSize;row++) {
				for(int col=0;col<kBoardSize;col++) {
					cout<<allBoards[i][col][row];
				}
				cout<<endl;
			}
			cout<<endl;
		}*/
		
	//do connected components
	bool skip = false;
	bool spaceWasEmpty=false;
	for(int boardIndex=0;boardIndex<numberOfGames;boardIndex++) {
		//print generic statement
		fout<<"Case #"<<boardIndex+1<<": ";
		skip = false;
		spaceWasEmpty=false;
		for(int x=0;x<kBoardSize && !skip;x++) {
			for(int y=0;y<kBoardSize && !skip;y++) {
				//check left, up left, up, up right (if in bounds) for the correct symbol
				char thisSymbol = allBoards[boardIndex][x][y];
				if(thisSymbol=='.') {
					spaceWasEmpty = true;
				}
				else if(thisSymbol=='T') {
					if(checkLeft(allBoards[boardIndex],x,y,'X') ==kBoardSize ||
						 checkUpLeft(allBoards[boardIndex],x,y,'X')    ==kBoardSize ||
						 checkUp(allBoards[boardIndex],x,y,'X')        ==kBoardSize ||
						 checkUpRight(allBoards[boardIndex],x,y,'X')   ==kBoardSize ) {
							//we have a winner, print it and skip checking
							fout<<'X'<<" won"<<endl;
							skip = true;
					}
					else if (checkLeft(allBoards[boardIndex],x,y,'O') ==kBoardSize ||
						 checkUpLeft(allBoards[boardIndex],x,y,'O')    ==kBoardSize ||
						 checkUp(allBoards[boardIndex],x,y,'O')        ==kBoardSize ||
						 checkUpRight(allBoards[boardIndex],x,y,'O')   ==kBoardSize ) {
							//we have a winner, print it and skip checking
							fout<<'O'<<" won"<<endl;
							skip = true;
					}
				}
				//if a function returns 4 then there is a winner
				else if(checkLeft(allBoards[boardIndex],x,y,thisSymbol) ==kBoardSize ||
					 checkUpLeft(allBoards[boardIndex],x,y,thisSymbol)    ==kBoardSize ||
					 checkUp(allBoards[boardIndex],x,y,thisSymbol)        ==kBoardSize ||
					 checkUpRight(allBoards[boardIndex],x,y,thisSymbol)   ==kBoardSize ) {
						//we have a winner, print it and skip checking
						fout<<thisSymbol<<" won"<<endl;
						skip = true;
				}
			}
		}
		if(!skip) {
			if(spaceWasEmpty) {
				fout<<"Game has not completed"<<endl;
			}
			else {
				fout<<"Draw"<<endl;
			}
		}
	}
	//if there was no winner, check if the game is a draw or incomplete
fout.close();
	return 0;
}
