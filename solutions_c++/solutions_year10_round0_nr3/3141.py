// Q3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("C-small-attempt0.in");
	ofstream out ("C-small-attempt0.out");
	

	int t;


	in >> t >> ws;

	for (int i =0;i<t;i++)
	{
		unsigned int r,k,n;
	unsigned long long euro=0;

		in >> r >> k >> n >>ws;
	unsigned int* g = new unsigned int[n];

		for (int j=0;j<n;j++)
			in >> g[j] >> ws;

		unsigned int* group = new unsigned int[n];
		unsigned int* index = new unsigned int[n];
		for (int j=0;j<n;j++)
		{
			group[j]=0;
			for (int l =j;;l++)
			{
				if (l>=n&&l%n==j)
				{			
					index[j]=j;
					break;
				}
				l%=n;
				
				if (group[j]+g[l]>k)
				{
					index[j]=l;
					break;
				}
				else
					group[j]+=g[l];
			}
			
			
		}

		int pos = 0;
		for (unsigned int j = 0;j<r;j++)
		{
			euro+=group[pos];
			pos = index[pos];
		}
		cout << "Case #" << i+1 <<": " << euro << endl;
		out << "Case #" << i+1 <<": " << euro << endl;


		delete group;
		delete index;
		delete g;
		//for (int j = 0;j<n;j++)
		//	cout << group[j] << " ";
		//cout << endl;
		//for (int j = 0;j<n;j++)
		//	cout << index[j] << " ";
		
	}

	in.close();
	out.close();

	return 0;
}