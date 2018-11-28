// codejam3.cpp : Defines the entry point for the console application.
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <stdlib.h>
#include <math.h>

using namespace std;

long long found(vector< vector <long long> > list, vector<long long> groups)
{
	if (list.size() == 0)
		return -1;
	for (long long i=0; i < list.size(); i++)
	{
		if (list[i] == groups)
			return i;
	}
	return -1;
}

int _tmain(int argc, _TCHAR* argv[])
{
    long long T, R, k, N;
	
    ifstream input("C-large.in");
	ofstream output ("C-large.out");
    input >> T;
	for (long long g=0; g < T; g++)
	{
		long long counter=0, final=0;
		input >> R;
		input >> k;
		input >> N;
 
		vector<long long> groups;
		vector<long long> individual_sum;
		vector < vector<long long> > list;
		long long occur;
		bool done=false;

		for (long long i=0; i < N; i++)
		{
			long long val;
			input >> val;
			groups.push_back(val);
		}        
		list.push_back(groups);
		for (long long i=0; i < R; i++)
		{
			long long sum=0, count=0, val=0;
			for (long long j=0; j < N; j++)
			{
				if (count == groups.size())
					break;
				if (sum < k)
				{
				   sum += groups[j];
				   count++;
				}
	            
				if (sum > k)
				{
						sum -= groups[j];
						count--;
						break;
				}
				else if (sum >= k)
					 break;
			}

			if (count != N)
			{
				for (long long j=0; j < count; j++)
				{
					groups.push_back(groups.front());
					groups.erase(groups.begin());
				}
			}
			counter += sum;
			individual_sum.push_back(sum);
			occur = found(list, groups);
			if (occur == -1)
			{
				list.push_back(groups);
				//cout << i <<" " << sum << endl;
			}
			else 
			{
				if (i+1 != R)
					done = true;
				break;
			}
		}

		if (done)
		{
			final += counter;
			counter = 0;
			for (long long i=occur; i < individual_sum.size(); i++)
				counter += individual_sum[i];
			long long remain = R-individual_sum.size();
			long long rem = remain % (list.size()-occur);
			final += (remain / (list.size()-occur)) * counter;
			for (long long i=0; i < rem; i++)
				final += individual_sum[i+occur];
		}
		else final = counter;
		output << "Case #" << g+1 << ": " << final << endl;

	}
    return 0;
}
