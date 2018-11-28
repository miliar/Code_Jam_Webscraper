#include <iostream>
#include <stdio.h>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int nTestCases;
	int n, k;

	FILE *in_file;
	FILE *out_file;

	in_file = fopen("prob1_in.txt", "r");
	out_file = fopen("prob1_out.txt", "w+");

#define in_file stdin
#define out_file stdout

	if (in_file == NULL || out_file==NULL)
		return 0;

	fscanf(in_file, "%d\n", &nTestCases);

	for (int i=1; i<=nTestCases; ++i)
	{
		fscanf (in_file, "%d", &n);
		fscanf (in_file, "%d", &k);

		int k1 = 1<<n;
		--k1;

		fprintf (out_file, "Case #%d: %s\n", i, (((k & k1)==k1)? "ON" : "OFF"));
	}


	fclose(in_file);
	fclose(out_file);

	return 0;
}