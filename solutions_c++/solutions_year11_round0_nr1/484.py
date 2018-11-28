#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

const double pi = 3.1415926535;
const double eps = 1e-6;

int n, a1, tx[1000], ty[1000], nx[1000], ny[1000], x, y;
char ch;
int Abs(int a)
{
	return a < 0 ? -a : a;
}
void walk(int &a, int b, int c)
{
	if (Abs(a - b) <= c)
		a = b;
	else {
		if (a > b)
			a -= c;
		else
			a += c;
	}
}
int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T, tt = 0;
	for (scanf("%d", &T); T; T--) {
		scanf("%d", &n);
		x = 0, y = 0;
		for (int i = 0; i < n; i++) {
			scanf(" %c %d", &ch, &a1);
			if (ch == 'O') {
				nx[++x] = a1;
				tx[x] = i;
			}
			else {
				ny[++y] = a1;
				ty[y] = i;
			}
		}
		nx[x + 1] = 1992837465;
		tx[x + 1] = 1992837465;
		ny[y + 1] = 1992837465;
		ty[y + 1] = 1992837465;
		int sx = 1, sy = 1, hx = 1, hy = 1, ans = 0;
		for (int i = 0; i < n; i++) {
			int del;
			if (tx[hx] == i)
				del = Abs(nx[hx] - sx);
			else
				del = Abs(ny[hy] - sy);
			walk(sx, nx[hx], del);
			if (sx != nx[hx])
				walk(sx, nx[hx], 1);
			else
			if (i == tx[hx])
				hx++;
			walk(sy, ny[hy], del);
			if (sy != ny[hy])
				walk(sy, ny[hy], 1);
			else
			if (i == ty[hy])
				hy++;
//			cout << sx << ' ' << sy << ' ' << del << endl;
			ans += del + 1;
		}
		tt++;
		printf("Case #%d: %d\n", tt, ans);
	}
}

