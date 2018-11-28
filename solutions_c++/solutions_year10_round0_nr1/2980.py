#include "stdafx.h"
#include <math.h>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int test = 1073741824;

	int T;
	cin>>T;

	int N,K;
	vector<bool> results;
	for(int i=0; i<T; i++)
	{
		cin>>N;
		cin>>K;
		int power = (int)pow((float)2, (float)N);

		bool result = false;
		if(K == (power-1))
		{
			result = true;
		}
		else
		{
			K -= (power -1);
			if(K % power == 0)
			{
				result = true;
			}
		}
		results.push_back(result);
	}

	char on[] = "ON\n";
	char off[] = "OFF\n";

	for(int i=0; i<T; i++)
	{
		if(results[i])
			cout<<"Case #"<<i+1<<": "<<on;
		else
			cout<<"Case #"<<i+1<<": "<<off;
	}
	return 0;
}

