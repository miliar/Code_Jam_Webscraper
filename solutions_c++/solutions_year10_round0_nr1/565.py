// Snapper Chain.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>

int main()
{
	FILE* infile = fopen("A-large.in", "r");
	FILE* outfile = fopen("large.txt", "w");
	int t;
	fscanf(infile, "%d", &t);
	for (int i = 0; i < t; i++)
	{
		int n, k;
		fscanf(infile, "%d %d", &n, &k);

		if ((k + 1) % (1 << n) == 0) fprintf(outfile, "Case #%d: ON\n", i + 1);
		else fprintf(outfile, "Case #%d: OFF\n", i + 1);
	}
}