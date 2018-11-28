#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	int a[31];
	a[1] = 1;
	int i;
	for( i = 1; i < 30; i++)
		a[i+1] = a[i] * 2 + 1;
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int t, n, k;

	fin >> t;

	for( i = 1; i <= t; i++)
	{
		fin >> n >> k;

		if( k % (a[n] + 1) == a[n] )
			fout << "Case #" << i << ": ON" << endl;
		else
			fout << "Case #" << i << ": OFF" << endl;
	}
	
	return 0;
}