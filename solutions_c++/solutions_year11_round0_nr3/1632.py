#include <fstream>
#include <iostream>

using namespace std;

ifstream fin("cs.in");
ofstream fout("cs.out");


int main()
{
	int T, N, i, j;
	unsigned value, res = 0, min, maxPile = 0;

	fin >> T;

	for(i = 1; i <= T; i ++)
	{
		res = 0;
		fin >> N;
		fin >> value;
		min = value;
		res ^= value;
		maxPile = value;

		for(j = 1; j < N; j ++)
		{
			fin >> value;
			res ^= value;
			maxPile += value;
			if(value < min)
				min = value;
		}
		
		if(res == 0)
		{
			fout << "Case #" << i << ": " << maxPile - min << endl;
		}
		else
		{
			fout << "Case #" << i << ": " << "NO" << endl;
		}
	}
}
