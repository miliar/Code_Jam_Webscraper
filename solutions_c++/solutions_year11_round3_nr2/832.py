

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

double func(long int L, long long int t, long int N, long int C, vector<long int> v)
{
	double start = (t * 0.5);
	
	long int sum = 0;
	//long int sum1; 

	long int i;

	long int interval = 0; 

	for(i = 0; i < N; i++)
	{
		sum += (v[i % C]);
		if( sum > start)
			break;
		interval++;
	}

	vector<long int> d;
	long int overallDistance = 0; 
	for(i = 0; i < N; i++)
	{
		//d.push_back(v[i % C]);
		overallDistance += (v[i % C]);
	}

	for(i = interval; i < N; i++)
	{
		d.push_back(v[i % C]);
		//overallDistance += (v[i % C]);
	}

	if(start >= overallDistance)
	{
		return overallDistance *2.0;
	}
	else if(L == 0)
	{
		return overallDistance *2.0;
	}
	else
	{
		d[0] = sum - start;
	
		sort(d.begin(), d.end()); 
		
		double dist = t; 
		for(i = d.size() - 1; i > -1; i--)
		{
			if((d.size() -1 - i) < L)
			{
				dist += d[i];
			}
			else dist += 2.0 * d[i];

		}

		return dist;
	}


}

long int main()
{
	ifstream in ("B-small-attempt1.in");
	ofstream out ("B-small-attempt1.out");

	string s;

	long int T;
	in >> T;

	getline(in, s); 
	
	long int i, j;
	long int temp; 

	for(i = 0; i < T; i++)
	{
		if(i == 79)
			int mm = 0;
		long int L, N, C;
		long long int t;
		in >> L >> t >> N >> C; 

		vector<long int> v;

		for(j = 0; j < C; j++)
		{
			in >> temp;
			v.push_back(temp); 
		}

		out << "Case #" << i + 1 << ": " << (long int)func(L, t, N, C, v) << endl; 
		getline(in, s); 
		
	}

	return 0;
}

