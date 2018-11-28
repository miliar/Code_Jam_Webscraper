
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

const int SZ = 20000;

int d[SZ], l[SZ];
int res[SZ];

int n, D;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	REP(I, tests)
	{
		scanf("%d", &n);
		REP(i, n)
			scanf("%d%d", &d[i], &l[i]);
		memset(res, -1, sizeof(res));
		scanf("%d", &D);
		int ans = 0;
		res[0] = d[0];
		REP(i, n)
		{
			if(res[i] != -1)
				ans = max(ans, d[i] + res[i]);
			FOR(j, i + 1, n)
			{
				if(res[i] >= d[j] - d[i])
					res[j] = max(res[j], min(l[j], d[j] - d[i]));
			}
		}
		printf("Case #%d: ", I + 1);
		if(ans >= D)
			puts("YES");
		else
			puts("NO");
	}
	return 0;
}