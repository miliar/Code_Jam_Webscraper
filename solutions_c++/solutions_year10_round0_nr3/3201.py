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

//
using namespace std;

typedef map<long, long> HashLong;

void FindProfitInThisRound(long k, long N, long *g, long currentIndex, long *moveFwdBy, long *sum)
{
	*moveFwdBy = 0;
	*sum = 0;
	while((*sum < k) && (*moveFwdBy < N))
	{
		*sum += g[currentIndex];
		currentIndex = (currentIndex + 1) % N;
		(*moveFwdBy)++;
	}
	if(*sum > k)
	{
		if(currentIndex == 0)
			currentIndex = N - 1;
		else 
			currentIndex--;
		*sum = *sum - g[currentIndex];
		(*moveFwdBy)--;
	}
}


long SolveGooglePuzzle2(long R, long k, long N, long *g)
{
	long profit = 0; 
	long currentIndex = 0;
	
	HashLong sumHash, moveFwdByHash;
	for(long i = 0; i < R; i++)
	{
		long moveFwdBy = 0, sum = 0;
		HashLong::iterator foundInMoveFwd = moveFwdByHash.find(currentIndex);
		HashLong::iterator foundInSumHash = sumHash.find(currentIndex);
		if((foundInMoveFwd != moveFwdByHash.end()) &&
		   (foundInSumHash != sumHash.end()))
		{
			moveFwdBy = foundInMoveFwd->second;
			sum = foundInSumHash->second;
		}
		else
		{
			FindProfitInThisRound(k, N, g, currentIndex, &moveFwdBy, &sum);
			moveFwdByHash.insert(pair<long, long>(currentIndex, moveFwdBy));
			sumHash.insert(pair<long, long>(currentIndex, sum));
		}
		profit += sum;
		currentIndex = (currentIndex + moveFwdBy) % N;
	}
	return profit;
}

void ReadAndSolveGooglePuzzle2()
{
	ifstream inFile;  // declarations of streams inFile and outFile
	ofstream outFile;
	long inputSize;
	long count = 0;
	long N = 0, R = 0, k = 0, g[1000];
	inFile.open("C:\\googlecode\\input2.txt", ios::in);    // open the streams
	outFile.open("C:\\googlecode\\output2.txt", ios::out);
	inFile >> inputSize;
	count = 0;
	while(!inFile.eof() && (count < inputSize))
	{
	  inFile >> R >> k >> N;
	  
	  for(long i = 0; i < N; i++)
	  {
		  inFile >> g[i];
	  }

	  outFile << "Case #" << (count + 1) << ": " << SolveGooglePuzzle2(R, k, N, g) << endl;
	  count++;
	}
	inFile.close();   // close the streams
	outFile.close(); 
	cout << "Outfile written\n";
}


int _tmain(int argc, _TCHAR* argv[])
{	
	ReadAndSolveGooglePuzzle2();
}