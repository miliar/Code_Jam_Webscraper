//============================================================================
// Name        : gcj@2011-QR-A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#include <cmath>
using namespace std;

int op[105];
int pos[105];
int tt[105];
int out[105];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t;
	int index = 1;
	scanf ("%d", &t);
	while (t --) {
		int n;
		scanf ("%d", &n);
		for (int i = 0; i < n; i ++) {
			char tmp[3];
			scanf ("%s%d", tmp, &pos[i]);
			if (tmp[0] == 'O') {
				op[i] = 0;
			} else {
				op[i] = 1;
			}
		}
		int cur[2];
		cur[0] = cur[1] = 1;
		for (int i = 0; i < n; i ++) {
			tt[i] = abs(pos[i] - cur[op[i]]) + 1;
			cur[op[i]] = pos[i];
		}
		cur[0] = cur[1] = 0;
		for (int i = 0; i < n; i ++) {
			int per = op[i];
			int t = cur[per] + tt[i];
			if (i != 0 && t <= out[i - 1]) {
				out[i] = out[i - 1] + 1;
			} else {
				out[i] = t;
			}
			cur[per] = out[i];
		}
//		for (int i = 0; i < n; i ++) {
//			cerr << out[i] << " ";
//		}
//		cerr << endl;
		printf ("Case #%d: %d\n", index ++, out[n - 1]);
	}
	return 0;
}
