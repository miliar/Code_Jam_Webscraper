#pragma comment(linker, "/STACK:128777216")

#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <iostream>
#include <functional>
#include <numeric>
#include <sstream>
#include <exception>
#include <cassert>

typedef long long i64;
typedef unsigned int u32;
const int null = 0;

using namespace std;

template<class T> int size(const T &a) {
	return int(a.size());
}
template<class T> T abs(const T &a) {
	return (a < 0? -a: a);
}
template<class T> T sqr(const T &a) {
	return a * a;
}

char a[4][5];

int main() {
#ifdef pperm
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int iTest = 1; iTest <= T; iTest++) {
		printf("Case #%d: ", iTest);
		for (int i = 0; i < 4; i++) {
			scanf("%s", a[i]);
		}
		int xwin = 0, owin = 0;
		for (int i = 0; i < 4; i++) {
			int co = 0, cx = 0, ct = 0;
			for (int j = 0; j < 4; j++) {
				switch (a[i][j]) {
				case 'X':
					cx++;
					break;
				case 'O':
					co++;
					break;
				case 'T':
					ct++;
				default:
					break;
				}
			}
			if (co + ct == 4) {
				owin = 1;
			}
			if (cx + ct == 4) {
				xwin = 1;
			}
			cx = co = ct = 0;
			for (int j = 0; j < 4; j++) {
				switch (a[j][i]) {
				case 'X':
					cx++;
					break;
				case 'O':
					co++;
					break;
				case 'T':
					ct++;
				default:
					break;
				}
			}
			if (co + ct == 4) {
				owin = 1;
			}
			if (cx + ct == 4) {
				xwin = 1;
			}
		}
		{
			int co = 0, cx = 0, ct = 0;
			for (int i = 0; i < 4; i++) {
				switch (a[i][i]) {
				case 'X':
					cx++;
					break;
				case 'O':
					co++;
					break;
				case 'T':
					ct++;
					break;
				default:
					break;
				}
				if (co + ct == 4) {
					owin = 1;
				}
				if (cx + ct == 4) {
					xwin = 1;
				}
			}
		}
		{
			int co = 0, cx = 0, ct = 0;
			for (int i = 0; i < 4; i++) {
				switch (a[i][3 - i]) {
				case 'X':
					cx++;
					break;
				case 'O':
					co++;
					break;
				case 'T':
					ct++;
					break;
				default:
					break;
				}
				if (co + ct == 4) {
					owin = 1;
				}
				if (cx + ct == 4) {
					xwin = 1;
				}
			}
		}
		int dot = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (a[i][j] == '.') {
					dot = 1;
				}
			}
		}
		if (xwin) {
			printf("X won");
		} else if (owin) {
			printf("O won");
		} else {
			if (dot) {
				printf("Game has not completed");
			} else {
				printf("Draw");
			}
		}
		printf("\n");
	}
#ifdef pperm
	fprintf(stderr, "\n%.3lf\n", clock() / double(CLOCKS_PER_SEC));
#endif
	return 0;
}