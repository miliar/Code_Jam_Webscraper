#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <stack>

using namespace std;

#define pb push_back
#define mp make_pair
#define fir first
#define fi first
#define sec second
#define y1 botva23
typedef long long int64;
typedef long double ld;

const int inf = 2000000000;
const ld eps = 1e-07;

int prec[2001000];

int rev(int x, int y) {
	//cerr << x <<  " " << y << endl;
	vector <int> a, b;
	a.clear();
	b.clear();
	while (x) {
		a.pb(x % 10);
		x = x / 10;
	}
	while (y) {
		b.pb(y % 10);
		y = y / 10;
	}
	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());
	if (a.size() != b.size())
		return 0;
	for (int i = 0; i <= a.size(); ++i) {
		int x = a[0];
		for (int t = 1; t < a.size(); ++t)
			a[t - 1] = a[t];
		a[a.size() - 1] = x;
		for (int j = 0; j <= b.size(); ++j) {
			if (a == b)
				return 1;
			x = b[0];
			for (int t = 1; t < b.size(); ++t)
				b[t - 1] = b[t];
			b[b.size() - 1] = x;
		}
	}
	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	//for (int i = 1; i <= 2000000; ++i)
	//	rev(i);
	for (int x = 0; x < t; ++x) {
		cerr << x << endl;
		int l, r;
		scanf("%d %d", &l, &r);
		int res = 0;
		for (int i = l; i <= r; ++i)
			for (int j = i + 1; j <= r; ++j)
				res += rev(i, j);
		printf("Case #%d: %d\n", x + 1, res);
	}
	return 0;
}