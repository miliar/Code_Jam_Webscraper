#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker,"/STACK:64000000")

#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

const int nmax = 25;
map < lint , int > q;
int n;
lint a[nmax];

void print(int msk)
{
	vector < lint > x;
	for (int i = 0; i < n; i ++)
	{
		if ( (1 << i) & msk )
		{
			x.pb(a[i]);
		}
	}
	for (int i = 0; i < sz(x); i ++)
	{
		if (i) printf(" ");
		printf("%lld",x[i]);
	}
	printf("\n");
}

bool solve()
{
	cin >> n;
	for (int i = 0; i < n; i ++)
		cin >> a[i];
	
	q.clear();
	for (int i = 1; i < (1 << n); i ++)
	{
		lint sum = 0;
		for (int j = 0; j < n; j ++)
		{
			if (i & (1 << j))
			{
				sum += a[j];
			}
		}
		if (q.find(sum) != q.end())
		{
			printf("\n");
			print(q[sum]);
			print(i);
			return false;
		}
		q.insert(mp(sum,i));
	}
	printf(" Impossible\n");
	return false;
}

int main()
{
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		printf("Case #%d:",i + 1);
		solve();
	}
	return 0;
}