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

int v1 [1000], v2 [1000];

using namespace std;
int main (void) {

#ifndef SPOJ
	FILE *in, *out;
	in = fopen ("test.in", "r");
	out = fopen ("test.out", "w");
#endif
	int t, c, n, i;
	long long s;
	SCANF ("%d", &t);
	for (c = 1; c <= t; c++) {
		s = 0;
		SCANF ("%d", &n);
		for (i = 0; i < n; i++)
			SCANF ("%d", &v1 [i]);
		for (i = 0; i < n; i++)
			SCANF ("%d", &v2 [i]);
		sort (v1, v1 + n);
		sort (v2, v2 + n);
		for (i = 0; i < n; i++)
			s += v1 [i] * v2 [n - i - 1];
		fprintf (out, "Case #%d: %lld\n", c, s);
	}
}