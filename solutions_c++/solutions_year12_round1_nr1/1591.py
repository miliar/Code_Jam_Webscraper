// Test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <string.h>
#include <vector>

using namespace std;

double FindKeyStroke(long A, long B, long numBS, const vector<double>& prob)
{
	return (2*B-A+2+2*numBS) - (B+1)*prob[A-numBS-1];
}

int main()
{
	int numTest;
	char num[4];
	ifstream in;
	in.open("A-small-attempt0.in");
	in.getline(num, 4);
	numTest = atoi(num);
	ofstream out;
	out.open("output.txt");
	char* temp;
	for(int i=0; i<numTest; i++) {
		char buf[1024];
		in.getline(buf, 1024);
		temp = strtok(buf, " ");
		long A = atol(temp);
		temp = strtok(NULL, " ");
		long B = atol(temp);
		char buff[1024];
		in.getline(buff, 1024);
		vector<double> prob;
		double multprob = 1.0;
		temp = strtok(buff, " ");
		while(temp != NULL) {
			multprob *= atof(temp);
			prob.push_back(multprob);
			temp = strtok(NULL, " ");
		}
		cout << "Case #" << i+1 << ": ";
		double min = std::numeric_limits<double>::infinity();
		for(long numBS=0; numBS<A; numBS++) {
			double ks = FindKeyStroke(A, B, numBS, prob);
			if(ks < min) {
				min = ks;
			}
		}
		if(B+2 < min) {
			min = B+2;
		}
		printf("%.6f", min);
		if(i != numTest-1)
			cout << endl;
	}
	in.close();
	out.close();
	int dumb;
	scanf("%d", &dumb);
	return 0;
}