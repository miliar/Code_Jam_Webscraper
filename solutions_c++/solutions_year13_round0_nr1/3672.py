#include <iostream>
#include <fstream>

using namespace std;

int nums, dats[16];
int iTable[10][4] = {
	{ 0 , 1 , 2 , 3 } ,
	{ 4 , 5 , 6 , 7 } ,
	{ 8 , 9 , 10, 11} ,
	{ 12, 13, 14, 15} ,
	{ 0 , 4 , 8 , 12} ,
	{ 1 , 5 , 9 , 13} ,
	{ 2 , 6 , 10, 14} ,
	{ 3 , 7 , 11, 15} ,
	{ 0 , 5 , 10, 15} ,
	{ 3 , 6 , 9 , 12} };

int main(int argc, char **argv) {
	ifstream inFile;
	ofstream outFile;
	int imsier;
	bool flag;
	char imsi;

	inFile.open("input.txt");
	outFile.open("output.txt");

	inFile >> nums;
	for(int i = 1 ; i <= nums ; ++i) {
		flag = true;
		for(int j=0 ; j<16 ; ) {
			inFile >> imsi;
			// X - 1 , O - 2 , T - 3 , . - 0
			switch( imsi ) {
			case '.':
				dats[j++] = 0;
				flag = false;
				break;
			case 'X':
				dats[j++] = 1;
				break;
			case 'O':
				dats[j++] = 2;
				break;
			case 'T':
				dats[j++] = 3;
				break;
			}
		}

		// Processing Start
		for( int j = 0 ; j < 10 ; ++j ) {
			imsier = 3;
			for( int k = 0 ; k < 4 ; ++k ) imsier &= dats[iTable[j][k]];
			if ( imsier ) break;
		}

		outFile << "Case #" << i << ": " ;
		switch( imsier ) {
		case 0:
			outFile << (flag ? "Draw" : "Game has not completed") << endl;
			break;
		case 1:
			outFile << "X won" << endl ;
			break;
		case 2:
			outFile << "O won" << endl ;
			break;
		default:
			outFile << "?????" << endl ;
		}
	}

	inFile.close();
	outFile.close();

	return 0;
}