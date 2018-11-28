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

struct	Circle
{
	int	r, n, x, y;
};

Circle	a[5555];
int	x[5555], y[5555], N, W, H;


bool	sort_r(const Circle &X, const Circle &Y)
{
	return X.r > Y.r;
}

bool	sort_n(const Circle &X, const Circle &Y)
{
	return X.n < Y.n;
}

bool	work(int A, int B, int P)
{
	sort(a + 1, a + N + 1, sort_r);
	
	int	L = -a[1].r;
	for (int i = 1; i <= N; )
	{	
		int	R = L + a[i].r * 2;
		int	U = a[i].r;
		
		a[i].x = max(L + a[i].r, 0);
		a[i].y = 0;
		
		if (L + a[i].r >= A) return 0;
		
		for (++ i; i <= N && B - U >= a[i].r; ++ i)
		{
			a[i].x = max(L + a[i].r, 0);
			a[i].y = U + a[i].r;
			U += a[i].r * 2;
		}
		
		L = R;
	}
	
	sort(a + 1, a + N + 1, sort_n);
	
	for (int i = 1; i <= N; ++ i)
	{
		if (P) swap(x[i], y[i]);
		printf("%d %d ", a[i].x, a[i].y);
	}
	puts("");
	return 1;
}

int	main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int	Test;
	scanf("%d", &Test);
	for (int test = 1; test <= Test; ++ test)
	{
		printf("Case #%d: ", test);
		cerr<<test<<endl;
		
		if (test==3)
			int	asd=1;
		
		scanf("%d%d%d", &N, &W, &H);
		for (int i = 1; i <= N; ++ i)
		{
			scanf("%d", &a[i].r);
			a[i].n = i;
		}
		/*
		printf("%d %d %d\n", N, W, H);
		for (int i = 1; i <= N; ++ i) printf("%d ", a[i].r);
		puts("");
		*/
		if (work(W, H, 0)) continue;
		if (work(H, W, 1)) continue;
		
		puts("ERROR");
	}
	
	return 0;
}
