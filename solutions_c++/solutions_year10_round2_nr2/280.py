
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

#define SZ 1000

int tests;

Long n, k, b, t;

int x[SZ], v[SZ];

bool can[SZ];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> tests;
	REP(I, tests)
	{
		cin >> n >> k >> b >> t;
		REP(i, n)
			cin >> x[i];
		REP(i, n)
			cin >> v[i];
		REP(i, n)
			if(x[i] + v[i]*t >= b)
				can[i] = 1;
			else
				can[i] = 0;
		int c = 0;
		int res = 0;
		int cnt = 0;
		RREP(i, n)
			if(can[i] && c < k)
			{
				res += cnt;
				++c;
			}
			else if(!can[i])
				++cnt;
		if(c < k)
		{
			printf("Case #%d: IMPOSSIBLE\n", I + 1);
			continue;
		}
		printf("Case #%d: %d\n", I + 1, res);
	}
	return 0;
}