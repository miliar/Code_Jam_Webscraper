// Magicka.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int tc, t, totalCombine, totalOppose, textLength, startOppose = -1, ansIndex = 0;
	char currChar = '-';
	char combine[4], oppose[4], text[20], ans[20];

	fscanf(fp, "%d", &t);

	// Loop for each test cases
	for(tc=1;tc<=t;tc++) 
	{
		// Clear data
		currChar = '-';
		totalCombine = totalOppose = textLength = ansIndex = 0;
		startOppose = -1;
		memset(combine, 0, sizeof(combine));
		memset(oppose, 0, sizeof(oppose));
		memset(text, 0, sizeof(text));
		memset(ans, 0, sizeof(ans));

		// Combine
		fscanf(fp, "%d", &totalCombine);

		if (totalCombine > 0)
		{
			fscanf(fp, "%s", &combine);	
			combine[3] = NULL;
		}

		// Oppose
		fscanf(fp, "%d", &totalOppose);

		if (totalOppose > 0)
		{
			fscanf(fp, "%s", &oppose);	
			oppose[3] = NULL;
		}

		// String to determine
		fscanf(fp, "%d", &textLength);

		if (textLength > 0)
		{
			fscanf(fp, "%s", &text);	
			text[10] = NULL;
		}

		for(int i = 0; i < textLength; i++)
		{
			currChar = text[i];

			// check combine
			if ( totalCombine > 0 &&
				 (ans[ansIndex - 1] == combine[0] && currChar == combine[1]) ||
				 (ans[ansIndex - 1] == combine[1] && currChar == combine[0]) )
			{
				ans[ansIndex - 1] = combine[2];

				if(startOppose == ansIndex - 1) 
					startOppose = -1;
				
				continue;
			}

			// check oppose
			if ( totalOppose > 0 && 
				 (currChar == oppose[0] || currChar == oppose[1]) )
			{
				if(startOppose < 0)
				{
					startOppose = ansIndex;
					ans[ansIndex++] = text[i];
				}
				else
				{
					// Clear list
					if ( (currChar == oppose[0] && ans[startOppose] == oppose[1]) ||
						 (currChar == oppose[1] && ans[startOppose] == oppose[0]) )
					{
						ansIndex = 0;
						startOppose = -1;
					}
					else
					{
						ans[ansIndex++] = text[i];
					}
				}

				continue;
			}

			ans[ansIndex++] = text[i];
		}

		ans[ansIndex] = NULL;

		// Print to output file
		fprintf(ofp, "Case #%d: [", tc);

		for (int j = 0; j < ansIndex; j++)
		{
			if ( j == 0)
				fprintf(ofp, "%c", ans[j]);
			else
				fprintf(ofp, ", %c", ans[j]);
		}

		fprintf(ofp, "]\n");
	}

	return 0;
}

