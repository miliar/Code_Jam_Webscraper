//============================================================================
// Name        : gcj@2011-1B-B.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#include <string.h>
#define M 1000005
#define EXP 1e-8
using namespace std;
typedef long long LL;

int D;
int n;
double value[M];
double next[M];

bool judge(double time) {
	next[0] = value[0] - time;
	for (int i = 1; i < n; i ++) {
		double pos = value[i] - time;
		if (pos - next[i - 1] >= D) {
			next[i] = pos;
		} else {
			pos = next[i - 1] + D;
			if (pos <= value[i] + time) {
				next[i] = pos;
			} else {
				return false;
			}
		}
	}
	return true;
}

int main() {
//	freopen("test.in", "r", stdin);
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	int index = 1;
	scanf ("%d", &T);
	while (T --) {
		int C;
		scanf ("%d%d", &C, &D);
		n = 0;
		for (int i = 0; i < C; i ++) {
			int P, V;
			scanf ("%d%d", &P, &V);
			while (V --) {
				value[n ++] = P;
			}
		}
		double left = 0;
		double right = 1.0 * n * D;
		while (right - left > EXP) {
			double mid = (left + right) / 2.0;
			bool can = judge(mid);
			if (can) {
				right = mid;
			} else {
				left = mid;
			}
		}
		printf ("Case #%d: %.6f\n", index ++, left);
	}
	return 0;
}
