
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

#define SZ 1200

int r, k, n;
int g[SZ];
Long res[SZ];
int s[SZ];

Long solve()
{
	scanf("%d%d%d", &r, &k, &n);
	REP(i, n)
		scanf("%d", &g[i]);
	memset(s, -1, sizeof(s));
	s[0] = 0;
	Long cnt = 0;
	int cur = 0;
	int next;
	Long sum;
	int S = 0;
	bool b = 1;
	while(r)
	{
		sum = g[cur];
		next = cur;
		while((next + 1)%n != cur && sum + g[(next + 1)%n] <= k)
		{
			next = (next + 1)%n;
			sum += g[next];
		}
		cnt += sum;
		--r;
		++S;
		cur = (next + 1)%n;
		if(s[cur] != -1 && b)
		{
			Long c = r/(S - s[cur]);
			cnt += c*(cnt - res[cur]);
			r -= c*(S - s[cur]);
			b = 0;
		}
		else
		{
			s[cur] = S;
			res[cur] = cnt;
		}
	}
	return cnt;
}

int tests;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &tests);
	REP(i, tests)
		printf("Case #%d: %lld\n", i + 1, solve());
	return 0;
}