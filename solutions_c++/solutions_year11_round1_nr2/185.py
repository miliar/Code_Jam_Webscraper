#define _CRT_SECURE_NO_DEPRECATE

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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

using namespace std;

#define pb push_back
#define pf push_front
#define mp make_pair
#define fi(a, b) for(i=a; i<=b; i++)
#define fj(a, b) for(j=a; j<=b; j++)
#define fo(a, b) for(o=a; o<=b; o++)
#define fu(a, b) for(u=a; u<=b; u++)
#define fdi(a, b) for(i=a; i>=b; i--)
#define fdj(a, b) for(j=a; j>=b; j--)
#define fdo(a, b) for(o=a; o>=b; o--)
#define ZERO(x) memset(x, 0, sizeof(x))
#define COPY(x,y) memcpy(x, y, sizeof(y))
#define LEN(x) (int)x.length()
#define SIZE(x) (int)x.size()

typedef unsigned long long int64;

int testq;
int test;

#define MAX 10100

int n, m;

char dic[MAX][20];
int len[MAX];

int Q[MAX];

char lst[MAX][30];

int f[MAX][30];

void Read() {
	int i, j;
	scanf("%d %d", &n, &m);

	ZERO(f);
	ZERO(dic);
	ZERO(len);
	ZERO(lst);
	ZERO(Q);

	fi(1, n) {
		scanf("%s", dic[i]);
		len[i] = (int)strlen(dic[i]);
	}
	fi(1, n) {
		fj(0, len[i] - 1) {
			f[i][dic[i][j] - 'a'] = 1;
		}
	}

	fi(1, n) {
		fj(0, 25) {
			if (f[i][j]) Q[i]++;
		}
	}
	fi(1, m) {
		scanf("%s", lst[i]);
	}
}

int64 hash[MAX];
map <int64, int> color;
int d[MAX];

int C;

int ans;
int ansp;
char anss[15];

int q[MAX];

void Solve() {
	int i, j, o, u;

	int64 p[15];

	p[0] = 1;

	fi(1, 11) {
		p[i] = p[i - 1] * 29;
	}

	fi(1, m) {
		ZERO(d);
		ZERO(q);
		ans = -1;
		ansp = -1;
		ZERO(anss);
		color.clear();
		fo(1, n) {
			hash[o] = p[11] * len[o];
		}
		color.clear();
		fj(0, 25) {			
			C++;
			fo(1, n) {
				if (f[o][lst[i][j] - 'a']) {
					color[ hash[o] ] = C;
				}
			}

			fo(1, n) {
				if (color.find(hash[o]) != color.end() && color[ hash[o] ] == C) {

					if (f[o][lst[i][j] - 'a']) {

						q[o]++;

						fu(0, len[o] - 1) {
							if (dic[o][u] == lst[i][j]) {
								hash[o] += p[u] * lst[i][j];
							}
						}
						if (q[o] == Q[o]) {
							if (d[o] > ans || d[o] == ans && o < ansp) {
								ansp = o;
								ans = d[o];
								strcpy(anss, dic[o]);
							}
						}
					} else {
						d[o]++;
					}
				}
			}
		}
		printf("%s", anss);
		if (i != m) printf(" ");
		fflush(stdout);
	}
	printf("\n");
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &testq);
	for (test = 1; test <= testq; test++) {
		Read();
		printf("Case #%d: ", test);
		Solve();
		fflush(stdout);
	}
	return 0;
}