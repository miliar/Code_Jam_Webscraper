#include <iostream>
#include <fstream>
#include <list>
#include <string>
#include <sstream>
#include "BigUnsigned.hh"
#include "BigIntegerAlgorithms.hh"
#include <vector>
using namespace std;

BigUnsigned getBigUnsigned(string str) {
	BigUnsigned num = 0;
	for (int i=0; i < str.size(); i++) {
		char ch = str.at(i);
		int val = atoi(&ch);
		num = num*10 + val;
	}
	return num;
}

string getString(BigUnsigned num) {
	string str;
	while (num > 0) {
		int i = (num % BigUnsigned(1000000)).toInt();
		stringstream strstr;
		strstr << i;
		string s = strstr.str();
		s.append(str);
		str = s;
		num /= 1000000;
	}
	return str;
}


int main(int argc, char **argv) {
	ifstream inputFile("B-small.in", ios_base::in);
	ofstream outputFile("output.txt", ios_base::out);
	int noOfCases, N;

	inputFile >> noOfCases;
	for (int caseNo = 0; caseNo < noOfCases; caseNo++) {
		inputFile >> N;
		vector<BigUnsigned> numList;
		for (int i = 0; i < N; i++) {
			string str;
			inputFile >> str;
			numList.push_back(getBigUnsigned(str));
		}
		BigUnsigned T;
		if ( numList[1] > numList[0] ) {
			T = numList[1] - numList[0] ;
		} else {
			T = numList[0] - numList[1];
		}
		for (int i = 2; i < N; i++ ) {
			T = gcd(T, ((numList[i] < numList[i-1]))? (numList[i-1]-numList[i]):(numList[i]-numList[i-1]));
		}

		BigUnsigned remainder = numList[0] % T;

		

		outputFile << "Case #" << (caseNo+1) << ": " << getString(T-remainder) << endl;
	}
}
