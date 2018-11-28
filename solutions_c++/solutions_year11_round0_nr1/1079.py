#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>

#define INF 100000000

using namespace std;

FILE *in = fopen("B-large.in", "r"), *out = fopen("results.txt", "w");

int a, b, c, d, e, blen;
char c1[40][5], c2[40][5];
char s[400], build[400];

bool test(char a, char b, char c, char d) {
    return ((a == c && b == d) || (a == d && b == c));
}

int main() {
    fscanf(in, "%d", &a);
    
    for (int i=0; i<a; i++) {
	blen = 0;
	
	fscanf(in, "%d", &b);
	for (int j=0; j<b; j++) fscanf(in, "%s", &c1[j]);
	
	fscanf(in, "%d", &c);
	for (int j=0; j<c; j++) fscanf(in, "%s", &c2[j]);
	fscanf(in, "%d", &d);
	
	fscanf(in, "%s", &s);
	
	for (int j=0; j<d; j++) {
	    build[blen++] = s[j];
	    if (blen >= 2) {
		for (int k=0; k<b; k++) {
		    if (test(build[blen-1], build[blen-2], c1[k][0], c1[k][1])) --blen, build[blen-1] = c1[k][2];
		}
		for (int k=0; k<c; k++) {
		    for (int l=0; l<blen-1; l++) {
			if (test(build[blen-1], build[l], c2[k][0], c2[k][1])) blen = 0;
		    }
		}
	    }
	}
	printf("Case #%d: [", i+1);
	for (int j=0; j<blen; j++) {
	    printf("%c%s", build[j], (j < blen-1 ? ", " : "]\n"));
	}
	if (blen == 0) printf("]\n");
    }
    return 0;
}