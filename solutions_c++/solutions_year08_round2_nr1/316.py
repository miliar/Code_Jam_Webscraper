//Maked by diver_ru, maked with love^^
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>

FILE *fi = fopen("input.txt", "r"), *fo = fopen("output.txt", "w");

using namespace std;

typedef long long int64;

int n;

int cnt[3][3];
int64 answer;

void readData()
{
	memset(cnt, 0, sizeof cnt);
	int n, A, B, C, D, x0, y0, M;
	fscanf(fi, "%d", &n);
	fscanf(fi, "%d%d%d%d", &A, &B, &C, &D);
	fscanf(fi, "%d%d", &x0, &y0);
	fscanf(fi, "%d", &M);
	int X = x0, Y = y0;
	for (int i = 0; i < n; ++i){
		++cnt[X % 3][Y % 3];
		X = (int)((((int64)A) * X + B) % M);
		Y = (int)((((int64)C) * Y + D) % M);
	}
}

int64 getCount(int p1, int p2, int p3)
{
	int a = cnt[p1 / 3][p1 % 3],
		b = cnt[p2 / 3][p2 % 3],
		c = cnt[p3 / 3][p3 % 3];
	if (p1 == p2 && p2 == p3)
		return (a > 2) ? (int64)a * (a - 1) * (a - 2) / 6 : 0;
	if (p1 == p2 && p2 != p3)
		return (a > 1) ? (int64)a * (a - 1) / 2 * c : 0;
	if (p1 != p2 && p2 == p3)
		return (b > 1) ? (int64)b * (b - 1) / 2 * a : 0;
	return ((int64) a * b * c);
}

void solve()
{
	answer = 0;
	for (int p1 = 0; p1 < 9; ++p1)
		for (int p2 = p1; p2 < 9; ++p2){
			int p3 = ((6 - p1 / 3 - p2 / 3) % 3) * 3 + (6 - p1 % 3 - p2 % 3) % 3;
			if (p3 >= p2)
				answer += getCount(p1, p2, p3);
		}
}

void writeResult()
{
	fprintf(fo, "%lld\n", answer);
}

int main()
{
	int T;
	fscanf(fi, "%d", &T);
	for (int i = 0; i < T; ++i){
		readData();
		solve();
		fprintf(fo, "Case #%d: ", i + 1);
		writeResult();
	}
	return 0;
}