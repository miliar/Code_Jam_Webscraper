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

int FindHighestScore(int sum, bool surprise)
{
	if(surprise) {
		if(sum % 3 == 0) return (sum+3)/3;
		if(sum % 3 == 1) return (sum+2)/3;
		if(sum % 3 == 2) return (sum+4)/3;
	} else {
		if(sum % 3 == 0) return sum/3;
		if(sum % 3 == 1) return (sum+2)/3;
		if(sum % 3 == 2) return (sum+1)/3;
	}
}

int main()
{
	int numTest;
	char num[4];
	ifstream in;
	in.open("B-large.in");
	in.getline(num, 4);
	numTest = atoi(num);
	ofstream out;
	out.open("output.txt");
	char* temp;
	for(int i=0; i<numTest; i++) {
		char buf[1024];
		in.getline(buf, 1024);
		temp = strtok(buf, " ");
		int N = atoi(temp);
		temp = strtok(NULL, " ");
		int S = atoi(temp);
		temp = strtok(NULL, " ");
		int p = atoi(temp);
		vector<int> scores;
		vector<bool> surpriseflag;
		temp = strtok(NULL, " ");
		while(temp != NULL) {
			scores.push_back(atoi(temp));
			surpriseflag.push_back(false);
			temp = strtok(NULL, " ");
		}
		out << "Case #" << i+1 << ": ";
		int countAbovep = 0;
		for(int j=0; j<N; j++) {
			if(scores[j] == 0 || scores[j] == 1 || scores[j] == 29 || scores[j] == 30)
				continue;
			if(scores[j] % 3 == 0) {
				if(scores[j]/3 == p-1 && S > 0) {
					surpriseflag[j] = true;
					S--;
				}
			} else if(scores[j] % 3 == 1) {
				continue;
			} else {
				if((scores[j]+1)/3 == p-1 && S > 0) {
					surpriseflag[j] = true;
					S--;
				}
			}
		}
		int ind = 0;
		while(S > 0) {
			if(scores[ind] == 0 || scores[ind] == 1 || scores[ind] == 29 || scores[ind] == 30) {
				ind++;
				continue;
			}
			if(surpriseflag[ind] == false) {
				surpriseflag[ind] = true;
				S--;
			}
			ind++;
		}
		for(int j=0; j<N; j++) {
			int high = FindHighestScore(scores[j], surpriseflag[j]);
			if(high >= p)
				countAbovep++;
		}
		out << countAbovep;
		if(i != numTest-1)
			out << endl;
	}
	in.close();
	out.close();
	return 0;
}