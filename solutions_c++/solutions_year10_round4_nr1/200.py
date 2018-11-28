#define _CRT_SECURE_NO_DEPRECATE

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <string.h>

using namespace std;

#define pb push_back
#define pf push_front
#define mp make_pair
#define fi(a, b) for(i=a; i<=b; i++)
#define fj(a, b) for(j=a; j<=b; j++)
#define fo(a, b) for(o=a; o<=b; o++)
#define fdi(a, b) for(i=a; i>=b; i--)
#define fdj(a, b) for(j=a; j>=b; j--)
#define fdo(a, b) for(o=a; o>=b; o--)
#define ZERO(x) memset(x, 0, sizeof(x));
#define COPY(x, y) memcpy(x, y, sizeof(y));
#define SIZE(x) (int)x.size()
#define LEN(x) (int)x.length()

typedef long long int64;

#define MAX 501

int k;

int d[MAX][MAX];
int w[MAX];

int matr[MAX][MAX];
int color[MAX][MAX];
int C;

bool Try(int x0, int y0, int s) {
	int S = 2 * s - 1;
	int i, j;

	if (x0 == 3 && y0 == 6 && s == 6) {
		s = s;
	}

	int X;

	C++;
	X = x0;
	fj(1, k) {
		fi(1, j) {
			if (j + y0 - 1 > S) return false;
			if (j + X - 1 > w[j + y0 - 1]) return false;
			if (i + X - 1 <= 0) return false;
		
			color[j + y0 - 1][i + X - 1] = C;
			matr[j + y0 - 1][i + X - 1] = d[j][i];
			
		}
		if (j + y0 - 1 >= s) X--;
	}
	fj(k + 1, 2*k - 1) {
		X++;
		fi(1, 2*k - j) {
			if (j + y0 - 1 > S) return false;
			if (2*k - j + X - 1 > w[j + y0 - 1]) return false;
			if (i + X - 1 <= 0) return false;
			
			color[j + y0 - 1][i + X - 1] = C;			
			matr[j + y0 - 1][i + X - 1] = d[j][i];			
			
		}
		if (j + y0 - 1 >= s) X--;
	}
	fj(1, s) {
		fi(1, j) {
			if (color[j][i] == C && color[j][ w[j] - i + 1 ] == C && matr[j][i] != matr[j][ w[j] - i + 1 ]) return false;
			if (color[j][i] == C && color[ S - j + 1 ][i] == C && matr[j][i] != matr[ S - j + 1 ][i]) return false;
			if (color[j][i] == C && color[ S - j + 1 ][ w[j] - i + 1 ] == C && matr[j][i] != matr[ S - j + 1 ][ w[j] - i + 1 ]) return false;
/*
			if (color[j][i] != C && color[j][ w[j] - i + 1 ] == C ) {
				matr[j][i] = matr[j][ w[j] - i + 1 ];
				color[j][i] = C;
			}
			if (color[j][i] != C && color[ S - j + 1 ][i] == C) {
				matr[j][i] = matr[ S - j + 1 ][i];
				color[j][i] = C;
			}
			if (color[j][i] != C && color[ S - j + 1 ][ w[j] - i + 1 ] == C) {
				matr[j][i] = matr[ S - j + 1 ][ w[j] - i + 1 ];
				color[j][i] = C;
			}*/
		}
	}
	fj(s + 1, 2*s - 1) {
		fi(1, 2*s - j) {
			if (color[j][i] == C && color[j][ w[j] - i + 1 ] == C && matr[j][i] != matr[j][ w[j] - i + 1 ]) return false;
			if (color[j][i] == C && color[ S - j + 1 ][i] == C && matr[j][i] != matr[ S - j + 1 ][i]) return false;
			if (color[j][i] == C && color[ S - j + 1 ][ w[j] - i + 1 ] == C && matr[j][i] != matr[ S - j + 1 ][ w[j] - i + 1 ]) return false;
/*
			if (color[j][i] != C && color[j][ w[j] - i + 1 ] == C ) {
				matr[j][i] = matr[j][ w[j] - i + 1 ];
				color[j][i] = C;
			}
			if (color[j][i] != C && color[ S - j + 1 ][i] == C) {
				matr[j][i] = matr[ S - j + 1 ][i];
				color[j][i] = C;
			}
			if (color[j][i] != C && color[ S - j + 1 ][ w[j] - i + 1 ] == C) {
				matr[j][i] = matr[ S - j + 1 ][ w[j] - i + 1 ];
				color[j][i] = C;
			}*/
		}
	}
	return true;
}

int test, testq;

void Print(int o) {
	int i, j;
	printf("\n");
	fj(1, o) {
		fi(1, o - j) printf(" ");
		fi(1, j) {
			if (color[j][i] != C) {
				printf("# ");
			} else {
				printf("%d ", matr[j][i]);
			}
		}
		printf("\n");
	}
	fj(o + 1, 2*o - 1) {
		fi(1, j - o) printf(" ");
		fi(1, 2*o - j) {
			if (color[j][i] != C) {
				printf("# ");
			} else {
				printf("%d ", matr[j][i]);
			}
		}
		printf("\n");
	}
	printf("\n\n");
}

int main() {
	int i, j, o;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &testq);
	for (test = 1; test <= testq; test++) {
		printf("Case #%d: ", test);
		scanf("%d", &k);
		ZERO(d);
		ZERO(matr);
		ZERO(color);
		C = 0;
		fj(1, k) {
			fi(1, j) {
				scanf("%d" , &d[j][i]);
			}
		}
		fj(k + 1, 2*k - 1) {
			fi(1, 2*k - j) {
				scanf("%d" , &d[j][i]);
			}
		}
		o = k;
		while (1) {
			fj(1, o) {
				w[j] = j;
			}
			fj(o + 1, 2*o - 1) {
				w[j] = 2*o - j;
			}
			fj(1, o) {
				fi(1, j) {
					if (Try(i, j, o)) {
						//Print(o);
						goto l;
					}
				}
			}
			fj(o + 1, 2*o - 1) {
				fi(1, w[j]) {
					if (Try(i, j, o)) {						
						//Print(o);
						goto l;
					}
				}
			}
			o++;
		}
l:;
		//Print(o);
		printf("%d\n", o * o - k * k);
		fflush(stdout);
	}
	return 0;
}
