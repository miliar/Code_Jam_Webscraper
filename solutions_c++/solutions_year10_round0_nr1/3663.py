//============================================================================
// Name        : Algorithms.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include "KiloManX.h"
#include "Snapper.h"

using namespace std;
#include <fstream.h>
#include <sstream>
int main() {
	cout << "Hello World!!!" << endl; // prints Hello World!!!
	//KiloManX k;
	int T =4;
	int *N;// = {1,1,4,4};
	int *K;// = {0,1,0,47};
	char str[10000];
	bool firstLine = true;
	ifstream myReadFile;
	ofstream myWriteFile;
	myReadFile.open("A-large.in");
	myWriteFile.open("A-large.out");
	int i=0;
	char output[100];
	if (myReadFile.is_open() && myWriteFile.is_open()) {
		while (!myReadFile.eof()) {

			myReadFile.getline(str,100);
			if (firstLine){
				T = atoi(str);
				N = new int[T];
				K = new int[T];
				firstLine = false;
			} else {
				//cout << "1: " << sub << " 2: " << sub1;
				istringstream iss(str);
				char sub[12], sub1[12];
				iss >> sub;
				iss >> sub1;
				N[i] = atoi(sub);
				K[i] = atoi(sub1);
				i++;
			}
		}
	}
	Snapper s;

//	for (int i=0;i<T;i++)
//	{
//		myWriteFile << i << ": 1:" << N[i] << " 2: " << K[i] << endl;
//	}
	s.isOn(myWriteFile,T,N,K);
	myReadFile.close();
	myWriteFile.close();




	//	string w1[] = {"1542", "7935", "1139", "8882"};


	exit(0);
}
