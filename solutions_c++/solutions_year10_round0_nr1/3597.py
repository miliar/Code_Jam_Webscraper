// chain.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <tchar.h>
#include <math.h>
#include <fstream>
#include <iostream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin;
	char garbage[256];
	long long T, N;
	long long K;


	fin.open(argv[1]);

	fin >> T;

	for(long long i=0; i<T; i++)
	{
		fin >> N >> K;
		fin.getline(garbage, 256); //advance to next line

		bool bLightOn = false;
		//generated series by hand, used wolfram alpha to generate closed form
		int nSolution = pow((float)2, (float)N)-1;
		if(K==nSolution)
			bLightOn = true;
		else if(K>nSolution)
		{
			//generated series by hand, used wolfram alpha to generate closed form		
			if(0==(K+1)%(nSolution+1))
				bLightOn = true;
		}
		


		cout << "Case #" << i+1 << ": " << (bLightOn ? "ON" : "OFF") << endl;
	}


	return 0;
}

