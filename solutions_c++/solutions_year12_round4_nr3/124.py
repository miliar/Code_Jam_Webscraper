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


int	h[55], x[55], N;


int	cmp(double X, double Y)
{
	if (fabs(X - Y) < 1e-10) return 0;
	return X < Y ? -1 : 1;
}

bool	dfs(int n)
{
	if (!n) return 1;
	
	for (h[n] = 1; h[n] <= 20; ++ h[n])
	{
		if (n < N)
		{
			int	t = -1;
			double	k = -1e20;
			for (int i = n + 1; i <= N; ++ i)
				if (cmp(((double)h[i] - h[n]) / (i - n), k) > 0)
				{
					k = ((double)h[i] - h[n]) / (i - n);
					t = i;
				}
			
			if (t != x[n]) continue;
		}
		
		if (dfs(n - 1)) return 1;
	}
	return 0;
}

int	main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	
	int	Test;
	scanf("%d", &Test);
	for (int test = 1; test <= Test; ++ test)
	{
		cerr<<test<<endl;
		printf("Case #%d: ", test);
		
		if (test==4)
			int	asd=1;
		
		scanf("%d", &N);
		for (int i = 1; i < N; ++ i) scanf("%d", &x[i]);
		
		bool	can = dfs(N);
		
		if (!can)
			puts("Impossible");
		else
		{
			for (int i = 1; i <= N; ++ i) printf("%d ", h[i]);
			puts("");
		}
	}
	
	return 0;
}
