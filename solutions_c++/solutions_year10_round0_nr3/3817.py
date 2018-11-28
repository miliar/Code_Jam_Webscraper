// GoogleCodeJam2010QualificationQ3.cpp : Defines the entry point for the console application.
//

// GoogleCodeJam2009Q1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <math.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <queue>

using namespace std;

bool JudgeEqual(queue<int> Qorigin, queue<int> myqueue)
{
	int sizeQ = myqueue.size();
	for (int i=0; i<sizeQ; i++)
	{
		int temp1 = myqueue.front();
		int temp2 = Qorigin.front();
		myqueue.pop();
		Qorigin.pop();
		if (temp1 != temp2)
			return false;
	}
	return true;
}


int EarningComputation(int R, int k, int N, queue<int> myqueue)
{
	int totalEarn=0;
	int sumQ = 0;
	int sizeQ = myqueue.size();
	queue<int> Qcopy(myqueue);
	for (int i=0 ; i<sizeQ ; i++)
	{
		sumQ += Qcopy.front();
		Qcopy.pop();
	}
	if (sumQ <= k)
	{
		totalEarn = R * sumQ;
		return totalEarn;
	}

	queue<int> Qorigin(myqueue);
	
	vector<int> tempR(1,0); 
	for (int i=0; i <R; i++)
	{
		int temp;
		int tempAll = 0;
		while (tempAll + myqueue.front() <= k)
		{
			temp = myqueue.front();
			myqueue.pop();
			tempAll += temp;
			myqueue.push(temp);
		} 
		totalEarn += tempAll;
		if (i<N )
		{
			tempR.push_back(tempR.back()+tempAll);
			if ( JudgeEqual(Qorigin, myqueue) )
				return totalEarn * (R/(i+1)) +	tempR[R%(i+1)];		
		}

	}
	return totalEarn;
}

int _tmain(int argc, _TCHAR* argv[])
{
	
	ifstream in;
	in.open("C-small-attempt0.in");

	ofstream out;
	out.open("C-small-attempt0.out");

	int T;
	
	// Read the parameter T from file
	in >> T;

	for (int i=0; i<T; i++)
	{
		int R, k, N;
		in >> R >> k >> N;
		queue<int> myqueue;
		int temp;
		for (int j=0; j<N; j++)
		{
			in >> temp;
			myqueue.push(temp);
		}
		out <<"Case #"<<i+1<<": "<< EarningComputation(R, k , N, myqueue) <<endl;
	}
	


	in.close();
	out.close();
	//cout << Words.size();

	return 0;
}

