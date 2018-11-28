//
//  main.cpp
//  RecycledNumbers
//
//  Created by Justin Schmidt on 4/14/12.
//  Copyright (c) 2012 Grizzly. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <set>

using namespace std;


unsigned long numRecycled(long long a, long long b);

int main(int argc, const char * argv[])
{
	ifstream input("input.txt");
	
	int numCases = 0;
	input >> numCases;
	
	for (int i = 0; i < numCases; ++i)
	{
		long long a, b;
		input >> a;
		input >> b;
		unsigned long result = numRecycled(a, b);
		cout << "Case #" << (i + 1) << ": " << result << endl;
	}
	
	return 0;
}

unsigned long numRecycled(long long a, long long b)
{
	unsigned long count = 0;
	for (long long n = a; n < b; ++n)
	{
		if (n < 10)
			continue;
		
		int length = 0;
		int temp = n;
		int multiplier = 1;
		while (temp > 0)
		{
			++length;
			multiplier *= 10;
			temp /= 10;
		}
		multiplier /= 10;
		
		
		set<long long> s;
		long long m = n;
		for (int i = 0; i < length; ++i)
		{
			long long shift = m % 10;
			shift *= multiplier;
			m /= 10;
			m += shift;
			
			if (s.find(m) != s.end())
				continue;
			else
				s.insert(m);
			
			if (m <= b && m > n)
				++count;
		}
	}
	return count;
}








