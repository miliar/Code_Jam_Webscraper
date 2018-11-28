#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
	ifstream inFile(argv[1]);
	ofstream outFile("result.out");
	unsigned caseNum(0);
	inFile >> caseNum;
	for( unsigned i = 0; i != caseNum; ++i ) {
		// read file
		char oneCase[4][4];
		int oneCaseSub[4][4] = {0};
		bool emptyB(false);
		for( unsigned j = 0; j != 4; ++j ) {
			for( unsigned k = 0; k != 4; ++k ) {
				inFile >> oneCase[j][k];
				if( oneCase[j][k] == 'X' ) {
					oneCaseSub[j][k] = 1;
				} else if( oneCase[j][k] == 'O' ) {
					oneCaseSub[j][k] = 2;
				} else if( oneCase[j][k] == 'T' ) {
					oneCaseSub[j][k] = 3;
				} else {
					emptyB = true;
				}
			}
		}
		// get result
		int result(0);
		for( unsigned j = 0; result == 0 && j != 4; ++j ) {
			result = (oneCaseSub[j][0] & oneCaseSub[j][1] & oneCaseSub[j][2] & oneCaseSub[j][3]);
			if( result == 0 ) {
				result = (oneCaseSub[0][j] & oneCaseSub[1][j] & oneCaseSub[2][j] & oneCaseSub[3][j]);
			}
		}
		if( result == 0 ) {
			result = (oneCaseSub[0][0] & oneCaseSub[1][1] & oneCaseSub[2][2] & oneCaseSub[3][3]);
			if( result == 0 ) {
				result = (oneCaseSub[0][3] & oneCaseSub[1][2] & oneCaseSub[2][1] & oneCaseSub[3][0]);
			}
		}
		// output
		outFile << "Case #" << i+1 << ": ";
		if( result == 1 ) {
			outFile << "X won";
		} else if( result == 2 ) {
			outFile << "O won";
		} else if( result == 0 && emptyB) {
			outFile << "Game has not completed";
		} else {
			outFile << "Draw";
		}
		outFile << endl;
	}
	outFile.close();
}