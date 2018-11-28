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
#define fdi(a, b) for(i=a; i>=b; i--)
#define fdj(a, b) for(j=a; j>=b; j--)
#define fdo(a, b) for(o=a; o>=b; o--)
#define ZERO(x) memset(x, 0, sizeof(x))
#define COPY(x,y) memcpy(x, y, sizeof(y))
#define LEN(x) (int)x.length()
#define SIZE(x) (int)x.size()

typedef long long int64;

int testq;
int test;

int c, d;
int n;

char str[1000];

string C[1000], D[1000];

void Read() {
	int i;
	char s[100];
	scanf("%d", &c);
	fi(1, c) {
		scanf("%s", s);
		C[i] = s;
	}
	scanf("%d", &d);
	fi(1, d) {
		scanf("%s", s);
		D[i] = s;
	}
	scanf("%d", &n);
	scanf("%s", str);
}

char ans[1000];
int q;
int color[1000];

int f[255][255];

void Solve() {
	int i, j;
	ZERO(ans);
	ZERO(color);
	map <pair <char, char>, char > comb;
	fi(1, c) {
		comb[mp(C[i][0], C[i][1])] = C[i][2];
		comb[mp(C[i][1], C[i][0])] = C[i][2];
	}
	ZERO(f);
	fi(1, d) {
		f[D[i][1]][D[i][0]] = 1;
		f[D[i][0]][D[i][1]] = 1;
	}
	q = 0;
	fi(0, n - 1) {
		q++;
		ans[q] = str[i];

		while (q >= 2 && comb.find(mp(ans[q - 1], ans[q])) != comb.end()) {
			ans[q - 1] = comb[mp(ans[q - 1], ans[q])];
			q--;
		}

		ZERO(color);
		fj(1, q - 1) {
			color[ans[j]] = 1;
		}
		fj('A', 'Z') {
			if (color[j] && f[j][ans[q]]) {
				q = 0;
				break;
			}
		}
	}

	printf("[");
	fi(1, q) {
		printf("%c", ans[i]);
		if (i != q) {
			printf(", ");
		}
	}
	printf("]\n");
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