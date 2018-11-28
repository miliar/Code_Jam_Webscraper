//============================================================================
// Name        : Snapper.cpp
// Author      : Jaqoup
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	unsigned int N, K;
	int loop;
	fin>>loop;
	for (int i=0; i<loop;i++)
	{
		bool power = true;
		fin>>N>>K;
		fout<<"Case #"<<i+1<<": ";
		for  (unsigned int j=0;power && j<N;j++)
		if (!(K>>(j) & 1))
			power = false;

		if (power)
			fout<<"ON\n";
		else
			fout<<"OFF\n";
	}
	return 0;
}
