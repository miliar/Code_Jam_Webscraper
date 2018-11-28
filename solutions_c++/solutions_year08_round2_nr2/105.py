#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <sstream>
#include <cstdlib>
#include <cassert>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)

#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair

typedef  vector<int> VI;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"
typedef long long ll;
const int NMAX = 1000005;
int p[NMAX];

int up(int x) {
	if (x == p[x]) return x;
	p[x] = up(p[x]);
	return p[x];	
}

void un(int x, int y) {
	x = up(x);
	y = up(y);
	if (x == y) return;
	if (rand() & 1) { 
		p[x] = y;
	} else {
		p[y] = x;
	}
}

bool used[NMAX];

bool isPrime(int x) {
	for(int i = 2; i * i <= x; i++) {
		if (x % i == 0) return false;
	}
	return true;
}


int main()
{
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);
	int tc; cin >> tc;
	for1(it, tc) {
		ll a, b, c;
		cin >> a >> b >> c;
		int len = (b - a + 1);
		forn(i, len) p[i] = i;
		int end = (int)min(b + 1, 1000001ll);
		if (c < end) {
		for(int x = (int)c; x < end; x++) {
			if (!isPrime(x)) continue;
			int s = int(((a + x - 1) / x) * x - a);
			int k = s + x;

			while (k < len) {
				un(s, k);
				k += x;
			}
		}
		}

		memset(used, 0, sizeof(used));

		int ans = 0;
		forn(i, len) {
			used[up(i)] = true;
		}
		forn(i, len) if (used[i]) ans++;

		printf("Case #%d: %d\n", it, ans);


	}

	return 0;
}
