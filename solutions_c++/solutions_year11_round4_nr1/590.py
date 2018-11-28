
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

const int SZ = 1 << 10;

int tests;

int x, s, r, t_, n;

int w[SZ];

int speed[1 << 20];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &tests);
	int I = 0;
	while(tests--)
	{
		scanf("%d%d%d%d%d", &x, &s, &r, &t_, &n);
		memset(speed, 0, sizeof(speed));
		REP(i, n)
		{
			int b, e, w;
			scanf("%d%d%d", &b, &e, &w);
			FOR(j, b, e)
				speed[j] += w;
		}
		sort(speed, speed + x, greater<int>());
		REP(i, x)
			speed[i] += s;
		double res = 0;
		double t = t_;
		RREP(i, x)
		{
			double d = min(1.0, t * (speed[i] + r - s));
			res += d / (speed[i] + r - s);
			t -= d / (speed[i] + r - s);
			res += (1 - d) / speed[i];
		}
		printf("Case #%d: %.10lf\n", ++I, res);
	}
	return 0;
}