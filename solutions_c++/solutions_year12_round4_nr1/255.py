#define _CRT_SECURE_NO_DEPRECATE

#pragma comment(linker, "/STACK:32000000")

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

#define INF 1000010000
#define MAX 10500

int n;
int d[MAX], l[MAX];
int D;


void Read() {
	int i;
	scanf("%d", &n);
	fi(1, n) {
		scanf("%d %d", &d[i], &l[i]);
	}
	n++;
	scanf("%d", &D);
	d[n] = D;
	l[n] = 1000011000;
}

int color[MAX];

int dst[MAX];

void Dijkstra() {
	int i;
	int x;
	set <pair<int, int>> t;
	fi(1, n) {
		dst[i] = 0;
	}
	ZERO(color);
	dst[1] = d[1];
	t.insert(mp(-dst[1], 1));
	while (!t.empty()) {
		x = t.begin()->second;
		t.erase(t.begin());
		if (color[x]) continue;
		color[x] = 1;
		fi(1, n) {
			if (i == x) continue;
			if (abs(d[i] - d[x]) <= dst[x]) {
				if (dst[i] < min(l[i], abs(d[i] - d[x])) ) {
					dst[i] = min(l[i], abs(d[i] - d[x]));
					t.insert(mp(-dst[i], i));
				}
			}
		}
	}
	if (color[n]) {
		printf("YES\n");
	} else {
		printf("NO\n");
	}
}

void Solve() {
	Dijkstra();

}

int main(int argc, char **argv) {
	if (argc == 1) {
		freopen("input.txt","r",stdin);
	} else {
		freopen(argv[1], "r",stdin);
	}
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