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
#include "utilHashTable2.h"
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;
#pragma warning(disable:4018)


char *doB(char **&toks)
{
	int P = atoi(*toks++);
	int req[1024];
	int tp[11][512];
	for (int i=0; i<(1<<P); i++)
	{
		req[i] = atoi(*toks++);
	}
	int p2 = 1<<(P-1);
	int tpi=0;
	while (p2)
	{
		for (int i=0; i<p2; i++)
		{
			tp[tpi][i] = atoi(*toks++);
		}
		p2>>=1;
		tpi++;
	}

	int r=0;
	p2 = 1<<(P-1);
	int m=2;
	for (int i=0; i<tpi; i++)
	{
		for (int j=0; j<p2; j++)
		{
			bool b=false;
			for (int k=j*m; k<(j+1)*m; k++)
			{
				if (req[k]<=i)
					b=true;
			}
			if (b)
				r+=tp[i][j];
		}
		p2>>=1;
		m<<=1;
	}


	static char buf[16384];
	sprintf(buf, "%d", r);
	return buf;
}
