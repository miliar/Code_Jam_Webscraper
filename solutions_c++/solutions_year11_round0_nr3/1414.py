#include <iostream>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <map>
#include <string>

using namespace std;

int main()
{
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");
	
	int T;
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		fout << "Case #" << i+1 << ": ";
		
		int N;
		fin >> N;
		
		long long minVal = 99999999;
		long long xr = 0;
		long long total = 0;
		
		for(int j = 0; j < N; j++)
		{
			long long tmp;
			fin >> tmp;
			xr ^= tmp;
			minVal = min(minVal,tmp);
			total += tmp;
		}
		if(xr > 0)
			fout << "NO\n";
		else fout << total-minVal << endl;
	}
	return 0;
}