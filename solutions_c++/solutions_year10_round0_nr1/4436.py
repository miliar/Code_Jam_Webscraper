//============================================================================
// Name        : SnapperChain.cpp
// Author      : Jinjun.Chen
// Version     :
// Copyright   : jinjunch@gmail.com
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

int getIndexOfPowerConnected(int * snapperStatus, size_t size){
	size_t i;
	for(i = 1; i < size; i++ ) {
		if( snapperStatus[i-1] == 0) break;
	}
	return i-1;
}

void snapTheSnapper(int * snapperStatus, size_t size, size_t index) {
	size_t i;
	if(index >= size) return;
	for(i = 1; i <= index; i++ ) {
		if( snapperStatus[i] == 0) {
			snapperStatus[i] = 1; continue;
		}
		if( snapperStatus[i] == 1) {
			snapperStatus[i] = 0; continue;
		}
	}
}

bool outputStatus(int * snapperStatus, size_t size) {
	size_t i, totalON = 0;
	for(i = 1; i < size; i++ ) {
		//cout << snapperStatus[i] << " ";
		if(snapperStatus[i] == 1) totalON++;
	}
	return (totalON == size-1);
}

size_t getFactor (size_t input){
	size_t result = 1;
	if ( input==0 ) return 1;
	result = getFactor(input-1) * input;
	return result;
}

int main() {
	size_t T_numTestCase = 0, N_snapperNum = 0, K_snapTimes = 0;
	ifstream inFileStrm;
	ofstream outFileStrm;
	size_t i, j, k;
	inFileStrm.open("C:\\Documents and Settings\\jinjun\\workspace\\codeJam2010\\SnapperChain\\A-small-attempt2.in", ifstream::in);
	outFileStrm.open("C:\\Documents and Settings\\jinjun\\workspace\\codeJam2010\\SnapperChain\\output.txt", ifstream::out);

	if(inFileStrm.is_open()) {
		// read-in head line
		inFileStrm >> T_numTestCase;
		//cout << T_numTestCase << endl;

		// read-in testCases
		for(i=0; i<T_numTestCase; i++) {
			inFileStrm >> N_snapperNum;
			inFileStrm >> K_snapTimes;
			//cout << "\n\nInput: N_snapperNum " << N_snapperNum << ", K_snapTimes: " << K_snapTimes << endl;

			// Start guessing here
			int * snapperStatus = new int[N_snapperNum + 1];
			int * pointer = snapperStatus;
			size_t size = N_snapperNum + 1;
			snapperStatus[0] = 1;
			for(j = 1; j < size; j++) {
				snapperStatus[j] = 0;
			}

			//size_t timesOfReset = getFactor(N_snapperNum) * 2;
			//K_snapTimes = K_snapTimes % timesOfReset;
			//cout << "Before operating: "; outputStatus(snapperStatus, size);
			//cout << endl;
			for(k = 0; k < K_snapTimes; k++) {
			   size_t index = getIndexOfPowerConnected(snapperStatus, size);
			   snapTheSnapper(pointer, size, index);
			   //cout << "Index= " << index << "\nAfter operated " << k+1 << " times: ";
			   //outputStatus(pointer, size);
			}
			//cout << "\nFinal status: " << outputStatus(snapperStatus, size);
			if(outputStatus(snapperStatus, size)) {
				cout << "Case #" << i+1 << ":\tON" << endl;
				outFileStrm << "Case #" << i+1 << ":\tON" << endl;
			} else {
				cout << "Case #" << i+1 << ":\tOFF" << endl;
				outFileStrm << "Case #" << i+1 << ":\tOFF" << endl;
			}
			delete snapperStatus;
		}
	} else {
		cout<<"Unable to open this file."<<endl;
	}
	return 0;
}
