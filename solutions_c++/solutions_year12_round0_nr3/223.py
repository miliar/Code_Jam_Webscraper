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
	freopen("input.txt","r", stdin);
#ifndef _DEBUG
	freopen("output.txt","w",stdout);
#endif
}

set < pii > q;

int getlen(int x)
{
	int p = 1;
	for (int i = 0; ; i ++)
	{
		if (x < p) return i;
		p *= 10;
	}
}

int a,b;
void go(int x)
{
	int len = getlen(x);
	int p = 10;
	int pp = 1;
	for (int i = 0; i < len - 1; i ++) pp *= 10;
	for (int i = 0; i < len - 1; i ++, p *= 10, pp /= 10)
	{
		int y = x / p + (x % p) * pp;
		if (getlen(x) == getlen(y) && x != y && a <= y && y <= b)
		{
			if (!q.count(mp(x,y)) && !q.count(mp(y,x)))
			{
				q.insert(mp(x,y));
			}
		}
	}
}

bool solve()
{
	q.clear();
	scanf("%d%d",&a,&b);
	for (int i = a; i <= b; i ++)
		go(i);
	printf("%d\n",sz(q));
	return false;
}

int main()
{
	prepare();
	int nTests;
	scanf("%d",&nTests);
	for (int i = 0; i < nTests; i ++)
	{
		printf("Case #%d: ",i + 1);
		solve();
	}
	return 0;
}