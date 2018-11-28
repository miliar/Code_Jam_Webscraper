#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cassert>

using namespace std;

typedef long long int64;

const int MAX = 1000005;

int pos[MAX], n;

bool check(int64 M, int D)
{
	int64 x = pos[0] - M;
	for (int i = 1; i < n; i++)
	{
		int64 y = x + D;
		if (pos[i] + M < y) return false;
		x = max(pos[i] - M, y);
	}
	return true;
}

int main()
{
	freopen("f:\\B-small-attempt0.in", "r", stdin);
	freopen("f:\\B-small-attempt0.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		int C, D, P, V;
		scanf("%d %d", &C, &D);
		D *= 2;
		n = 0;
		while (C--)
		{
			scanf("%d %d", &P, &V);
			while (V--) pos[n++] = P * 2;
		}
		int64 L = 0, H = 0x3f3f3f3f3f3f3f3fLL;
		while (L < H)
		{
			int64 M = (L + H) / 2;
			if (check(M, D))
				H = M;
			else
				L = M + 1;
		}
		printf("Case #%d: %.10f\n", t_case, L / 2.0);
	}
	return 0;
}
