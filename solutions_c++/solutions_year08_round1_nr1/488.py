#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <stdio.h>
using namespace std;

#define ALL(ar)       (ar).begin(),(ar).end()
#define SZ(a)         int((a).size())
#define REP(i,n)      for(int i=0,len123=(n);i<len123;i++)
#define FOR(i,n,m)    for(int i=(n),len123=(m);i<len123;i++)
#define INF           (1<<30)
typedef long long          LL;
typedef long double        LD;
typedef unsigned long long ULL;
typedef vector<int>        VI;
typedef pair<int,int>      II;

int T, N;
int x[1000], y[1000];
LL res;

bool f(int _a, int _b)
{
	return _a > _b;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.in", "rt", stdin);
    freopen("out.out", "wt", stdout);
#endif

	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%d", &N);
		REP(i,N)
			scanf("%d", x+i);
		REP(j,N)
			scanf("%d", y+j);
		sort(x,x+N);
		sort(y,y+N,f);
		res = 0;
		REP(i,N)
			res += x[i]*y[i];
		printf("Case #%d: %d\n", tc+1, res);
	}

    return 0;
}

