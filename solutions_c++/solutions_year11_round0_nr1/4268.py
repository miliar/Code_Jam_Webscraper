// BotTrust.cpp : Defines the entry point for the console application.
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
	
	int i, j, t, n, tc;
	int cnt = 0, turn = 0, currPos_O = 1, currPos_B = 1;
	char prevTurn = 'A', currTurn = 'A';
	bool isDupTurn = false;
	int numData = 0, dest = 0, diff = 0;

	fscanf(fp, "%d", &t);

	// Loop for each test cases
	for(tc=1;tc<=t;tc++) 
	{
		fscanf(fp, "%d", &numData);	
		
		cnt = turn = 0;
		currPos_O = currPos_B = 1;
		prevTurn = currTurn = 'A';

		for ( j = 0; j < numData; j++ )
		{
			fscanf(fp, " %c  %d", &currTurn, &dest);

			isDupTurn = ( currTurn == prevTurn )  ? true : false;
			prevTurn = currTurn;

			if( currTurn == 'O')
			{
				diff = abs(dest - currPos_O);
				currPos_O = dest;
			}
			else if ( currTurn == 'B' )
			{
				diff = abs(dest - currPos_B);
				currPos_B = dest;
			}

			if (isDupTurn)
			{
				cnt += diff + 1;
				turn += diff + 1;
			}
			else
			{
				if ( diff <= turn )
				{
					cnt += 1;
					turn = 1;
				}
				else
				{
					cnt += diff - turn + 1;
					turn = diff - turn + 1;
				}
			}
		}
		
		// Print to output file
		fprintf(ofp, "Case #%d: %d\n", tc, cnt);
	}

	return 0;
}

