// TaskB.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
using namespace std;

int compare (const void * a, const void * b)
{
  return -( *(int*)a - *(int*)b );
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream input("C-large.in");
	ofstream output;
	output.open("C.out");
	if(input.is_open())
	{
		int T;
		input >> T;
		for(int testi = 0;testi < T; testi++)
		{
			int N;
			/// test case
			input >> N;
			int* c = new int[N];
			for(int j = 0; j<N; j++)
			{
				input >> c[j];
			}
			qsort(c, N, sizeof(int), compare);
			int tmp = 0;
			for(int i = 0; i<N; i++)
				/// count bits
				tmp ^=c[i];
			if(tmp != 0)
				output << "Case #" << testi + 1<<": NO"<<endl;
			else
			{
				unsigned long long sum = 0;
				for(int i = 0; i<N-1; i++)
					sum += c[i];
				output << "Case #" << testi + 1<<": "<<sum<<endl;
			}
			delete[] c;
		}
		input.close();
		output.close();
	}
	else
	{
		cout<<"Input file not found";
		return 1;
	}
	return 0;
}

