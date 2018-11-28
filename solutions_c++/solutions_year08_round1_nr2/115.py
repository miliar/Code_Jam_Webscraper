#define _CRT_SECURE_NO_WARNINGS

#ifdef SPOJ
#define SCANF(s1,s2) scanf(s1, s2)
#define SCANF2(s1,s2,s3) scanf(s1, s2, s3)
#define SCANF3(s1,s2,s3,s4) scanf(s1, s2, s3, s4)
#define SCANF4(s1,s2,s3,s4,s5) scanf(s1, s2, s3, s4, s5)
#define GETS(s1) gets(s1)
#else
#define SCANF(s1,s2) fscanf(in, s1, s2)
#define SCANF2(s1,s2,s3) fscanf(in, s1, s2, s3)
#define SCANF3(s1,s2,s3,s4) fscanf(in, s1, s2, s3, s4)
#define SCANF4(s1,s2,s3,s4,s5) fscanf(in, s1, s2, s3, s4, s5)
#define GETS(s1) fgets(s1, 1000000, in)
#endif
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<list>
#include<deque>
#include<vector>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#include<string>
//#include<iterator>

struct pp {
	int val, notVal;
	int bitCount;

	pp () {
	}

	void set (int v) {
		val = v;
		notVal = ~v;
		bitCount = 0;
		while (v > 0) {
			if (v & 1)
				bitCount++;
			v >>= 1;
		}
	}

	bool operator < (pp p) const {
		return (bitCount < p.bitCount);
	}
};

pp tests [1024];
int malted [200], notMalted [200];

using namespace std;
int main (void) {

#ifndef SPOJ
	FILE *in, *out;
	in = fopen ("test.in", "r");
	out = fopen ("test.out", "w");
#endif
	int cases, c, n, i, m, j, t, flavor, malt, k;
	for (i = 0; i < 1024; i++)
		tests [i].set (i);
	sort (tests, tests + 1024);
	SCANF ("%d", &cases);
	for (c = 0; c < cases; c++) {
		SCANF2 ("%d %d", &n, &m);
		for (i = 0; i < m; i++) {
			malted [i] = notMalted [i] = 0;
			SCANF ("%d", &t);
			for (j = 0; j < t; j++) {
				SCANF2 ("%d %d", &flavor, &malt);
				flavor--;
				if (malt == 1)
					malted [i] |= 1 << flavor;
				else
					notMalted [i] |= 1 << flavor;
			}
		}
		for (i = 0; i < 1024; i++) {
			for (j = 0; j < m; j++) {
				if (!(malted [j] & tests [i].val) && !(notMalted [j] & tests [i].notVal))
					break;
			}
			if (j == m)
				break;
		}
		if (i == 1024)
			fprintf (out, "Case #%d: IMPOSSIBLE\n", c + 1);
		else {
			k = tests [i].val;
			fprintf (out, "Case #%d:", c + 1);
			for (i = 0; i < n; i++) {
				fprintf (out, " %d", k & 1);
				k >>= 1;
			}
			fprintf (out, "\n");
		}
	}
}