//Problem C. Recycled Numbers
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

const	int	maxn = 2000000;

set<int>	hash[maxn + 5];
int		A, B;


int	main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	
	for (int i = 10; i <= maxn; ++ i)
	{
		int	d = (int)(log10(i) + 1e-9);
		d = (int)(pow(10.0, d) + 1e-9);
		
		int	x = i;
		for (int j = 1; j <= 10; ++ j)
		{
			x = x % 10 * d + x / 10;
			if (x < i) hash[i].insert(x);
		}
	}
	
	int	Test;
	scanf("%d", &Test);
	for (int test = 1; test <= Test; ++ test)
	{
		scanf("%d%d", &A, &B);
		
		int	Ans = 0;
		for (int i = A; i <= B; ++ i)
		for (set<int>::iterator j = hash[i].begin(); j != hash[i].end(); ++ j)
			Ans += (*j) >= A;
		
		printf("Case #%d: %d\n", test, Ans);
	}
	
	return 0;
}
