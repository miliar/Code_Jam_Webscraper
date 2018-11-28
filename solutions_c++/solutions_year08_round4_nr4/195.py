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
#include <algorithm>
using namespace std;

int k;
int score(char *s, int slen, vector<int> v)
{
	int r=0;
	char last=-1;
	int p=0;
	for (int i=0; i<slen; i+=k) {
		for (int j=0; j<k; j++) {
			char c = s[i + v[j]];
			if (c != last) {
				r++;
				last = c;
			}
		}
	}
	return r;
}

char *doD(char **&toks)
{
	k = atoi(*toks++);
	char *s = *toks++;
	int slen = strlen(s);
	vector<int> v;
	for (int i=0; i<k; i++) {
		v.push_back(i);
	}
	int best=-1;
	do {
		int sc = score(s, slen, v);
		if (best==-1 || sc < best)
			best = sc;
	} while (next_permutation(v.begin(), v.end()));
	static char buf[1024];
	sprintf(buf, "%d", best);
	return buf;
}
