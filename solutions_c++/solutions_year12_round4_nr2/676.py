#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <ctime>

using namespace std;

int X[10], Y[10], u[10], W, L;
bool rec(int cur, int n, int xx, int yy, bool xfree, bool yfree, vector<int> &r)
{
	if (cur == n)
		return true;
	for(int i = 0; i < n; i++)
	{
		if (u[i]) continue;
		if (!xfree && xx + r[i] > W)
		{
			int newyy = 0;
			for(int j = 0; j < n; j++)
				if (u[j])
					newyy = max(newyy, Y[j] + r[j]);
			if (newyy + r[i] > L) continue;
			X[cur] = 0;
			Y[cur] = newyy + r[i];
			u[cur] = true;
			if (rec(cur + 1, n, r[i], newyy, 0, 0, r))
				return true;
		}
		u[cur] = true;
		X[cur] = (xfree ? -r[i] : xx) + r[i];
		Y[cur] = (yfree ? -r[i] : yy) + r[i];
		if (Y[cur] > L)
		{
			u[cur] = false;
			continue;
		}
		if (rec(cur + 1, n, X[cur] + r[i], yy, 0, yfree, r))
			return true;
	}
	return false;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;

	cin >> T;

	for(int t = 1; t <= T; t++)
	{
		int n, i, j, k;
		cin >> n >> W >> L;
		vector<int> r(n);
		for(i = 0; i < n; i++)
			cin >> r[i];
		
		for(i = 0; i < n; i++)
			u[i] = false;
		if (!rec(0, n, 0, 0, 1, 1, r))
			puts("NOOO");
		cout << "Case #" << t << ":";
		for(i = 0; i < n; i++)
			printf(" %d %d", X[i], Y[i]);
		puts("");

		for(i = 0; i < n; i++)
		{				
			if (X[i] < 0 || X[i] > W || Y[i] < 0 || Y[i] > L) 
				puts("NO");
			for(j = i + 1; j < n; j++)
			{
				int x1 = max(X[i] - r[i], X[j] - r[j]);
				int x2 = min(X[i] + r[i], X[j] + r[j]);
				int y1 = max(Y[i] - r[i], Y[j] - r[j]);
				int y2 = min(Y[i] + r[i], Y[j] + r[j]);
				if (x1 < x2 && y1 < y2)
					puts("NO");
			}
		}
	}

	return 0;
}