#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char ** argv)
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	
	int T;
	fin >> T;
	for (int i = 1; i <= T; i++)
	{
		int R = 0, k = 0, N = 0, order = 0;
		fin >> R >> k >> N;
		int g[N];
		for (int j = 0; j < N; j++)
		{
			fin >> g[j];
		}
		
		int costTol = 0;
		
		for (int m = 0; m < R; m++)
		{
			int costTmp = 0, leftGroup = N;
			while (leftGroup > 0 && costTmp <= k)
			{
				costTmp += g[order];
				order = (order + 1) % N;
				leftGroup--;
			}
			
			if (costTmp > k)
			{
				order = (order + N - 1) % N;
				costTmp -= g[order];
			}
			costTol += costTmp;
		}
		
		fout << "Case #" << i << ": " << costTol << endl; 
	}
	return 0;
}
