// Using libUtil from libGlov (Game Library of Victory) available at http://bigscreensmallgames.com/libGlov
// Some solutions may use BigInteger from http://mattmccutchen.net/bigint/
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
#include <algorithm>
using namespace std;
#pragma warning(disable:4018)
extern void doneParsingArgs(char **&toks);

char *doB(char **&toks)
{
	int C = atoi(*toks++);
	char **comb = toks;
	toks += C;
	int D = atoi(*toks++);
	char **dest = toks;
	toks += D;
	int N = atoi(*toks++);
	char *str = *toks++;
	doneParsingArgs(toks);

	char buf[16384];
	memset(buf, 0, sizeof(buf));
	int idx=0;
	while (*str)
	{
		buf[idx++] = *str;
		buf[idx] = 0;
		if (idx > 1)
		{
			// merge
			bool bMerged=false;
			for (int i=0; i<C; i++)
			{
				if (strncmp(&buf[idx-2], comb[i], 2)==0 ||
					buf[idx-2] == comb[i][1] && buf[idx-1] == comb[i][0])
				{
					buf[idx-2] = comb[i][2];
					idx--;
					buf[idx] = 0;
					bMerged = true;
					break;
				}
			}
			// clear
			if (!bMerged)
			{
				for (int i=0; i<D; i++)
				{
					if (strchr(buf, dest[i][0]) && strchr(buf, dest[i][1]))
					{
						idx = 0;
						buf[idx] = 0;
						break;
					}
				}
			}
		}
		str++;
	}

	static char rbuf[16384];
	int ridx=0;
	rbuf[ridx++] = '[';
	for (int i=0; i<idx; i++)
	{
		rbuf[ridx++] = buf[i];
		if (i != idx - 1)
		{
			rbuf[ridx++] = ',';
			rbuf[ridx++] = ' ';
		}
	}
	rbuf[ridx++] = ']';
	rbuf[ridx++] = 0;
	
	return rbuf;
}

