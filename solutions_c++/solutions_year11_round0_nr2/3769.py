#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

const int MAX = 29;

int C, D, N;
int c[MAX][MAX], d[MAX][MAX];
int st[209], tp;
string s;

void solve(int t)
{
	tp = -1;

	for(int i = 0; i < s.size(); i++)
	{
		int x = s[i]-'A';

		if(tp == -1) st[++tp] = x;
		else if(c[st[tp]][x] != -1)
		{
			st[tp] = c[st[tp]][x];
		}
		else
		{
			for(int j = 0; j <= tp; j++)
			{
				if(d[x][st[j]]) { tp = -1; break; }
			}
			if(tp != -1) st[++tp] = x;
		}
	}
	printf("Case #%d: [", t);

	if(tp == -1) { printf("]\n"); return ; }

	for(int i = 0; i < tp; i++)
		printf("%c, ", st[i] + 'A');
	printf("%c]\n", st[tp] + 'A');
}


int main()
{
	freopen("B_small_in.txt", "r", stdin);
	freopen("B_small_out.txt", "w", stdout);
	int x, y, z;
	int T; cin >> T;
	for(int t = 1; t <= T; t++)
	{
		memset(c, -1, sizeof(c));
		memset(d, 0, sizeof(d));
		cin >> C;
		for(int i = 0; i < C; i++)
		{
			cin >> s;
			x = s[0] - 'A';
			y = s[1] - 'A';
			z = s[2] - 'A';
			c[x][y] = c[y][x] = z;
		}
		cin >> D;
		for(int i = 0; i < D; i++)
		{
			cin >> s;
			x = s[0] - 'A';
			y = s[1] - 'A';
			d[x][y] = d[y][x] = 1;
		}
		cin >> N >> s;

		solve(t);
	}

	return 0;
}