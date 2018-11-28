#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int a1[60][60];
int a2[60][60];
int main() {
	ifstream ifs("input.txt");
	ofstream ofs("output.txt");

	int T;
	ifs >> T;
	for(int i = 1; i <= T; ++i)
	{
		int K, N;
		memset(a1, 0, sizeof(a1));
		memset(a2, 0, sizeof(a2));
		ifs >> N >> K;

		for(int i1 = 0; i1 < N; ++i1)
		{
			string str;
			ifs >> str;
			for(int i2 = 0; i2 < N; ++i2)
			{
				if(str.at(i2) == '.')
					a1[i1][i2] = 0;
				else if(str.at(i2) == 'R')
					a1[i1][i2] = 1;
				else if(str.at(i2) == 'B')
					a1[i1][i2] = 2;
			}
		}
		
		for(int i1 = 0; i1 < N; ++i1)
		{
			int count = 0;
			for(int i2 = N-1; i2 >= 0; --i2)
			{
				if(a1[i1][i2] == 1)
					a2[N-1-count++][N-1-i1] = 1;
				else if(a1[i1][i2] == 2)
					a2[N-1-count++][N-1-i1] = 2;
			}
		}

		bool fb = false;
		bool fr = false;
	
		for(int i1 = 0; i1 < N; ++i1)
		{
			for(int i2 = 0; i2 < N; ++i2)
			{
				if(a2[i1][i2] == 0)
					continue;
				bool ff1 = true, ff2 = true, ff3 = true, ff4 = true;
				for(int i3 = 0; i3 < K; ++i3)
				{
					if((i2 + i3 >= N) || (a2[i1][i2+i3] != a2[i1][i2]))
						ff1 = false;
					if((i1 + i3 >= N) || (a2[i1+i3][i2] != a2[i1][i2]))
						ff2 = false;
					if((i2 + i3 >= N) || (i1 + i3 >= N) || (a2[i1+i3][i2+i3] != a2[i1][i2]))
						ff3 = false;
					if((i2 - i3 < 0) || (i1 + i3 >= N) || (a2[i1+i3][i2-i3] != a2[i1][i2]))
						ff4 = false;
				}
				if(ff1 || ff2 || ff3 || ff4)
				{
					if(a2[i1][i2] == 1)
						fr = true;
					else 
						fb = true;
				}
			}
		}

		ofs << "Case #" << i << ": ";
		if(fb && fr)
			ofs << "Both" << endl;
		else if(fb)
			ofs << "Blue" << endl;
		else if(fr)
			ofs << "Red" << endl;
		else
			ofs << "Neither" << endl;
	}
	
	ifs.close();
	ofs.close();
	
	return 0;
}