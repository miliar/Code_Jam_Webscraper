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

lint dist2(pii a,pii b)
{
	lint dx = a.first - b.first, dy = a.second - b.second;
	return dx * dx + dy * dy;
}

bool solve()
{
	vector < double > angs;
	int n,m,d;
	char s[35][35];
	scanf("%d%d%d",&n,&m,&d);
	for (int i = 0; i < n; i ++)
	{
		scanf("%s",s[i]);
	}
	pii me;
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < m; j ++)
		{
			if (s[i][j] == 'X')
			{
				me = mp(i - 1,j - 1);
				break;
			}
		}
	}
	n -= 2;
	m -= 2;
	n *= 2;
	m *= 2;
	d *= 2;
	me.first = me.first * 2 + 1;
	me.second = me.second * 2 + 1;

	int DELTA = 100;
	int ans = 0;
	for (int it = -DELTA; it <= DELTA; it ++)
	{
		for (int it2 = -DELTA; it2 <= DELTA; it2 ++)
		{
			if (it == 0 && it2 == 0) continue;

			pii me2 = me;
			if (abs(it) & 1)
				me2.first = n - me.first;
			if (abs(it2) & 1)
				me2.second = m - me.second;
			me2.first += n * it;
			me2.second += m * it2;
			if (dist2(me,me2) <= d * d)
			{
				double angle = atan2((double)me2.second - me.second,(double)me2.first - me.first);
				bool ok = true;
				for (int i = 0; i < sz(angs); i ++)
				{
					if (fabs(angs[i] - angle) < eps)
					{
						ok = false;
						break;
					}
				}
				if (ok)
				{
					angs.pb(angle);
					ans++;
				}
			}
		}
	}
	printf("%d\n",ans);
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