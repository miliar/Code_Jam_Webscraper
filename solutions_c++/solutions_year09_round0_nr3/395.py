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

char *TEST="welcome to code jam";
int TEST_LEN=strlen(TEST);

int len;
char *str;
int cache[501][20];
bool bcache[501][20];

int doit(int stri, int testi)
{
	int r;
	if (testi >= TEST_LEN)
		return 1;
	if (stri >= len)
		return 0;
	if (bcache[stri][testi])
		return cache[stri][testi];
	if (TEST[testi] == str[stri])
	{
		r = (doit(stri+1, testi+1) + doit(stri+1, testi)) % 10000;
	} else {
		r = doit(stri+1, testi);
	}
	bcache[stri][testi] = true;
	cache[stri][testi] = r;
	return r;
}

char *doC(char **&toks)
{
	static char buf[32768];
	str = *toks++;
	memset(cache, 0, sizeof(cache));
	memset(bcache, 0, sizeof(bcache));
	len = strlen(str);
	int r = doit(0, 0) % 10000;

	sprintf(buf, "%04d", r);
	return buf;
}

