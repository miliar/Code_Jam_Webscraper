#define _USE_MATH_DEFINES 
#define _CRT_SECURE_NO_DEPRECATE
#include <cmath> 
#include <iostream> 
#include <algorithm> 
#include <cstdio> 
#include <ctime> 
#include <map> 
#include <string> 
#include <vector> 
#include <set> 
#include <stack> 
#include <queue> 
#include <deque> 
#include <iomanip>
#include <sstream>

using namespace std; 

#pragma comment(linker, "/STACK:64000000") 
typedef long long int64; 
typedef unsigned long long uint64; 
template<class T> inline T sqr(T a) {return a * a;} 
#define prime 1103 
#define INF 123456789
#define TASK "B-small-attempt0"
#define MOD 1000000007


pair<int, int> f(int val, int p)
{
	pair<int, int> res(0, 0);

	for(int a = 0; a < 11; ++a)
	{
		for(int b = 0; b < 11; ++b)
		{
			for(int c = 0; c < 11; ++c)
			{
				if(a + b + c != val || abs(a - b) > 2 || 
					abs(b - c) > 2 || abs(a - c) > 2 ||
					max(a, max(b, c)) < p) continue;
				if(abs(a - b) == 2 || abs(b - c) == 2 || 
					abs(a - c) == 2)
				{
					res.first = 1;
					if(res.second) return res;
					continue;
				}
				res.second = 1;
				if(res.first) return res;
			}
		}
	}
	return res;
}

int ans(int qs, int qt, int q, int s, int n)
{
	if(qs + qt + q == 0) return 0;
	if(qs >= s) 
		return q + s + qt;
	if(qs + qt + q <= s)
		return qs + qt;
	if(qs < s)
	{
		if(qs + qt == s)
			return s + q;
		if(qs + qt > s) 
			return qs + qt + q;
		if(qs + qt < s)
			return 2 * qs + 2 * qt + q - s;
	}
}


int main()
{
	freopen(TASK ".in", "r", stdin); 
	freopen(TASK ".out", "w", stdout); 
	int t;
	scanf("%d", &t);
	for(int test = 0; test < t; ++test)
	{
		int n, s, p;
		scanf("%d%d%d", &n, &s, &p);
		int qs = 0, qt = 0, q = 0;
		for(int i = 0; i < n; ++i)
		{
			int val;
			scanf("%d", &val);
			pair<int, int> pt = f(val, p);
			if(pt.first && pt.second)
			{
				++qt;
				continue;
			}
			if(pt.first) ++qs;
			if(pt.second) ++q;
		}
		int res = ans(qs, qt, q, s, n);
		printf("Case #%d: %d\n", test + 1, res);
	}
	return 0; 
}