#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A.out");
	int t;
	fin >> t;
	for(int testnum = 0; testnum < t; testnum++)
	{
		int n;
		fin >> n;
		vector<int> x, y;
		long long int result = 0;
		int i,j;
		for(i = 0; i < n; i++)
		{
			int tx, ty;
			fin >> tx >> ty;
			x.push_back(tx);
			y.push_back(ty);
		}
		for(i = 0; i < n-1; i++)
			for(j = i+1; j < n; j++)
			{
			if((x[i] > x[j] && y[i] < y[j])||(x[i] < x[j] && y[i] > y[j]))
				result += 1;
			}
		fout << "Case #"<<testnum+1<<": "<<result<<'\n';
	}
	return 0;
}



	