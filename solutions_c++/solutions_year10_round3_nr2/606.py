// gcj2010.cpp : Defines the entry point for the console application.
//

#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

double mypow(double x, int k) {
	if (k == 0)
		return 1;

	if (k == 1)
		return x;

	double y = pow(x, k >> 1);

	if (k & 0x01 == 1) {
		return y * y * x;
	}
	else {
		return y * y;
	}
}

int u(int l, int p, int c) {
	if (l * c >= p)
		return 0;

	int m = 1000000000;

	/*
	double x = pow(l, 1.0 / c);
	double y = pow(p, 1.0 / c);

	for (int i = 1; i <= c - 1; i++) {
		int t = (int) ceil(mypow(x, i) * mypow(y, c - i));
		int mx1 = 0, mx2 = 0, mx3 = 0, mx4 = 0;
		if (l < t && t < p) {
			mx1 = u(l, t, c);
			mx2 = u(t, p, c);
		}

		if (l < t - 1 && t - 1 < p) {
			mx3 = u(l, t - 1, c);
			mx4 = u(t - 1, p, c);
		}

		int x = 1  + min(max(mx1, mx2), max(mx3, mx4));
		if (x < m)
			m = x;
	}
	*/


	int x = l * c;
	int y = (int)ceil((double)p/c);

//	int m = 1000000000;
	while (x < p) {
		m = min(m, max(u(l, x, c), u(x, p, c)));
		x = x * c;
	}

	while (y > l) {
		m = min(m, max(u(l, y, c), u(y, p, c)));
		y = (int)ceil((double)y/c);
	}

	return m + 1;
}

int main(int argc, char* argv[])
{
	// Read input
	FILE* f = fopen("B-small-attempt4.in", "r");
	FILE* fOut = fopen("output.txt", "w");

	unsigned int nCases;
	int l, p, c;
	fscanf(f, "%i", &nCases);
	for (unsigned int iCase = 0; iCase < nCases; iCase++) {
		printf("Processing case #%i\n", iCase + 1);
		fscanf(f, "%i %i %i", &l, &p, &c);

		fprintf(fOut, "Case #%i: %i\n", iCase + 1, u(l, p, c));
		fflush(fOut);
	}

	fclose(f);
	fclose(fOut);

	return 0;
}

