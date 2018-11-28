#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
	int t, n, k;
	bool find=true;
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
	fin>>t;
	for(int i=0; i<t; i++)
	{
		fin>>n>>k;
		if(k % (1<<n)==((1<<n)-1)) fout<<"Case #"<<i+1<<": ON\n";
		else fout<<"Case #"<<i+1<<": OFF\n";
	}
	return 0;
}
