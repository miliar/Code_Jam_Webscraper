#include <iostream>
#include <fstream>
using namespace std;

int T, N, C[1001];
void main(void)
{
	ifstream fin("C-large.in");
	ofstream fout("Output.txt");
	fin >> T;
	int i;
	for( i = 0; i < T; ++i )
	{
		fin >> N;
		int j, cry, min = 1000001, sum = 0;
		for( j = 0; j < N; ++j )
			fin >> C[j];

		cry = C[0];
		for( j = 1; j < N; ++j )
			cry ^= C[j];
		if( cry )
			fout << "Case #" << i+1 << ": NO" << endl;
		else
		{
			for( j = 0; j < N; ++j )
			{
				sum += C[j];
				if( min > C[j] )
					min = C[j];
			}
			fout << "Case #" << i+1 << ": "<< sum - min <<endl;
		}
	}
}
