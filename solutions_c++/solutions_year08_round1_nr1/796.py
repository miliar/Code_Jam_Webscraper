// Template for code jam!
//
#include "stdafx.h"
//#include <math.h>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
//#include <map>
//#include <queque>
//#include <stack>
//#include <set>

using namespace std;

//other functions may go here!
bool sortSmallBig (int& a, int& b){ return a < b; }
bool sortBigSmall (int& a, int& b){ return b < a; }
//main function!

int _tmain(int argc, _TCHAR* argv[])
{
    ifstream inputFile("A-small.in");
    ofstream outputFile("A-small.out", std::ios::trunc);
	//ifstream inputFile("A-large.in");
    //ofstream outputFile("A-large.out", std::ios::trunc);
    if((!inputFile.is_open()) || (!outputFile.is_open()))
      return -1;  //error openning input/output file!

	int numIterations;
	//string receive; getline(inputFile, receive); numIterations = atoi(receive.c_str());
	inputFile >> numIterations;
	int numCases = 1;
	vector<int> vecA, vecB;
	long int numItems, item, acum, x;
	while(numCases <= numIterations)
	{
		if(numCases == 125)
			int a = 1;

		vecA.clear();
		vecB.clear();
		//parsing code goes here
		inputFile >> numItems;
		for(x=0; x< numItems; x++)
		{
			inputFile >> item;
			vecA.push_back(item);
		}
		for(x=0; x< numItems; x++)
		{
			inputFile >> item;
			vecB.push_back(item);
		}
		//problem code goes here
		sort(vecA.begin(), vecA.end(), sortSmallBig);
		sort(vecB.begin(), vecB.end(), sortBigSmall);
		acum = 0;
		for(x=0; x<numItems; x++)
			acum+= vecA[x]*vecB[x];
		outputFile << "Case #" << numCases << ": " << acum << endl;
			numCases++;
	}
	return 0;
}

