/*
 * main.cc
 *
 *  Created on: May 7, 2010
 *      Author: elden
 */

#include <iostream>
#include <fstream>
using namespace std;


int main()
{
	ifstream inFile("A-large.in");
	ofstream outFile("A-large.out");
	int T;
	inFile >> T;
	for (int i=0;i<T;i++) {
		int N;
		long K;
		inFile >> N >> K;

		long maxN1 = 1 << N;

		string result;
		if ((K+1) % maxN1 == 0)
			result = "ON";
		else
			result = "OFF";

		outFile << "Case #" << i+1 <<": " << result <<endl;
	}
	return 0;
}
