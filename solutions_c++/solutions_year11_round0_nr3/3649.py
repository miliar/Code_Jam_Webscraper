/* 
 * File:   main.cpp
 * Author: tom
 *
 * Created on 8 May 2011, 3:22 AM
 */

#include <cstdlib>
#include <fstream>
#include <iostream>
#define in cin
using namespace std;

const int DIGS = 22;

int placeFreq[DIGS];
int singleDigit[DIGS];
/*
 * 
 */
int main()
{
	//ifstream in("in.txt");

	singleDigit[0] = 1;
	for (int i = 1; i < DIGS; i++)
	{
		singleDigit[i] = singleDigit[i-1] << 1;
	}

	int numT;

	in >> numT;

	for (int t = 0; t < numT; t++)
	{
		for (int i = 0; i < DIGS; i++)
		{
			placeFreq[i] = 0;
		}

		int n;
		int min = 1000*1000*1000;
		int total = 0;
		
		in >> n;

		for (int i = 0; i < n; i++)
		{
			int x;
			in >> x;

			total += x;
			if (min > x) min = x;

			for (int d = 0; d < DIGS; d++)
			{
				if (x & singleDigit[d])
				{
					placeFreq[d]++;
				}
			}
		}

		bool impossible = false;

		for (int i = 0; i < DIGS; i++)
		{
			if (placeFreq[i] % 2 != 0)
			{
				impossible = true;
				break;
			}
		}

		cout << "Case #" << t + 1 << ": ";

		if (impossible)
			cout << "NO";
		else
			cout << total - min;

		cout << "\n";
	}

	return 0;
}


