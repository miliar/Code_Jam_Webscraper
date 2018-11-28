//Problem B. Dancing With the Googlers
#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

#define sqr(x) ((x) * (x))
#define minn(x,y) (x=(y)<(x)?(y):(x))
#define maxx(x,y) (x=(y)>(x)?(y):(x))
#define pluss(x,y) (x+=(y),x%=mod)

using namespace std;

typedef	long long	int64;


int	n[35][15], s[35][15], a[105], f[105][105], N, S, P;


int	main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	for (int i = 0; i <= 10; ++ i)
	for (int j = i; j <= 10; ++ j)
	for (int k = j; k <= 10; ++ k)
		if (k - i <= 1)	n[i + j + k][k] = 1; else
		if (k - i <= 2) s[i + j + k][k] = 1;
	
	for (int i = 0; i <= 30; ++ i)
	for (int j = 9; j >= 0; -- j)
		n[i][j] |= n[i][j + 1], s[i][j] |= s[i][j + 1];
	
	int	Test;
	scanf("%d", &Test);
	for (int test = 1; test <= Test; ++ test)
	{
		scanf("%d%d%d", &N, &S, &P);
		for (int i = 1; i <= N; ++ i) scanf("%d", &a[i]);
		
		memset(f, -60, sizeof(f)); f[0][0] = 0;
		for (int i = 1; i <= N; ++ i)
		for (int j = 0; j <= N; ++ j) if (f[i - 1][j] >= 0)
		{
			maxx(f[i][j], f[i - 1][j] + n[a[i]][P]);
			maxx(f[i][j + 1], f[i - 1][j] + s[a[i]][P]);
		}
		
		printf("Case #%d: %d\n", test, f[N][S]);
	}
	
	return 0;
}
