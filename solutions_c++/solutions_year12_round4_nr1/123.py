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


pair<int,int>	a[10005];
int		f[10005], N, M;


int	main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int	Test;
	scanf("%d", &Test);
	for (int test = 1; test <= Test; ++ test)
	{
		printf("Case #%d: ", test);
		
		cerr<<test<<endl;
		
		scanf("%d", &N);
		for (int i = 1, x, l; i <= N; ++ i)
			scanf("%d%d", &a[i].first, &a[i].second);
		scanf("%d", &M);
		
		memset(f, 60, sizeof(f));
		
		int	Ans = 0;
		for (int i = N; i; -- i)
		{
			if (a[i].first + a[i].second >= M) f[i] = M - a[i].first;
			for (int j = i + 1; j <= N; ++ j)
				if (a[j].first - a[i].first >= f[j])
				if (a[i].first >= a[j].first - a[i].second)
					f[i] = min(f[i], a[j].first - a[i].first);
		}
		
		puts(a[1].first >= f[1] ? "YES" : "NO");
	}
	
	return 0;
}
