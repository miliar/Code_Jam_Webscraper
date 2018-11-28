
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

#define SZ 700
#define P 100003

int tests;

Long res[SZ][SZ];
Long C[SZ][SZ];

int n;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	REP(i, SZ)
	{
		C[i][0] = 1;
		FOR(j, 1, i + 1)
			C[i][j] = (C[i - 1][j - 1] + C[i - 1][j])%P;
	}
	FOR(x, 2, 550)
	{
		res[x][1] = 1;
		FOR(i, 2, x)
			FOR(j, 1, i)
				res[x][i] = (res[x][i] + res[i][j]*C[x - i - 1][i - j - 1])%P;
	}
	cin >> tests;
	REP(I, tests)
	{
		cin >> n;
		Long r = 0;
		REP(i, n)
			r += res[n][i];
		r %= P;
		printf("Case #%d: %d\n", I + 1, (int)r);
	}
	return 0;
}