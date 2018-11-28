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
	int N = atoi(*toks++);
	int S = atoi(*toks++);
	int p = atoi(*toks++);
	int p1 = MAX(0, p-1);
	int p2 = MAX(0, p-2);
	int scores[101];
	for (int i=0; i<N; i++) {
		scores[i] = atoi(*toks++);
	}
	doneParsingArgs(toks);

	int r = 0;
	int pn = p + p1 + p1;
	int ps = p + p2 + p2;
	for (int i=0; i<N; i++) {
		int v = scores[i];
		if (v >= pn) {
			// not surprising
			r++;
		} else if (S > 0 && v >= ps) {
			S--;
			r++;
		}
	}

	static char buf[16384];
	sprintf(buf, "%d", r);
	return buf;
}

