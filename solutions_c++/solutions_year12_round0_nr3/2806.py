// Recycled Numbers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <math.h>
#include <string.h>


int shift(int source, int num)
{
	int base = (int)pow(10.0, num);
	int r = source % base;
	int q = source / base;
	int t = (int)log10((double)q) + 1;
	base = (int)pow(10.0, t);
	return r * base + q;
}


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *inFile = fopen("input.txt", "r");
	FILE *outFile = fopen("output.txt", "w");

	int n, a, b;

	fscanf(inFile, "%d", &n);
	for(int i = 0; i < n; i++)
	{
		fscanf(inFile, "%d %d", &a, &b);
		int len = (int)log10((double)a);
		int ans = 0;
		for(int j = a; j <= b; j++)
		{
			int list[20];
			for(int z = 0; z < len; z++)
			{
				int m = shift(j, z+1);
				list[z] = m;
				int flag = false;
				for(int w = 0; w < z; w++)
					if(list[w] == m)
					{
						flag = true;
						break;
					}
				if(!flag && m <= b && m > j)
					ans++;
			}
		}
		fprintf(outFile, "Case #%d: %d\n", i+1, ans);
	}
	return 0;
}

