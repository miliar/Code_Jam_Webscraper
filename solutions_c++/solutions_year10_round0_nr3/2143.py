//============================================================================
// Name        : ThemePark.cpp
// Author      : 1k1k1k
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>

#include <string.h>
#include <errno.h>

using namespace std;

int main(int argc, char *argv[]) {

	int T = 0;	//case
	int R = 0;	//running R times
	int k = 0;	//limit size
	int N = 0;	//number of groups
	int g[1000];	//the size of a group
	ifstream inFile;
	ofstream outFile;

	if(argc < 2){return -1;}

	//input file name
	inFile.open(argv[1]);
	if(!inFile){
		cout << "inFile open error ! " << argv[1] << endl;
		return -2;}

	//output file name
	outFile.open(argv[2]);
	if(!outFile){
		cout << "outFile open error ! " << argv[2] << ": " << strerror(errno) << endl;
		return -3;
	}

	inFile >> T;
	cout << "T = " << T << endl;

	//case T
	for(int i = 0; i < T; i++){
		cout << "[case " << i+1 << "]" << endl;

		inFile >> R >> k >> N;
		cout << "R = " << R << std::endl;
		cout << "k = " << k << std::endl;
		cout << "N = " << N << std::endl;

		cout << "g = ";
		for(int j = 0; j < N; j++){
			inFile >> g[j];
			cout << g[j] << " ";
		}
		cout << endl;

		int gPoint = 0;
		int gStart = 0;
		int sizeCount = 0;
		int money = 0;

		//running
		for(int r = 0; r < R; r++){
			sizeCount = 0;
			gStart = gPoint;

			//size count
			do{
				sizeCount += g[gPoint];
				gPoint = (gPoint + 1 < N) ? gPoint + 1 : 0;
			} while( (sizeCount + g[gPoint] <= k) && (gPoint != gStart) );

            money += sizeCount * 1;//size * 1euro
		}

		//output fare
		cout << "money = " << money << endl;
		outFile << "Case #" << i+1 << ": " << money << endl;
	}

	cout << "finish!!" << endl;

	inFile.close();
	outFile.close();

	return 0;
}
