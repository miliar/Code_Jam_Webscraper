//============================================================================
// Name        : jam_test.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
//#include <sstream>
//#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


int main(int argc, char** argv)
{

	if(argc!=3)
	{
		cout << "Usage:" << endl;
		cout << "jam_test infile outfile" << endl;
		return 0;
	}

	ifstream infile(argv[1]);
	ofstream outfile(argv[2]);

	if(!infile)
		cout << "Input file open error!" << endl;

	if(!outfile)
		cout << "Output file open error!" << endl;

	int nCase;

	int a,b;
	int i,j;
	int ans[10];
	int ansNum = 0;

	infile >> nCase ;
	//cout << "Case Num:" << nCase << endl;

	for(int iCase=0; iCase<nCase; iCase++)
	{
		cout << "Case #" << iCase+1 << ": " << endl;
		outfile << "Case #" << iCase+1 << ": ";

		infile >> a;
		infile >> b;

		cout << a << " " << b << endl;

		int count = 0;
		int testMin = 10;
		int testMax = 10;

		while( (a/testMax) || (b/testMax) )
			testMax *= 10;
		testMax /= 10;

		int testA, testB;
		bool same = false;

		for(i=a; i<b; i++)
		{
			ansNum = 0;

			for(j=i+1; j<=b; j++)
			{
				testA = 10;
				testB = testMax;

				if(i != j)
				{
					while(testB >= 10)
					{
						if( (i%testA == j/testB)
								&& (i/testA == j%testB) )
						{
							same = false;

							for(int ansi=0; ansi<ansNum; ansi++)
							{
								if(j == ans[ansi])
								{
									same = true;
									break;
								}
							}

							if(!same)
							{
								ans[ansNum] = j;
								ansNum++;
								count++;
							}
							cout << count << ">> " << i << "," << j << endl;
						}

						testA *= 10;
						testB /= 10;
					}
				}

			}
		}

		outfile << count << endl;
		//outfile << endl;

	}

	return 0;
}
