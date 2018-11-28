// Using libUtil from libGlov (Graphics Library of Victory) available at http://bigscreensmallgames.com/libGlov
#include "utils.h"
#include "file.h"
#include "strutil.h"
#include "assert.h"
#include "array.h"
#include <string.h>
#include <stdio.h>
#include <stdarg.h>
#include <conio.h>
#include "rand.h"
#include <vector>
using namespace std;

char *doB(char **&toks)
{
	int N = atoi(*toks++);
	int M = atoi(*toks++);
	int A = atoi(*toks++);
	for (int x0=0; x0<=N; x0++) {
		for (int y0=0; y0<=M; y0++) {
	for (int x1=0; x1<=N; x1++) {
		for (int x2=0; x2<=N; x2++) {
			for (int y1=0; y1<=M; y1++) {
				for (int y2=0; y2<=M; y2++) {
					//int a = x1 *y2 - x2*y2;
					int a = abs((x1*y0-x0*y1)+(x2*y1-x1*y2)+(x0*y2-x2*y0));
					if (a == A) {
						static char buf[1024];
						sprintf(buf, "%d %d %d %d %d %d", x0, y0, x1, y1, x2, y2);
						return buf;
					}
				}
			}
		}
	}
	break;
		}
	break;
	}

	return "IMPOSSIBLE";
}