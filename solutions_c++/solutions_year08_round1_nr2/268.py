
#include <algorithm>
//#include <iostream>
#include <vector>
//#include <string>
#include <fstream>
using namespace std;


int main()
{
	ifstream infile;
	infile.open("B-large.in.txt");
	ofstream outfile;
	outfile.open("B-large.out.txt");
	
	int C, N, M, T;
	int i, j, k, x, y;

	vector<int> own;
	vector<vector<int>> custom;
	
	infile>>C;

	i = 0;
	while (i<C)
	{
		infile>>N>>M;
		own.resize(N);
		for (j=0; j<N; j++) own[j] = 0;

		custom.resize(M);
		for (j=0; j<M; j++)
		{
			custom[j].resize(N);
			for (k=0; k<N; k++) custom[j][k] = -1;
			
			infile>>T;
			
			bool has1 = false;
			bool has0 = false;
			int only;
			for (k=0; k<T; k++)
			{
				infile>>x>>y;
				custom[j][x-1] = y;
				
				if ( y == 0)
					has0 = true;
				else
				{
					has1 = true;
					only = x;
				}
			}
			if ( has1 && !has0)
				own[only-1] = 1;
		}
		//change
		while (1)
		{
			bool done = false;
			for (j=0; j<M; j++)
			{
				bool satif = false;
				for (k=0; k<N; k++)
				{
					if (custom[j][k] == own[k])
					{
						satif = true;
						break;
					}
				}
				if (! satif)
				{
					for (k=0; k<N; k++)
					{
						if (custom[j][k] == 1 && own[k] == 0)
						{
							own[k] = 1;
							done = true;
						}
					}
				}
			}
			int c=0;
			for (j=0; j<N; j++)
			{
				c += own[j];
			}
			if (!done || c==N)
			{
				break;
			}

		}
		


		//check
		int count = 0;
		for (j=0; j<M; j++)
		{
			bool satif = false;
			for (k=0; k<N; k++)
			{
				if (custom[j][k] == own[k])
				{
					satif = true;
					break;
				}
			}
			if (satif)
				count++;
		}
		
		outfile<<"Case #"<<i+1<<": ";
		if (count == M)
		{
			
			for (j=0; j<N; j++)
			{
				outfile<<own[j]<<' ';
			}
		}
		else
			outfile<<"IMPOSSIBLE";
		outfile<<endl;

		i++;
	}

	infile.close();
	outfile.close();

	return 0;
}

