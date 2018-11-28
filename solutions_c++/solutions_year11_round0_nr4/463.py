
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

const int D = 20;

int tests;

int n;

map<Long, double> Map[D];

int buf[D][10];

int a[1 << 10];

Long get_code()
{
	Long res = 0;
	REP(i, n)
		res = res * 10 + a[i];
	return res;
}

void fill(Long r)
{
	RREP(i, n)
	{
		a[i] = r % 10;
		r /= 10;
	}
}

int p[D][10];
int t[D][10];

double solve(int d)
{
	if(d == D)
		return 0;
	Long code = get_code();
	if(Map[d].count(code))
		return Map[d][code];
	memcpy(buf[d], a, sizeof(a));
	double res = -1;
	REP(i, n)
		if(a[i] ^ i)
			res = 1e100;
	FOR(mask, 1, (1 << n))
	{
		memcpy(a, buf[d], sizeof(a));
		bool valid = true;
		int cur = 0;
		REP(i, n)
			if((mask & (1 << i)) && a[i] == i)
				valid = false;
			else if(mask & (1 << i))
				p[d][cur++] = i;
		if(!valid)
			continue;
		double P = 1;
		FOR(i, 1, cur + 1)
			P /= i;
		memcpy(t[d], p[d], sizeof(p[d]));
		double lres = 0;
		do
		{
			REP(i, cur)
				a[t[d][i]] = buf[d][p[d][i]];
			lres += P * solve(d + 1);
		}while(next_permutation(p[d], p[d] + cur));
		res = min(res, lres);
	}
	return Map[d][code] = res + 1;
}

int A[1 << 10];
bool used[1 << 10];

int main1()
{
	scanf("%d", &n);
	REP(i, n)
		A[i] = i;
	do
	{
		REP(i, n)
			a[i] = A[i];
		REP(i, n)
			printf("%d ", A[i]);
		double ans = solve(0);
		int R = (int)(ans + 1e-3);
		printf(" %d", R);
		if(fabs(ans - R) > 1e-3)
			throw -1;
		int r = 0;
		memset(used, 0, sizeof(used));
		REP(i, n)
		{
			int cnt = 0;
			int cur = i;
			do
			{
				used[cur] = true;
				cur = A[cur];
				++cnt;
			}while(!used[cur]);
			if(cnt != 1)
				r += cnt;
		}
		printf(" (%d)\n", r);
		if((r ^ R))
			throw -1;
	}while(next_permutation(A, A + n));
	return 0;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &tests);
	int I = 0;
	while(tests--)
	{
		scanf("%d", &n);
		int cnt = 0;
		REP(i, n)
		{
			scanf("%d", &a[i]);
			--a[i];
		}

		int r = 0;
		memset(used, 0, sizeof(used));
		REP(i, n)
		{
			int cnt = 0;
			int cur = i;
			do
			{
				used[cur] = true;
				cur = a[cur];
				++cnt;
			}while(!used[cur]);
			if(cnt != 1)
				r += cnt;
		}
		printf("Case #%d: %d\n", ++I, r);
	}
	return 0;
}