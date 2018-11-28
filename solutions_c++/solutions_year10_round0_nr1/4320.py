#include <iostream.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <fstream.h>
#include <math.h>
#include <basetsd.h>

#include <limits>

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
	
	int T;
	
	fin>>T;
	
	for (int c = 1; c <= T; c++)
	{
		int N, Snappers[30], POW[30];
		LONG64 K;

		fin>>N>>K;
		
		for (int i = 0; i < N; i++)
		{
			Snappers[i] = 0;
			POW[i] = 0;
		}

		POW[N-1] = 1;

		while (K > 0)
		{
			for (int i = 0; i < N; i++)
				if (POW[i] == 1)
					Snappers[i] = 1 - Snappers[i];

			for (int i = N-1; i>0; i--)
			{
				if ((POW[i] == 1) && (Snappers[i] == 1))
					POW[i-1] = 1;
				else
					POW[i-1] = 0;
			}

			K--;
		}

		if ((Snappers[0] == 1) && (POW[0] == 1))
			fout<<"Case #"<<c<<": ON"<<endl;
		else
			fout<<"Case #"<<c<<": OFF"<<endl;
	}
	
	fin.close();
	fout.close();
	
	return 0;
}