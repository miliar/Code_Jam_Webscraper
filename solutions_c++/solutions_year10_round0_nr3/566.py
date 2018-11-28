// Theme Park.cpp : Defines the entry po__int64 for the console application.
//

#include "stdafx.h"
#include "string.h"
#include <iostream>

using namespace std;

int main()
{
	FILE* infile = fopen("C-large.in", "r");
	freopen("large.txt", "w", stdout);
	
	int t;
	fscanf(infile, "%d", &t);
	for (__int64 kase = 0; kase < t; kase++)
	{
		int r, k, n;
		fscanf(infile, "%d %d %d", &r, &k, &n);
		int size[1100];
		for (__int64 i = 0; i < n; i++)
			fscanf(infile, "%d", &size[i]);

		__int64 used[1100];
		for (__int64 i = 0; i < 1100; i++)
			used[i] = -1;
		__int64 earn[1100];
		__int64 startPos = 0;
		__int64 repTime, repEuro, leftEuro, beforeRep;
		for (__int64 i = 0; i < n + 1; i++)
		{
			if (used[startPos] == -1)
				used[startPos] = i;
			else
			{
				repTime = (r - used[startPos]) / (i - used[startPos]);
				beforeRep = 0;
				if (used[startPos] - 1 >= 0) beforeRep = earn[used[startPos] - 1];
				repEuro = earn[i - 1] - beforeRep;
				__int64 leftSize = (r - used[startPos]) % (i - used[startPos]);
				leftEuro = 0;
				if (leftSize > 0) leftEuro = earn[used[startPos] + leftSize - 1] - beforeRep;
				break;
			}
			__int64 hold = 0;
			__int64 endPos = startPos;
			while (1)
			{
				hold += size[endPos];
				if (hold > k)
					break;
				endPos = (endPos + 1) % n;
				if (endPos == startPos) break;
			}
			if (hold > k) earn[i] = hold - size[endPos];
			else earn[i] = hold;
			if (i != 0) earn[i] += earn[i - 1];
			startPos = endPos;
		}
		__int64 output= repEuro * repTime + beforeRep + leftEuro;
		cout << "Case #" << kase + 1 << ": " << output << endl;
	}
	fclose(infile);

	return 0;
}