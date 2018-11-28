#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

bool won(vector<vector<char> > tic, char car, bool& tie);

int main(int argc, char* argv[])
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int t;
	in >> t;
	vector<vector<char> > tic(4,4);
	for (int c=1; c<=t; c++) {
		bool tie(true);
		for (int i=0; i < 4; ++i)
			for (int j=0; j < 4; j++)
				in >> tic[i][j];
		out << "Case #" << c << ": ";
		if(won(tic, 'X', tie)) { 
			out << "X won\n";
		}
		else if (won(tic, 'O', tie)) {out << "O won\n";}
		else if (tie) {out << "Draw\n"; }
		else {out << "Game has not completed\n";}

	}

}//main

bool won(vector<vector<char> > tic, char car, bool& tie) {
	for (int i=0; i < 4; ++i) {
		bool won(true);
		for (int j=0; j < 4; j++) {
			if (tic[i][j] != car && tic[i][j] != 'T')
				won = false;
			if (tic[i][j] == '.') tie = false;
		}
		if (won) return true;
	}
	for (int i=0; i < 4; ++i) {
		bool won(true);
		for (int j=0; j < 4; j++) {
			if (tic[j][i] != car && tic[j][i] != 'T')
				won = false;
		}
		if (won) return true;
	}
	for (int b(0); b <= 1; b++) {
		bool won(true);
		for (int i=0; i<4; i++) {
			if (tic[i][(b?i:(4-i-1))] != car && tic[i][(b?i:(4-i-1))] != 'T')
				won = false;
		}
		if (won) return true;
	}
	return false;

}