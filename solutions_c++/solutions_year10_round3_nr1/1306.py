#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
	int t;
	int n;

	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("A-large.out");

	fin>>t;
	for(int i=0; i<t; i++)
	{
		int sum = 0;

		fin>>n;
		int* a = new int[n];
		int* b = new int[n];
		for(int j=0; j<n; j++)
		{
			fin>>a[j]>>b[j];
		}

		int x = 0;
		int y = x + 1;
		while(y != n)
		{
			if((a[x] > a[y]) && (b[x] < b[y]))
				sum++;
			else if((a[x] < a[y]) && (b[x] > b[y]))
				sum++;

			y++;
			if(y == n)
			{
				x++;
				y = x + 1;
			}
		}
		delete a;
		delete b;

		fout<<"Case #"<<i+1<<": "<<sum<<"\n";
	}

	fin.close();
	fout.close();

	return 0;
}