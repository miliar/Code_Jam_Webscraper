// Using libUtil from libGlov (Game Library of Victory) available at http://bigscreensmallgames.com/libGlov
// Some solutions using BigInteger from http://mattmccutchen.net/bigint/
#include "bigint/BigIntegerAlgorithms.hh"
#include "bigint/BigIntegerUtils.hh"
#include "utilUtils.h"
#include "utilFile.h"
#include "utilString.h"
#include "assert.h"
#include "utilArray.h"
#include <string.h>
#include <stdio.h>
#include <stdarg.h>
#include <conio.h>
#include "utilRand.h"
#include <vector>
#include <set>
#include <map>
using namespace std;

map<pair<int, int>, bool> cache[2];

bool wins(int a, int b, int turn)
{
	if (a <= 0 || b <= 0)
		return turn == 0;
	pair<int,int> key(a, b);
	if (cache[turn].find(key) != cache[turn].end())
	{
		return cache[turn][key];
	}
	for (int i=1; a*i < b; i++)
	{
		int b2 = b - a*i;
		if (wins(a, b2, !turn))
		{
			if (turn == 0)
			{
				cache[turn][key] = true;
				return true;
			}
		} else {
			if (turn == 1)
			{
				cache[turn][key] = false;
				return false;
			}
		}
	}
	for (int i=1; b*i < a; i++)
	{
		int a2 = a - b*i;
		if (wins(a2, b, !turn))
		{
			if (turn == 0)
			{
				cache[turn][key] = true;
				return true;
			}
		} else {
			if (turn == 1)
			{
				cache[turn][key] = false;
				return false;
			}
		}
	}
	if (turn==0)
	{
		cache[turn][key] = false;
		return false;
	}
	cache[turn][key] = true;
	return true;
}

char *doC(char **&toks)
{
	int A1 = atoi(*toks++);
	int A2 = atoi(*toks++);
	int B1 = atoi(*toks++);
	int B2 = atoi(*toks++);

	BigUnsigned ret=0;

	if (0)
	{
// 		for (int i=A1; i<=A2; i++)
// 		{
// 			for (int j=B1; j<=B2; j++)
// 			{
// 				if (wins(i, j, 0)) {
// 					printf("X");
// 					ret++;
// 				} else
// 					printf(".");
// 			}
// 			printf("\n");
// 		}
	} else {
		double golden_ratio = (1 + sqrt((double)5.0))/2.0;
		double inv = 1 / golden_ratio;
		for (int  i=A1; i<=A2; i++)
		{
			int p1 = i * inv; // last good
			int p2 = (i * golden_ratio) + 1;
			int dr=0;
			if (B1 <= p1)
			{
				if (B2 <= p1)
					dr = B2 - B1 + 1;
				else
					dr = p1 - B1 + 1;
			}
			if (B2 >= p2)
			{
				if (B1 >= p2)
					dr += B2 - B1 + 1;
				else
					dr += B2 - p2 + 1;
			}
			ret += dr;
		}
	}

	static char buf[16384];
	sprintf(buf, "%s", bigUnsignedToString(ret).c_str());
	return buf;
}
