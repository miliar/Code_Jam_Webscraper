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

char *doC(char **&toks)
{
	int A = atoi(*toks++);
	int B = atoi(*toks++);
	doneParsingArgs(toks);
	int r = 0;
	int L;
	char temp[15];
	sprintf(temp, "%d", A);
	L = strlen(temp);
	char bufA[15];
	char bufB[8];
	for (int i=A; i<B; i++) {
		itoa(i, bufA, 10);
		itoa(i, bufA+L, 10);
		for (int j=i+1; j<=B; j++) {
			itoa(j, bufB, 10);
			if (strstr(bufA, bufB)) {
				r++;
			}
		}
	}

	static char buf[16384];
	sprintf(buf, "%d", r);
	return buf;
}

