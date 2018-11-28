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

struct {
	U8 and; // 0 is OR
	U8 changeable;
	U8 V;
} tree[20000];

int cache[20000][2][2];
bool bcache[20000][2][2];

int M;
bool leaf(int i)
{
	return i>=(M-1)/2;
}

int findit(int N, int V);

int sub(int N, int V, U8 and)
{
	int r=-1;
	if (bcache[N][V][and])
		return cache[N][V][and];

	int r1 = findit(2*(N+1)-1, 1);
	int r2 = findit(2*(N+1), 1);
	int r3 = findit(2*(N+1)-1, 0);
	int r4 = findit(2*(N+1), 0);
#define TEST(v1, v2)\
		if (v1!=-1 && v2!=-1)\
			if (r==-1 || r> v1+v2)\
				r = v1+v2;
	if (and) {
		if (V) {
			TEST(r1, r2);
		} else {
			TEST(r3, r2);
			TEST(r3, r4);
			TEST(r1, r4);
		}
	} else {
		if (V) {
			TEST(r1, r2);
			TEST(r1, r4);
			TEST(r2, r3);
		} else {
			TEST(r3, r4);
		}
	}

	bcache[N][V][and] = true;
	cache[N][V][and] = r;
	return r;
}

int findit(int N, int V)
{
	assert(N<M);
	if (leaf(N)) {
		assert(tree[N].V != -1);
		if (tree[N].V == V)
			return 0;
		else
			return -1;
	}
	int r = sub(N, V, tree[N].and);
	if ((r == -1 || r>1) && tree[N].changeable)
	{
		int r2 = sub(N, V, !tree[N].and);
		if (r2!=-1) {
			r2++;
			if (r==-1 || r2 < r)
				r = r2;
		}
	}
	return r;
}

char *doA(char **&toks)
{
	memset(bcache, 0, sizeof(bcache));
	M = atoi(*toks++);
	int V = atoi(*toks++);
	for (int i=0; i<(M-1)/2; i++) {
		tree[i].and = atoi(*toks++);
		tree[i].changeable = atoi(*toks++);
		tree[i].V = -1;
	}
	for (int i=0; i<(M+1)/2; i++) {
		tree[(M-1)/2 + i].V = atoi(*toks++);
	}

	static char buf[1024];
	int n = findit(0, V);
	if (n==-1)
		return "IMPOSSIBLE";
	sprintf(buf, "%d", n);
	return buf;
}

void gentestcaseA(void)
{
	FILE *f = fopen("A-large-test.in", "w");
	fprintf(f, "1\n10000 1\n");
	for (int i=0; i<(10000-1)/2; i++) {
		fprintf(f, "%d 1\n", randInt(2));
	}
	for (int i=0; i<(10000+1)/2; i++) {
		fprintf(f, "%d\n", randInt(2));
	}
	fclose(f);
}
