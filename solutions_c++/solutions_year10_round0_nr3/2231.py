#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
	int t; //test case
	int r; //R times in a day
	int k; //k people at once
	int n; //groups count

	ifstream fin;
	fin.open("C-small.in");
	ofstream fout;
	fout.open("C-small.out");

	fin>>t;
	for(int i=0; i<t; i++)
	{
		int sum = 0; //number of Euros

		fin>>r>>k>>n;
		int* g = new int[n];
		for(int j=0; j<n; j++)
		{
			fin>>g[j];
		}

		int x = 0; //first of Queue
		int y = 0; //current of Queue
		int z = 0; //people count
		for(int j=0; j<r; j++)
		{
			x = y;
			while(k >= z+g[y])
			{
				z += g[y++];
				y = y%n;
				if(x == y)
					break;
			}
			sum += z;
			z = 0;
		}
		delete g;

		fout<<"Case #"<<i+1<<": "<<sum<<"\n";
	}

	fin.close();
	fout.close();

	return 0;
}

