
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

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define ALL(V) V.begin(), V.end()
#define SIZE(V) (int)V.size()
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

int tests;

int n, d;

PI x[1 << 8];

int p[1 << 8], v[1 << 8];

bool can(Long tm)
{
	Long prev;
	REP(i, n)
	{
		Long Min = p[i] - tm;
		if(i)
			Min = max(Min, prev + d);
		Long Max = Min + (v[i] - 1LL) * d;
		Long d1 = Min - p[i], d2 = Max - p[i];
		if(d1 < 0) d1 = -d1;
		if(d2 < 0) d2 = -d2;
		if(d1 > tm || d2 > tm)
			return false;
		prev = Max;
	}
	return true;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &tests);
	int I = 0;
	while(tests--)
	{
		scanf("%d%d", &n, &d);
		d *= 2;
		REP(i, n)
		{
			scanf("%d%d", &x[i].first, &x[i].second);
			x[i].first *= 2;
		}
		sort(x, x + n);
		REP(i, n)
			p[i] = x[i].first, v[i] = x[i].second;
		Long Min = 0, Max = 1LL << 60, Mid;
		do
		{
			Mid = (Min + Max) >> 1;
			if(can(Mid))
				Max = Mid;
			else
				Min = Mid;
		}while(Max - Min > 1);
		Long res;
		if(can(Min))
			res = Min;
		else if(can(Max))
			res = Max;
		else
			throw -1;
		printf("Case #%d: %lld.%lld\n", ++I, res / 2, (res % 2) * 5);
	}
	return 0;
}