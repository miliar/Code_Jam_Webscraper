// Problem C. Candy Splitting.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <stack>
#include <string>
#include <queue>
#include <set>
#include <algorithm>
#include <iterator>
using namespace std;

#define Sz 1100

int main()
{
	int arr[Sz];
	int num_of_cases,
		num_of_numbers,
		index1,
		index2,
		xor_sum = 0,
		the_sum = 0,
		min = 0;
	memset(arr,0,sizeof(arr));
	string file_name("input_2.txt");
	ofstream output("out_2.txt");
	ifstream input(file_name.c_str());
	input>>num_of_cases;

	for (index1 = 1; index1 <= num_of_cases; index1++)
	{
		input>>num_of_numbers;
		min = 1000000;
		xor_sum = 0;
		the_sum = 0;
		memset(arr,0,sizeof(arr));
		for(index2 = 1; index2 <= num_of_numbers; index2++)
		{
			input>>arr[index2];
			xor_sum = xor_sum^arr[index2];
			the_sum += arr[index2];
			if (min > arr[index2])
			{
				min = arr[index2];
			}
		}
		if (xor_sum == 0)
		{
			output<<"Case #"<<index1<<": "<<(the_sum - min)<<endl;
		}
		else
		{
			output<<"Case #"<<index1<<": NO\n";
		}
	}

	

	return 0;
}

