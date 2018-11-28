#include <iostream>
#include "TicTacToeAnalyzer.h"

using namespace std;


int main(int argc, char* argv[]) {
	if (argc != 3) {
		cerr << "Usage: tictactoe INPUTFILE OUTPUTFILE" << endl;
		return 1;
	}
	TicTacToeAnalyzer* ttta = new TicTacToeAnalyzer(argv[1]);
	//ttta->readFile(argv[1]);
	ttta->analyze();
	ttta->writeFile(argv[2]);
	return 0;
}
