#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

char winner(char a, char b, char c, char d){
	if(a=='T') a = b;
	else if(b=='T') b = a;
	else if(c=='T') c = a;
	else if(d=='T') d = a;
	if((a==b)&&(b==c)&&(c==d) && a!='.') return a;
	else return 0;
}

char findWinner(char inputBoard[][4]){
	char victor=0;
	for(int i=0; i<4; i++){
		if(victor=winner(inputBoard[0][i],inputBoard[1][i],inputBoard[2][i],inputBoard[3][i])) return victor;
	}
	for(int i=0; i<4; i++){
		if(victor=winner(inputBoard[i][0],inputBoard[i][1],inputBoard[i][2],inputBoard[i][3])) return victor;
	}
	if(victor=winner(inputBoard[0][0],inputBoard[1][1],inputBoard[2][2],inputBoard[3][3])) return victor;
	victor=winner(inputBoard[3][0],inputBoard[2][1],inputBoard[1][2],inputBoard[0][3]);
	return victor;
}

int main(int argc, char const *argv[]){
	if(argc != 2){
		cout<<"Error in Input"<<endl;
		return 0;
	}
	ifstream inFile;
	ofstream outFile;
	inFile.open(argv[1]);
	outFile.open("output.txt", ios::trunc | ios::out);
	if(!(inFile.is_open() && outFile.is_open()) ){
		cout << "can't open files"<<endl;
		return 0;
	}

	int N;
	char board[4][4];
	char gameWinner;
	bool endedEarly;
	inFile >> N;
	cout << "Running through " << N << " Iterations" << endl;
	for(int count=0; count<N; count++){
		endedEarly = false;
		gameWinner = 0;
		for(int i=0; i<16; i++){
			char tmp=inFile.get();
			while(tmp == '\n') tmp = inFile.get();
			board[i/4][i%4] = tmp;
			if(tmp == '.') endedEarly |= true;
		}
		gameWinner = findWinner(board);

		if(gameWinner){
			cout << "Case #" << count+1 << ": " << gameWinner << " won" << endl;
			outFile << "Case #" << count+1 << ": " << gameWinner << " won" << endl;
		} else if (endedEarly){
			cout << "Case #" << count+1 << ": " << "Game has not completed" << endl;
			outFile << "Case #" << count+1 << ": " << "Game has not completed" << endl;
		} else {
			cout << "Case #" << count+1 << ": " << "Draw" << endl;
			outFile << "Case #" << count+1 << ": " << "Draw" << endl;
		}
	}
	inFile.close();
	outFile.close();
	return 0;
}
