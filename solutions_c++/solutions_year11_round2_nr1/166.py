
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

const int SZ = 1 << 7;

int tests;

int n;

char s[SZ][SZ];

double wp[SZ];
double owp[SZ];
double oowp[SZ];

int ones[SZ], zeros[SZ];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &tests);
	int I = 0;
	while(tests--)
	{
		scanf("%d", &n);
		REP(i, n)
			scanf("%s", s[i]);
		REP(i, n)
		{
			ones[i] = count(s[i], s[i] + n, '1');
			zeros[i] = count(s[i], s[i] + n, '0');
			wp[i] = ones[i] / (double)(ones[i] + zeros[i]);
		}
		REP(i, n)
		{
			double sum = 0;
			int cnt = 0;
			REP(j, n)
				if(s[i][j] != '.')
				{
					int ones_j = ones[j], zeros_j = zeros[j];
					if(s[j][i] == '0')
						--zeros_j;
					else
						--ones_j;
					sum += ones_j / (double)(ones_j + zeros_j);
					++cnt;
				}
			owp[i] = sum / cnt;
		}
		REP(i, n)
		{
			double sum = 0;
			int cnt = 0;
			REP(j, n)
				if(s[i][j] != '.')
				{
					sum += owp[j];
					++cnt;
				}
			oowp[i] = sum / cnt;
		}
		printf("Case #%d:\n", ++I);
		REP(i, n)
			printf("%.10lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
	}
	return 0;
}