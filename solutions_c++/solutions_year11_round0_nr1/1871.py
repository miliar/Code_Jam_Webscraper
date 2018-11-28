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

#define MAX 1000

int testq;
int test;

int n;

pair <char, int> p[MAX];

vector <int> O;
vector <int> B;

int Oc, Bc;

int Ox, Bx;

int ans;

void Solve() {
	int i;
	int c;
	int Of, Bf;
	O.clear();
	B.clear();
	Oc = 0;
	Bc = 0;
	fi(1, n) {
		if (p[i].first == 'O') {
			O.pb(p[i].second);
		}
		if (p[i].first == 'B') {
			B.pb(p[i].second);
		}
	}

	ans = 0;

	Ox = 1;
	Bx = 1;

	c = 1;

	while (c <= n) {
		Of = 1;
		Bf = 1;
		if (Oc < SIZE(O) && Ox != O[Oc]) {
			Of = 0;
			if (Ox < O[Oc]) {
				Ox++;
			} else {
				Ox--;
			}
		}
		if (Bc < SIZE(B) && Bx != B[Bc]) {
			Bf = 0;
			if (Bx < B[Bc]) {
				Bx++;
			} else {
				Bx--;
			}
		}

		if (Of && p[c].first == 'O' && Ox == p[c].second) {
			Oc++;
			c++;
		} else if (Bf && p[c].first == 'B' && Bx == p[c].second) {
			Bc++;
			c++;
		}

		ans++;

	}

	printf("%d\n", ans);
}

int main() {
	char s[10];
	int a;
	int i;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &testq);
	for (test = 1; test <= testq; test++) {
		
		scanf("%d", &n);

		fi(1, n) {
			scanf("%s %d", s, &a);
			p[i] = mp(s[0], a);
		}

		printf("Case #%d: ", test);

		Solve();

		fflush(stdout);
	}
	return 0;
}