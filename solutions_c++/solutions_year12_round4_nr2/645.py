
#define _CRT_SECURE_NO_DEPRECATE 

#include <string> 
#include <vector> 
#include <map> 
#include <list> 
#include <set> 
#include <queue> 
#include <iostream> 
#include <sstream> 
#include <stack> 
#include <deque> 
#include <cmath> 
#include <memory.h> 
#include <cstdlib> 
#include <cstdio> 
#include <cctype> 
#include <algorithm> 
#include <utility> 

using namespace std; 

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, b, a) for(int i = (b) - 1; i >= (a); --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)

#define ALL(V) V.begin(), V.end()
#define pb push_back
#define mp make_pair
#define EPS 1e-7
#define Pi 3.14159265358979

typedef long long Long;
typedef unsigned long long ULong;
typedef unsigned int Uint;
typedef unsigned char Uchar;
typedef vector <int> VI;
typedef pair <int, int> PI;

const int SZ = 1 << 10;

int n;
int w, l;

int x[SZ], y[SZ];

int r[SZ];

const int t = 10;

PI p[SZ];

bool valid(int i, int j)
{
	Long d = (Long)(x[i] - x[j]) * (x[i] - x[j]) + (Long)(y[i] - y[j]) * (y[i] - y[j]);
	return d >= (Long)(r[i] + r[j]) * (r[i] + r[j]);
}

bool go(int i)
{
	if(i == n)
		return true;
	REP(cur, t)
	{
		int c = 0;
		if(rand() & 1)
		{
			x[i] = rand() % (w + 1);
			REP(j, i)
				if(abs(x[i] - x[j]) < r[i] + r[j])
				{
					p[c++] = mp(y[j] - r[i] - r[j], y[j] + r[i] + r[j]);
				}
			sort(p, p + c);
			int prev = 0;
			REP(i, c)
			{
				if(prev + r[i] <= p[i].first)
				{
					break;
				}
				prev = max(prev, p[i].second);
			}
			if(prev <= l)
			{
				y[i] = prev;
				if(go(i + 1))
					return true;
			}
		}
		else
		{
			y[i] = rand() % (l + 1);
			REP(j, i)
				if(abs(y[i] - y[j]) < r[i] + r[j])
				{
					p[c++] = mp(x[j] - r[i] - r[j], x[j] + r[i] + r[j]);
				}
			sort(p, p + c);
			int prev = 0;
			REP(i, c)
			{
				if(prev + r[i] <= p[i].first)
				{
					break;
				}
				prev = max(prev, p[i].second);
			}
			if(prev <= w)
			{
				x[i] = prev;
				if(go(i + 1))
					return true;
			}
		}
	}
	return false;
}

PI tmp[SZ];

int rx[SZ], ry[SZ];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	REP(I, tests)
	{
		scanf("%d%d%d", &n, &w, &l);
		REP(i, n)
		{
			scanf("%d", &r[i]);
			tmp[i] = mp(r[i], i);
		}
		sort(tmp, tmp + n);
		reverse(tmp, tmp + n);
		REP(i, n)
			r[i] = tmp[i].first;
		if(!go(0))
			throw -1;
		REP(i, n)
			FOR(j, i + 1, n)
				if(!valid(i, j))
					throw -1;
		REP(i, n)
		{
			rx[tmp[i].second] = x[i];
			ry[tmp[i].second] = y[i];
		}
		cerr << I + 1 << endl;
		printf("Case #%d:", I + 1);
		REP(i, n)
		{
			printf(" %d %d", rx[i], ry[i]);
		}
		puts("");
	}

	return 0;
}