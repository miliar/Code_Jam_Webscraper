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

struct cell
{
	char type;
	int rc;
	int cc;
	int ldc;
	int rdc;

	cell() : type('.'), rc(1), cc(1), ldc(1), rdc(1) { } 
};


int main()
{
	int nTestCases;
	int n, K;

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
		char carr[102][102];
		cell arr[102][102];

		fscanf (in_file, "%d", &n);
		fscanf (in_file, "%d", &K);

		for (int j=0; j<n; ++j)
			fscanf (in_file, "%s", carr[j]);

		int l=n, m=n;

		for (int j=0; j<n; ++j)
		{
			int len = strlen(carr[j]);

			string str;

			for (int k=len-1;k>=0;--k)
			{
				if (carr[j][k]!='.')
					str.push_back(carr[j][k]);
			}

			l=n;
			for (int k=0; k<str.length(); ++k)
			{
				arr[l][m].type = str.at(k);

				if (arr[l+1][m].type == arr[l][m].type)
					arr[l][m].cc += arr[l+1][m].cc;
				if (arr[l+1][m+1].type == arr[l][m].type)
					arr[l][m].rdc += arr[l+1][m+1].rdc;
				if (arr[l][m+1].type == arr[l][m].type)
					arr[l][m].rc += arr[l][m+1].rc;
				
				--l;
			}

			--m;
		}

		bool br=false, bb=false;
		for (l=n; l>=1; --l)
			for (m=1; m<=n; ++m)
			{
				if (arr[l][m].type != '.' && arr[l][m].type == arr[l+1][m-1].type)
					arr[l][m].ldc += arr[l+1][m-1].ldc;

				if (arr[l][m].cc >= K || arr[l][m].ldc >= K || arr[l][m].rc >= K || arr[l][m].rdc >= K)
				{
					if (arr[l][m].type == 'R')
						br=true;
					if (arr[l][m].type == 'B')
						bb=true;
				}

				if (br && bb)
					break;
			}



		int k1 = 1<<n;
		--k1;

		fprintf (out_file, "Case #%d: ", i);
		if (br && bb)
			fprintf (out_file, "Both\n");
		else
		if (br)
			fprintf (out_file, "Red\n");
		else 
		if (bb)
			fprintf (out_file, "Blue\n");
		else
			fprintf (out_file, "Neither\n");


	}


	fclose(in_file);
	fclose(out_file);

	return 0;
}