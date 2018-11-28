#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

using namespace std;
#define MAX 10010
int P, Q;
int mas[110];
int matr[MAX][MAX];

int f(int from, int to)
{
	if (from > to)
		return 0;
	if (matr[from][to] >= 0)
		return matr[from][to];
	int * start = lower_bound(mas, mas + Q, from);
	int * finish = upper_bound(mas, mas + Q, to);
	int res = 1000000000;
	for (; start != finish; start++)
	{
		int a = *start;
		int q = to - from + f(from, a - 1) + f(a + 1, to);
		if (res > q)
			res = q;
	}
	if (res == 1000000000)
		res = 0;
	matr[from][to] = res;
	return res;
}

int main()
{
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		scanf("%d%d", &P, &Q);
		for (int i = 0; i < Q; i++)
			scanf("%d", &mas[i]);
		memset(matr, 255, sizeof(int) * MAX*MAX);
		int res = f(1, P);
		printf("Case #%d: %d\n", t+1, res);
	}
	fclose(stdout);
	return 0;
}