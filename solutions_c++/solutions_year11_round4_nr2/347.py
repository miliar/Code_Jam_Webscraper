#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define sz(a) int((a).size())
#define all(X) (X).begin(), (X).end()
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

int sum[512][512];
char matr[512][512];
int sumx[512][512];
int sumy[512][512];

int getqz(int s, int r)
{
	if (s & 1) {
		return ((s / 2) - r) * 2;
	}
	else {
		return (s - 1) - r - r;
	}
}

int r, c, d;

int getsum(int r1, int c1, int r2, int c2)
{
	return sum[r2 + 1][c2 + 1] - sum[r1][c2 + 1] - sum[r2 + 1][c1] + sum[r1][c1];
}

void initial()
{
	memset(sum, 0, sizeof(sum));
	for (int i = 0; i < r; ++i) {
		int s = 0;
		for (int j = 0; j < c; ++j) {
			s += matr[i][j];
			sum[i + 1][j + 1] = sum[i][j + 1] + s;
		}
	}
}

bool isok(int s)
{
	{
		int sx = 0;
		for (int i = 0; i < s; ++i) {
			for (int j = 0; j < s; ++j) {
				if (i == 0 && j == 0 || i == s - 1 && j == s - 1 || i == s - 1 && j == 0 || i == 0 && j == s - 1) {
					;
				}
				else {
					sx += getqz(s, i) * matr[i][j];
				}
			}
		}
		for (int j = 0; j + s <= c; ++j) {
			if (j == 0) {
				;
			}
			else {
				sx = sumx[0][j - 1];
				for (int i = 1; i < s - 1; ++i) {
					sx -= getqz(s, i) * matr[i][j - 1];
					sx += getqz(s, i) * matr[i][j + s - 1];
				}
				sx -= getqz(s, 0) * matr[0][j];
				sx -= getqz(s, s - 1) * matr[s - 1][j];
				sx += getqz(s, 0) * matr[0][j + s - 2];
				sx += getqz(s, s - 1) * matr[s - 1][j + s - 2];
			}
			sumx[0][j] = sx;
			for (int i = 1; i + s <= r; ++i) {
				sx += 2 * (getsum(i - 1, j, i - 1 + s - 1, j + s - 1) - matr[i - 1][j] - matr[i - 1][j + s - 1] - matr[i - 1 + s - 1][j] - matr[i - 1 + s - 1][j + s - 1]);
				sx += getqz(s, s - 1) * getsum(i + s - 1, j + 1, i + s - 1, j + s - 2);
				sx -= getsum(i - 1, j + 1, i - 1, j + s - 2) * (getqz(s, 0) + 2);
				//sx += getsum(i + s - 1, j + 1, i + s - 1, j + s - 2) * getqz(s, s - 1);
				sx -= (matr[i][j] + matr[i][j + s - 1]) * getqz(s, 0);
				sx += (matr[i + s - 2][j] + matr[i + s - 2][j + s - 1]) * getqz(s, s - 2);
				sumx[i][j] = sx;
			}
		}
	}
	{
		int sy = 0;
		for (int j = 0; j < s; ++j) {
			for (int i = 0; i < s; ++i) {
				if (i == 0 && j == 0 || i == s - 1 && j == s - 1 || i == s - 1 && j == 0 || i == 0 && j == s - 1) {
					;
				}
				else {
					sy += getqz(s, j) * matr[i][j];
				}
			}
		}
		for (int i = 0; i + s <= r; ++i) {
			if (i == 0) {
				;
			}
			else {
				sy = sumy[i - 1][0];
				for (int j = 1; j < s - 1; ++j) {
					sy -= getqz(s, j) * matr[i - 1][j];
					sy += getqz(s, j) * matr[i + s - 1][j];
				}
				sy -= getqz(s, 0) * matr[i][0];
				sy -= getqz(s, s - 1) * matr[i][s - 1];
				sy += getqz(s, 0) * matr[i + s - 2][0];
				sy += getqz(s, s - 1) * matr[i + s - 2][s - 1];
			}
			sumy[i][0] = sy;
			for (int j = 1; j + s <= c; ++j) {
				sy += 2 * (getsum(i, j - 1, i + s - 1, j - 1 + s - 1) - matr[i][j - 1] - matr[i + s - 1][j - 1] - matr[i][j - 1 + s - 1] - matr[i + s - 1][j - 1 + s - 1]);
				sy += getqz(s, s - 1) * getsum(i + 1, j + s - 1, i + s - 2, j + s - 1);
				sy -= getsum(i + 1, j - 1, i + s - 2, j - 1) * (getqz(s, 0) + 2);
				//sy += getsum(i + 1, j + s - 1, i + s - 2, j + s - 1) * getqz(s, s - 1);
				sy -= (matr[i][j] + matr[i + s - 1][j]) * getqz(s, 0);
				sy += (matr[i][j + s - 2] + matr[i + s - 1][j + s - 2]) * getqz(s, s - 2);
				sumy[i][j] = sy;
			}
		}
	}
	for (int i = 0; i + s <= r; ++i) {
		for (int j = 0; j + s <= c; ++j) {
			if (sumx[i][j] == 0 && sumy[i][j] == 0) {
				return true;
			}
		}
	}
	return false;
}

int run()
{
	scanf("%d %d %d", &r, &c, &d);
	for (int i = 0; i < r; ++i) {
		scanf("%s", matr[i]);
		for (int j = 0; j < c; ++j) {
			matr[i][j] -= '0';
		}
	}
	initial();
	for (int s = min(r, c); s >= 3; --s) {
		if (isok(s)) {
			return s;
		}
	}
	return -1;
}

int main()
{
	freopen("B1.in", "r", stdin);
	freopen("B1.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		int ret = run();
		if (ret != -1) {
			printf("Case #%d: %d\n", i, ret);
		}
		else {
			printf("Case #%d: IMPOSSIBLE\n", i);
		}
	}
	return 0;
}