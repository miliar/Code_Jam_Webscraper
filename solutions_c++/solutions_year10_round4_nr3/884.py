/*
 * Author: rush
 * Created Time:  2010年06月05日 星期六 22时34分28秒
 * File Name: icpc/GCJ/C.cpp
 */
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;
typedef long long LL;

int T, R, X1, Y1, X2, Y2;
int cell[105][105], newcell[105][105];
int h, w;

int solve()
{
	int cnt = 0;
	while (true)
	{
		bool zero = true;
		for (int i = 1; i <= h; ++i)
			for (int j = 1; j <= w; ++j)
			{
				cell[i][j] = newcell[i][j];
				if (cell[i][j] == 1) zero = false;
			}
		if (zero) break;
		
		++cnt;
		for (int i = 1; i <= h; ++i)
			for (int j = 1; j <= w; ++j)
			{
				newcell[i][j] = cell[i][j];
				if (cell[i - 1][j] == 0 && cell[i][j - 1] == 0 && cell[i][j] == 1)
					newcell[i][j] = 0;
				if (cell[i - 1][j] == 1 && cell[i][j - 1] == 1 && cell[i][j] == 0)
					newcell[i][j] = 1;
			}
	}
	return cnt;
}

int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	cin >> T;
	for (int id = 1; id <= T; ++id)
	{
		cin >> R;
		memset(cell, 0, sizeof(cell));
		memset(newcell, 0, sizeof(newcell));
		h = w = 0;
		for (int i = 0; i < R; ++i)
		{
			cin >> X1 >> Y1 >> X2 >> Y2;
			h = max(h, X2);
			w = max(w, Y2);
			for (int j = X1; j <= X2; ++j)
				for (int k = Y1; k <= Y2; ++k)
					cell[j][k] = newcell[j][k] = 1;
		}
		cout << "Case #" << id << ": " << solve() << endl;
	}
    return 0;
}
