#include <iostream>
#include <cmath>
#include <fstream>
#include <cstdlib>

using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	
	int T;
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		fout << "Case #" << i+1 << ": ";
		int N;
		fin >> N;
		char c[N];
		int pos[N];
		for(int j = 0; j < N; j++)
			fin >> c[j] >> pos[j];
		
		int ans = 0;
		
		int currPosO = 1;
		int currPosB = 1;
		
		int extraMovesO = 0;
		int extraMovesB = 0;
		
		for(int j = 0; j < N; j++)
		{
			if(c[j] == 'O')
			{
				int dist = abs(pos[j]-currPosO) + 1;
				int extrasUsed = min(extraMovesO, dist-1);
				extraMovesO = 0;
				dist -= extrasUsed;
				extraMovesB += dist;
				ans += dist;
				currPosO = pos[j];
			}
			else
			{
				int dist = abs(pos[j]-currPosB) + 1;
				int extrasUsed = min(extraMovesB, dist-1);
				extraMovesB = 0;
				dist -= extrasUsed;
				extraMovesO += dist;
				ans += dist;
				currPosB = pos[j];
			}
		}
		fout << ans << endl;
	}
	return 0;
}