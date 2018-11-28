// Using libUtil from libGlov (Game Library of Victory) available at http://bigscreensmallgames.com/libGlov
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
using namespace std;

char *doA(char **&toks)
{
	static char buf[128000];
	int L = atoi(*toks++);
	int D = atoi(*toks++);
	int N = atoi(*toks++);
	char **words = toks;
	toks += D;
	for (int testnum=0; testnum<N; testnum++)
	{
		char *test = *toks++;
		bool lookup[15][256] = {0};
		for (int i=0; i<L; i++)
		{
			if (*test=='(')
			{
				test++;
				while (*test!=')')
				{
					lookup[i][*test] = true;
					test++;
				}
			} else {
				lookup[i][*test] = true;
			}
			test++;
		}
		int c = 0;
		for (int i=0; i<D; i++)
		{
			bool b=true;
			for (int j=0; j<L; j++)
			{
				if (!lookup[j][words[i][j]])
					b=false;
			}
			if (b)
				c++;
		}
		strcatf_s(buf, ARRAY_SIZE(buf), "Case #%d: %d\n", testnum+1, c);
	}
	return buf;
}
