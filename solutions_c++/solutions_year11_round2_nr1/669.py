/*
 * =========================================================
 *       Filename:  A.cpp
 *    Description:  
 *        Created:  2011/5/22 0:06:13
 *         Author:  rocket323
 * =========================================================
 */
#include <stdio.h>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
#define maxl 150
using namespace std;

char s[maxl][maxl];
double wp[maxl], op[maxl], oop[maxl];
int n;

int main() {
	int t;
	scanf("%d", &t);
	for(int q=1; q<=t; ++q) {
		scanf("%d", &n);
		for(int i=0; i<n; ++i) scanf("%s", s[i]);
		for(int i=0; i<n; ++i) {
			int win = 0, tot = 0;
			for(int j=0; j<n; ++j) {
				if(s[i][j] == '1') win++;
				if(s[i][j] != '.') tot++;
			}
			wp[i] = win * 1.0 / tot;
		}

		for(int i=0; i<n; ++i) {
			double a = 0;
			int cnt = 0;
			for(int j=0; j<n; ++j) {
				if(s[i][j] != '.') {
					int b1 = 0, b2 = 0;
					for(int k=0; k<n; ++k) {
						if(k == i) continue;
						if(s[j][k] != '.') b2++;
						if(s[j][k] == '1') b1++;
					}
					double tmp = b1 * 1.0 / b2;
					a += tmp;
					cnt++;
				}
			}
			op[i] = a * 1.0 / cnt;
		}

		for(int i=0; i<n; ++i) {
			double a = 0;
			int cnt = 0;
			for(int j=0; j<n; ++j) {
				if(s[i][j] != '.') {
					cnt++;
					a += op[j];
				}
			}
			oop[i] = a * 1.0 / cnt;
		}

		printf("Case #%d:\n", q);
		for(int i=0; i<n; ++i) {
			double ans = 0.25 * wp[i] + 0.5 * op[i] + 0.25 * oop[i];
			printf("%.9lf\n", ans);
		}
	}
	return 0;
}

