// codejam3.cpp : Defines the entry point for the console application.
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <math.h>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
    long long T, R, k, N;

    
    ifstream input("C-small-attempt0.in");
	ofstream output ("C-small-attempt0.out");
    input >> T;
	for (long long g=0; g < T; g++)
	{
	long long counter=0;
    input >> R;
    input >> k;
    input >> N;

    vector<long long> groups;

    for (long long i=0; i < N; i++)
    {
        long long val;
        input >> val;
        groups.push_back(val);
    }        

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
        
        for (long long j=0; j < count; j++)
        {
            groups.push_back(groups.front());
            groups.erase(groups.begin());
        }       
		counter += sum;
    }
	output << "Case #" << g+1 << ": " << counter << endl;
	}
    system("PAUSE");
    return 0;
}
