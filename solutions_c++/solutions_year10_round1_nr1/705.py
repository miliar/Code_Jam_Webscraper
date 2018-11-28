#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define MAXN 51

char a[MAXN][MAXN], b[MAXN][MAXN];
int dx[4] = { 1, 0, 1,-1};
int dy[4] = { 0, 1, 1, 1};
int n, k;
int tt;

inline void rotate90()
{	
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			b[j][n-1-i] = a[i][j];
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			a[i][j] = b[i][j];
}

char c[MAXN], l;

inline void gravity()
{	
	for (int j = 0; j < n; ++j)
	{
		l = 0;
		for (int i = n-1; i >= 0; --i)
			if (a[i][j]!='.') c[l++] = a[i][j];
		for (int i = n-1, w = 0; i >= 0; --i, ++w)
			if (w>=l)	a[i][j] = '.'; else a[i][j] = c[w];
	}
}

inline bool searchFk()
{
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			if (a[i][j]=='R')
				for (int w = 0; w < 4; ++w)
				{
					int p = 0;
					for (int sx = i, sy = j; sx >= 0 && sx < n && sy >= 0 && sy < n; sx+=dx[w], sy+=dy[w])
							if (a[sx][sy]=='R')
								++p;
							else 
								break;
					if (p>=k) return 1;
				}
	return 0;
}

inline bool searchSk()
{
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			if (a[i][j]=='B')
				for (int w = 0; w < 4; ++w)
				{
					int p = 0;
					for (int sx = i, sy = j; sx >= 0 && sx < n && sy >= 0 && sy < n; sx+=dx[w], sy+=dy[w])
							if (a[sx][sy]=='B')
								++p;
							else 
								break;
					if (p>=k) return 1;
				}
	return 0;
}

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	scanf("%d\n", &tt);
	for (int t = 0; t < tt; ++t)
	{
		scanf("%d%d\n", &n, &k);
		for (int i = 0; i < n; ++i)
			scanf("%s\n", a[i]);
		rotate90();
		gravity();
		bool ok1 = searchFk(), ok2 = searchSk();
		if (ok1 && ok2) 
			printf("Case #%d: Both\n", t+1);
		else if (ok1 && !ok2)
			printf("Case #%d: Red\n", t+1);
		else if (!ok1 && ok2)
			printf("Case #%d: Blue\n", t+1);
		else
			printf("Case #%d: Neither\n", t+1);		
	}
	return 0;
}
