#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <string>
#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define	COUNT(a)	(sizeof(a) / sizeof((a)[0]))
#define	MAXN	128

int main(int argc, char *argv[])
{
	int nc, ci;
	int m[MAXN][MAXN];
	double wp[MAXN], owp[MAXN], oowp[MAXN];
	
	scanf("%d", &nc);
	for (ci = 1; ci <= nc; ci++) {
		int i, j, k, n;
		char s[MAXN];
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			wp[i] = owp[i] = oowp[i] = 0;
			for (j = 0; j < n; j++) m[i][j] = 0;
		}
		for (i = 0; i < n; i++) {
			scanf("%s", s);
			for (j = 0; j < n; j++)
				if (s[j] == '1') m[i][j] = 1;
				else if (s[j] == '0') m[i][j] = -1;
		}
		
		for (i = 0; i < n; i++) {
			double win = 0, loss = 0;
			for (j = 0; j < n; j++) {
				if (m[i][j] > 0) win += 1;
				else if (m[i][j] < 0) loss += 1;
			}
			wp[i] = win / (win + loss);
		}
		
		for (i = 0; i < n; i++) {
			double wps = 0;
			int count = 0;
			for (j = 0; j < n; j++) {
				if (i == j || m[i][j] == 0) continue;
				double win = 0, loss = 0;
				for (k = 0; k < n; k++) {
					if (k == i) continue;
					if (m[j][k] > 0) win += 1;
					else if (m[j][k] < 0) loss += 1;
				}
				if (win + loss > 0) {
					count++;
					wps += win / (win + loss);
				}
			}
			if (count > 0)
				owp[i] = wps / count;
		}
		
		for (i = 0; i < n; i++) {
			oowp[i] = 0;
			int count = 0;
			for (j = 0; j < n; j++)
				if (m[i][j] != 0) {
					oowp[i] += owp[j];
					count++;
				}
			if (count > 0)
				oowp[i] /= count;
		}
		
		printf("Case #%d:\n", ci);

		for (i = 0; i < n; i++)
			printf("%.12f\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
	}
	
	return 0;
}
