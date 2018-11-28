// CodeOverflow.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
// Standard libraries
#include <string>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <queue>

// `BigIntegerLibrary.hh' includes all of the library headers.
#include "BigIntegerLibrary.h"
#include<limits>
using namespace std;






// GoogleCodeJam2010QualificationQ3.cpp : Defines the entry point for the console application.
//

// GoogleCodeJam2009Q1.cpp : Defines the entry point for the console application.
//





BigInteger EarningComputation(int R, int k, int N, queue<int> myqueue)
{
	BigInteger totalEarn=0;
	BigInteger sumQ = 0;
	int sizeQ = myqueue.size();

	queue<int> Qcopy(myqueue);
	for (int i=0 ; i<sizeQ ; i++)
	{
		sumQ += Qcopy.front();
		Qcopy.pop();
		if (sumQ > k)
			break;
	}
	if (sumQ <= k)
	{
		totalEarn =  (BigInteger) R*sumQ;
		return totalEarn;
	}

	queue<int> Qorigin(myqueue);
	
	vector<BigInteger> tempR(1,0); 
	int location = 0;
	int* Array = new int[N];
	for (int i=0; i<N; i++)
		Array[i]= 0;

	int limit = R;

	for (int i=0; i <limit; i++)
	{
		int temp;
		int tempAll = 0;
		while (tempAll + myqueue.front() <= k)
		{
			temp = myqueue.front();
			myqueue.pop();
			tempAll += temp;
			myqueue.push(temp);
			location ++;
		} 
		totalEarn += tempAll;
		tempR.push_back(tempR.back()+tempAll);

		if (limit == R)
		{
			if (Array[location%N]==0)
				Array[location%N] = i+1;
			else
			{
				totalEarn =  tempR[Array[location%N]] + ( totalEarn - tempR[ Array[location%N] ] ) * ( (R -Array[location%N] ) / (i+1-Array[location%N]) ); 
				limit -= Array[location%N];
				limit %= (i+1-Array[location%N]) ;
				limit += i+1;
				//cout<<limit<<endl;
			}
		}

		//cout<<totalEarn<<endl;
		

	}
	return totalEarn;
}

int _tmain(int argc, _TCHAR* argv[])
{
	
	ifstream in;
	in.open("C-large.in");

	ofstream out;
//	out.open("C-small-attempt0.out");
	out.open("C-large.out");

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




/*
The original sample program produces this output:

3141592653589793238462643383279
314424
313894
83252135
1185
134
0xFF
0xFF00FFFF
0xFF00FF00
0x1FFFE00000
0x3F
314^0 = 1
314^1 = 314
314^2 = 98596
314^3 = 30959144
314^4 = 9721171216
314^5 = 3052447761824
314^6 = 958468597212736
314^7 = 300959139524799104
314^8 = 94501169810786918656
314^9 = 29673367320587092457984
314^10 = 9317437338664347031806976
12
8
1931

*/
