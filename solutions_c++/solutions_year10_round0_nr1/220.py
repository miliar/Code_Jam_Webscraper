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
	int K = atoi(*toks++);

	static char buf[16384];
	sprintf(buf, "%s", ((K & ((1 << N) - 1))==((1<<N)-1))?"ON":"OFF");
	return buf;
}
