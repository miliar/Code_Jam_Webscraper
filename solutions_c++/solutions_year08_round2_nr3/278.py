// C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <stdio.h>



int _tmain(int argc, _TCHAR* argv[])
{
	FILE * fout;
	fout = fopen("d:\\C.out","w+b");
	std::string str_in = "d:\\C-small-attempt1.in";
	std::ifstream is(str_in.c_str());

	int N;
	is >> N;//number of cases
	int c[5000];
	int g[5000];

	for (int i=0; i<N; i++)
	{
		printf("%d",i);
		int K,n;
		is >> K;
		is >> n;
		for (int j =0; j<n; j++)
		{
			is >> c[j];
		}

		for (int j = 0; j<K; j++)
		{
			g[j] = K;
		}

		int x=1;
		int y=0;
		int z=0;
		while (x<K)
		{
			if (g[y]==K) z++;
			if (x==z) 
			{
				g[y] = x;
				x++;
				z=0;
			}
			y++;
			if (y==K) y=0;
		}
		
		fprintf(fout,"Case #%d: ",i+1);
		for (int j=0; j<n; j++)
		{
			fprintf(fout,"%d ",g[c[j]-1]);
		}
		fprintf(fout,"\r\n");

	}

	fclose(fout);
	return 0;
}

