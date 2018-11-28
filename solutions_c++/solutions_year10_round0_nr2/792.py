//============================================================================
// Name        : FairWarning.cpp
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

//generate Great Common Measure
unsigned long long int gcm(unsigned long long int num1, unsigned long long int num2){

	unsigned long long int diff;

	cout << "num1 = " << num1 << " num2 = " << num2 << endl;

	while(1) {
		if(num1 > num2){
			diff = num1 - num2;
			if(!(num1 % diff) && !(num2 % diff)){
				return diff;
			} else {
				num1 = diff;
			}
		} else if(num1 < num2){
			diff = num2 - num1;
			if(!(num1 % diff) && !(num2 % diff)){
				return diff;
			} else {
				num2 = diff;
			}
		} else {
			return num1;
		}
	}

	return 0;
}

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

	unsigned int C;
	unsigned int N;
	unsigned long long int t[1000];
	unsigned long long int diff[999];
	unsigned long long int T;
	unsigned long long int y;
	unsigned long long int offset;

	inFile >> C;
	cout << "C = " << C << endl;

	for(unsigned int x = 1; x <= C; x++){
		cout << "[Case " << x << "]" << endl;
		inFile >> N;
		cout << "N = " << N << endl;

		cout << "t = ";
		for(unsigned int i = 0; i < N; i++){
			inFile >> t[i];
			if(inFile.fail()){
				cout << "inFile error: " << strerror(errno) << endl;
				return -4;
			}
		    cout << t[i] << " ";
		}
		cout << endl;

		//bubble sort fot t[i]
		for(unsigned int i = 0; i < N-1; i++){
			for(unsigned int j = 0; j < N-1-i; j++){
				//convert
				if(t[j] > t[j+1]){
					unsigned long long int buf;
					buf= t[j+1];
					t[j+1] = t[j];
					t[j] = buf;
				}
			}
		}

		//diff with the next
		for(unsigned int i = 0; i < N-1; i++){
			//diff with the next
			diff[i] = t[i+1] - t[i];
		}

		//bubble sort fot diff[i]
		for(unsigned int i = 0; i < N-2; i++){
			for(unsigned int j = i; j < N-2-i; j++){
				//convert
				if(diff[j] > diff[j+1]){
					unsigned long long int buf;
					buf= diff[j+1];
					diff[j+1] = diff[j];
					diff[j] = buf;
				}
			}
		}

		if(N == 2){	//N = 2‚Ì‚Æ‚«
			T = diff[0];

		} else {	//N > 3‚Ì‚Æ‚«
			//GCM
			T = gcm(diff[0], diff[1]);
			for(unsigned int i = 2; i < N-1; i++){
				T = gcm(T, diff[2]);
			}
			cout << "T = " << T << endl;
		}

		//output
		unsigned long long int a = t[0] / T + ((t[0] % T) ? 1 : 0);
		y = a * T - t[0];
		cout << "y = " << y << endl;
		outFile << "Case #" << x << ": " << y << endl;
	}

	cout << "finish!!" << endl;


	inFile.close();
	outFile.close();

	return 0;
}
