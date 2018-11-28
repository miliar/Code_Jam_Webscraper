// prob2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include <math.h>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int C, N;

	ifstream from("input.txt");
	ofstream to("output.txt");

	string input;
	getline(from, input);
	C = atoi(input.c_str());

	vector<unsigned __int64> vec, diffVec;


	for(int c = 0; c < C; c++)
	{
		input.clear();
		vec.clear();
		diffVec.clear();

		getline(from, input);
		istringstream ist(input);
		ostringstream ost;

		ist >> N;

		for(int n = 0; n < N; n++)
		{
			unsigned __int64 tmp = 0;

			//string num;
			//ist >> num;		

			//int bits = 0;
			//for(string::reverse_iterator iter = num.rbegin(); iter != num.rend(); iter++)
			//{
			//	tmp += (*iter - 48) * (unsigned __int64)pow(10.0, (double)bits);
			//	bits++;
			//}

			ist >> tmp;
			vec.push_back(tmp);
		}

		vector<unsigned __int64>::iterator iter = vec.begin(), iter2 = vec.begin();
		for(++iter2; iter2 != vec.end(); iter++, iter2++)
		{
			if(*iter > *iter2)
				diffVec.push_back(*iter - *iter2);
			else
				diffVec.push_back(*iter2 - *iter);
		}

		unsigned __int64 largest = 0, smallest = 0xffffffffffffffff;
		
		// findout the largest and smallest elements:
		for(iter = diffVec.begin(); iter != diffVec.end(); iter++)
		{
			if(*iter > largest)
				largest = *iter;
			if(*iter && *iter < smallest)
				smallest = *iter;
		}

		do
		{
			for(iter = diffVec.begin(); iter != diffVec.end(); iter++)
			{
				if(*iter > smallest)
				{
					*iter = *iter - *iter / smallest * smallest;
				}
			}

			largest = 0, smallest = 0xffffffffffffffff;
			for(iter = diffVec.begin(); iter != diffVec.end(); iter++)
			{
				if(*iter > largest)
					largest = *iter;
				if(*iter && *iter < smallest)
					smallest = *iter;
			}

		}while(largest != smallest);

		smallest = 0xffffffffffffffff;
		for(iter = vec.begin(); iter != vec.end(); iter++)
		{
			if(*iter < smallest)
				smallest = *iter;
		}

		__int64 gcd = largest, anni = 0, i =0;
		while(++i)
		{
			anni = gcd * i - smallest;
			if(anni >= 0)
				break;
		}	
	
		ost<<"Case #"<< c+1 <<": "<< anni <<'\n';
		to << ost.str();

	}

	from.close();
	to.close();

	return 0;
}

