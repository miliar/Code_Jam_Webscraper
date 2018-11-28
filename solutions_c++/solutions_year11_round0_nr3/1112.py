#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>
#include <string>
#include <queue>
#include <stack>
#include <list>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <functional>
#include <algorithm>
#include <numeric>
#include <iomanip>
#include <memory.h>
#include <cstdlib>
#include <cmath>
#include <cstdio>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define RFOR(i, b, a) for (int i = (b) - 1; i >= (a); --i)
#define REP(i, n) FOR(i, 0, n)
#define RREP(i, n) RFOR(i, n, 0)

#define pb push_back
#define mp make_pair
#define ALL(v) v.begin(), v.end()

typedef long long Long;
typedef unsigned long long ULong;
typedef vector<int> VI;
typedef pair<int, int> PI;

int a[1<<10];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T,n;
	cin>>T;
	REP(tests, T)
	{
		scanf("%d",&n);
		int x=0;
		REP(i,n)
		{
			scanf("%d",&a[i]);
			x^=a[i];
		}

		int mn=*min_element(a,a+n);
		int sum=accumulate(a,a+n,0);

		printf("Case #%d: ",tests+1);
		if (x!=0)
			puts("NO"); else
			printf("%d\n",sum-mn);
	}
	return 0;
}