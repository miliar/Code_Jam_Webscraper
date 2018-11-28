#ifdef ONLINE_JUDGE
#pragma comment(linker, "/STACK:16777216")
#endif

#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <stack>
#include <sstream>
#include <cstring>
#include <numeric>
#include <ctime>

#define re return
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int) (x).size())
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rrep(i, n) for (int i = (n) - 1; i >= 0; i--)
#define y0 y32479
#define y1 y95874
#define fill(x, y) memset(x, y, sizeof(x))
#define sqr(x) ((x) * (x))
#define prev prev239
#define next next239
#define hash hash239
#define rank rank239

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef long long ll;
typedef double D;
typedef long double LD;

template<class T> T abs(T x) {return x > 0 ? x : -x;}

int n;
int m;

int mas[1000];
int was[1000];

int go(int x) {
	int ans = 1;
	int sx = x;
	was[x] = 1;
	x = mas[x];
	while (x != sx) {
		was[x] = 1;
		x = mas[x];
		ans++;
	}
	re ans;
}

void zlo(int n) {
	int col[100];
	int smas[100];
	rep(i, n)
		smas[i] = i;
	double sum = 0;
	int c1 = 0, c2 = 0;
	do {
		c1++;
		fill(was, 0);
		memcpy(mas, smas, sizeof(smas));
		rep(i, n) {
			if (was[mas[i]])
				continue;
			int len = go(mas[i]);
			if (len == n) {
				c2++;
			}
			else
				if (len > 1)
				sum += len;
		}
	}
	while (next_permutation(smas, smas + n));
	cout << c1 << ' ' << c2 << ' ' << sum << endl;
	cout << (sum + c1) / (double) (c1 - c2) << endl;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tc;
	cin >> tc;
	rep(tt, tc) {
		cout << "Case #" << tt + 1 << ": ";

		cin >> n;
		rep(i, n) {
			cin >> mas[i];
			mas[i]--;
		}

		int col = 0;
		fill(was, 0);
		rep(i, n) {
			if (was[mas[i]])
				continue;
			int len = go(mas[i]);
			if (len > 1)
				col += len;
/*
			if (len == 2)
				col += 2;
			if (len == 3)
				col += 3;
			if (len > 3)
				col += 2 * (len - 1); */
		}

		printf("%.6lf", (double) (col));
		cout << endl;
	}

	re 0;
}

