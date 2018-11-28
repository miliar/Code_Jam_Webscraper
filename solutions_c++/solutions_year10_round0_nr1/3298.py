#include "stdafx.h"
#include <cstdlib>
#include <iostream>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <ctime> 
#include <string>
#include <fstream>   // file I/O
#include <iomanip>   // format manipulation

using namespace std;


void SolveGooglePuzzle1()
{
	ifstream inFile;  // declarations of streams inFile and outFile
	ofstream outFile;
	long inputSize;
	long count = 0;
	long N = 0, K = 0;
	inFile.open("C:\\googlecode\\input.txt", ios::in);    // open the streams
	outFile.open("C:\\googlecode\\output.txt", ios::out);
	inFile >> inputSize;
	count = 0;
	while(!inFile.eof())
	{
	  inFile >> N >> K;
	  if((N == 0) && (K == 0))
		  break;
	  long Nrange = 1 << N;
	  bool turnedOn = ((K % Nrange) == (Nrange - 1));
	  outFile << "Case #" << (count + 1) << ": " << (turnedOn ? "ON" : "OFF") << endl;
	  count++;
	}
	inFile.close();   // close the streams
	outFile.close(); 
	cout << "Outfile written\n";
}

int _tmain(int argc, _TCHAR* argv[])
{	
	SolveGooglePuzzle1();
}