#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
	int t; //test case
	int n; //snapper count
	int k; //snapped count
	int x;

	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("A-large.out");

	fin>>t;
	for(int i=0; i<t; i++)
	{
		fin>>n>>k;
		x = (int)(pow((float)2, n));
		if(k%x == x-1)
			fout<<"Case #"<<i+1<<": ON\n";
		else
			fout<<"Case #"<<i+1<<": OFF\n";
	}

	fin.close();
	fout.close();

	return 0;
}

