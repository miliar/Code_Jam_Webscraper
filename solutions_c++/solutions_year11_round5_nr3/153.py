#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
#include <sstream>
#include <functional>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <queue>

using namespace std;

int nt, n, m;

char c[100][100];

const int MOD = 1000003;

int bit(int mask, int x, int y)
{
	mask &= (1 << (x * m + y));
	return mask != 0;
}

int to_x(int x, int y, int dir)
{
	if (c[x][y] == '-') return x;
		
	// |, /, \
	
	if (dir == 0) return (x - 1 + n) % n;
	return (x + 1 + n) % n;
}

int to_y(int x, int y, int dir)
{
	if (c[x][y] == '|') return y;
	
	if (c[x][y] == '-') 
	{
		if (dir == 0) return (y - 1 + m) % m;
		return (y + 1 + m) % m;
	}

	if (c[x][y] == '/') 
	{
		if (dir == 0) return (y + 1 + m) % m;
		return (y - 1 + m) % m;
	}
	
	// \
	
	if (dir == 0) return (y - 1 + m) % m;
	return (y + 1 + m) % m;
}

int main()
{
	int nt;
	scanf("%d", &nt);
	for(int tt = 1; tt <= nt; tt++)
	{
		fprintf(stderr, "test = %d\n", tt);
		printf("Case #%d: ", tt);
		
		scanf("%d %d ", &n, &m);
		for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++) scanf(" %c ", &c[i][j]);
		
		int all = (1 << (n * m)) - 1;
		
		int res = 0;
		
		for(int i = 0; i <= all; i++)
		{
			bool ok = true;
			
			for(int x = 0; x < n; x++)
			for(int y = 0; y < m; y++)
			{
				int cnt = 0;
				for(int dx = -1; dx <= 1; dx++)
				for(int dy = -1; dy <= 1; dy++)
				if (dx || dy)
				{
					int xx = (x + dx + n) % n;
					int yy = (y + dy + m) % m;
					
					cnt += (to_x(xx, yy, bit(i, xx, yy)) == x && to_y(xx, yy, bit(i, xx, yy)) == y);
				}
				
				if (cnt != 1) ok = false;
			}
			
			if (ok) res++;
		}		
		
		printf("%d\n", res % MOD);
	}
	return 0;
}