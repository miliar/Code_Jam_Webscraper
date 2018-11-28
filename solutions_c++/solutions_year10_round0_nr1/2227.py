//============================================================================
// Name        : SnapperChain.cpp
// Author      : 1k1k1k
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>

#include <math.h>
#include <string.h>
#include <errno.h>

using namespace std;

int main(int argc, char *argv[]) {

	ifstream inFile;
	ofstream outFile;

	if(argc < 2){return -1;}

	//input file name
	inFile.open(argv[1]);
	if(!inFile){
		cout << "inFile open error ! " << argv[1] << ": " << strerror(errno) << endl;
		return -2;}

	//output file name
	outFile.open(argv[2]);
	if(!outFile){
		cout << "outFile open error ! " << argv[2] << ": " << strerror(errno) << endl;
		return -3;
	}

	unsigned int T;
	unsigned int N;
	unsigned int K;
	unsigned int x;
	unsigned int y;

	//input T
	inFile >> T;
	cout << "T = " << T << endl;

	for(unsigned int x = 1; x <= T; x++){
		//input
		cout << "[Case " << x << "]" << endl;
		inFile >> N >> K;
		cout << "N = " << N << " K = " << K << endl;

		//
		unsigned long long int count;
		count = pow(2, N);
		cout << "count = " << count << endl;
		if( !((K + 1) % count) ){
			y = 1;
		} else {
			y = 0;
		}

		//output
		if(y == 0){
			cout << "y = OFF" << endl;
			outFile << "Case #" << x << ": OFF" << endl;
		} else {
			cout << "y = ON" << endl;
			outFile << "Case #" << x << ": ON" << endl;
		}
	}

	return 0;
}
