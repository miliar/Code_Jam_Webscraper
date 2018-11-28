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

int inputs [200];
int sortedInputs [200], sortedOutputs [200];


using namespace std;
int main (void) {

#ifndef SPOJ
	FILE *in, *out;
	in = fopen ("test.in", "r");
	out = fopen ("test.out", "w");
#endif
	int t, c, n, a, b, r, i;
	SCANF ("%d", &t);
	for (c = 0; c < t; c++) {
		SCANF ("%d", &inputs [c]);
		sortedInputs [c] = inputs [c];
	}
	sort (sortedInputs, sortedInputs + t);
	n = 2;
	a = 1;
	b = 5;
	r = 27;
	for (c = 0; c < t; c++) {
		while (n < sortedInputs [c]) {
			n++;
			a = b;
			b = r;
			r = (b * 6 - a * 4 + 10001) % 1000;
		}
		sortedOutputs [c] = r;
	}
	for (c = 0; c < t; c++) {
		i = 0;
		while (inputs [c] != sortedInputs [i])
			i++;
		fprintf (out, "Case #%d: %03d\n", c + 1, sortedOutputs [i]);
	}
}