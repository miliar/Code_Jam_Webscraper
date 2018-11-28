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
#define secon second

using namespace std;

typedef	long long	int64;

struct	Node
{
	int	t, p, n;
};

Node	a[1005];
int	N;


bool	sort_p(const Node &X, const Node &Y)
{
	if (X.p > Y.p) return 1;
	if (X.p < Y.p) return 0;
	return X.n < Y.n;
}

int	main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	
	int	Test;
	scanf("%d", &Test);
	for (int test = 1; test <= Test; ++ test)
	{
		printf("Case #%d: ", test);
		
		scanf("%d", &N);
		for (int i = 1; i <= N; ++ i) scanf("%d", &a[i].t);
		for (int i = 1; i <= N; ++ i) scanf("%d", &a[i].p);
		for (int i = 1; i <= N; ++ i) a[i].n = i;
		sort(a + 1, a + N + 1, sort_p);
		
		for (int i = 1; i <= N; ++ i) printf("%d ", a[i].n - 1);
		puts("");
	}
	
	return 0;
}
