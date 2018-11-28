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
	int N = atoi(*toks++);
	int len[41];
	memset(len, 0, sizeof(len));
	for (int i=0; i<N; i++)
	{
		char *s = *toks++;
		len[i] = 0;
		for (int j=0; j<N; j++, s++)
		{
			if (*s=='1')
				len[i] = j;
		}
	}
	int ret=0;
	for (int i=0; i<N; i++)
	{
		int j;
		for (j=i; len[j]>i; j++)
		{
			assert(j!=N-1);
		}
		int s=j;
		ret+=s-i;
		for (int j=s-1; j>=i; j--)
		{
			int t = len[j];
			len[j] = len[j+1];
			len[j+1] = t;
		}
	}
	static char buf[16384];
	sprintf(buf, "%d", ret);

	return buf;
}
