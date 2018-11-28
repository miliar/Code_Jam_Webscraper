#include <iostream>
#include <fstream>
#include <stdio.h>
#include <iomanip>
#include <algorithm>
#include <string>
#include <cctype>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <functional>
#include <stdarg.h>
#include <stdlib.h>
#include <iterator>
#include <math.h>
#include <complex>
#include <numeric>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef complex<double> point;
typedef complex<double> Vector;
typedef pair<point, point> Segment;
typedef pair<int, int> PII;
typedef pair<int, double> PID;
typedef pair<int, string> PIS;
typedef pair<PII, PII> PPII;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<point> VP;
typedef vector<VI> VVI;
typedef vector<VD> VVD;
typedef vector<VVI> VVVI;
typedef vector<PII> VPII;
typedef vector<string> VS;

#define f(i, n)					for(int i = 0; i < n; i++)
#define fo(i, a, b)				for(int i = a; i <= b; i++)
#define fx(it, x)				for(typeof((x).begin()) it = (x).begin(); it != (x).end();++it)
#define popcount(n)				__builtin_popcount(n)
#define clz(n)					__builtin_clz(n)
#define ctz(n)					__builtin_ctz(n)
#define gcd(a, b)				__gcd(a, b)
#define lcm(a, b)				((a) / gcd(a, b) * b)
#define nom						first
#define den						second
#define sz(a)					(int(a.size()))
#define pb						push_back
#define all(v)					v.begin(), v.end()
#define EQ(a, b)				(abs((a) - (b)) < EPS)
#define sqr(a)					((a) * (a))
#define cl(x, el)				memset(x, el, sizeof(x))
#define wait					system("pause")
#define Get_Time(time)			(double)((double)(clock() - time) / (double)CLOCKS_PER_SEC)

inline LL strtoint(const string &s) {stringstream ss;ss<<s;LL ret;ss>>ret;return ret;}
inline string inttostr(const LL &a) {stringstream ss;ss<<a;string ret;ss>>ret;return ret;}

const double INF = 1e50;
const double EPS = 1e-9;
const double Pi = acos(- 1.0);
const int MAX = 1 << 28;
const int MIN = - MAX;
const int MAX_N = 550;



int R, C, diff, ans[MAX_N];
int a[MAX_N][MAX_N], dp[MAX_N][MAX_N];


void Read()
{
char temp[MAX_N];
	
	
	scanf("%d %d", & R, & C);
	
	f(r, R)
	{
	int c = 0;
		
		if(r == 1)
		{
			int afvafa = 1212412;
		}
		
		scanf("%s", temp);
		
		f(j, C / 4)
		{
		int mask;
			
			if('0' <= temp[j] && temp[j] <= '9')
			{
				mask = temp[j] - '0';
			}
			else
			{
				mask = 10 + temp[j] - 'A';
			}
			
			
			for(int k = 3; 0 <= k; k --)
				if(mask & (1 << k)) a[r][c ++] = 0;
				else a[r][c ++] = 1;
		}
	}
	
	
//	system("pause");
}

void Fix()
{
	f(r, R) f(c, C)
	{
			if(1 < a[r][c]) {dp[r][c] = - 1; continue;}
			
			dp[r][c] = 1;
			
			for(int k = 2; r + k - 1 < R && c + k - 1 < C; k ++)
			{
			bool good = true;
				
				fo(x, r, r + k - 1) fo(y, c, c + k - 1)
				{
					if(1 < a[x][y]) good = false;
					
					if((x - r + y - c) % 2 == 0 && a[r][c] != a[x][y]) good = false;
					if((x - r + y - c) % 2 == 1 && a[r][c] == a[x][y]) good = false;
					
					if(good == false) goto next;
				}
				
				dp[r][c] = k;
				continue;
				
				next: break;
			}
	}
}

void Solve()
{
	diff = 0;
	f(i, MAX_N) ans[i] = 0;
	
	Fix();
	
	while(1)
	{
	int best = - 1, x = - 1, y = - 1;
		
		f(r, R) f(c, C)
		{
			if(best < dp[r][c])
			{
				x = r;
				y = c;
				
				best = dp[r][c];
			}
		}
		
		if(best < 0) return;
		
//		fprintf(stderr, "best = %d\n", best);
		
		if(ans[best] == 0) diff ++;
		
		ans[best] ++;
		
		fo(r, x, x + best - 1) fo(c, y, y + best - 1)
			a[r][c] = 9;
		
		Fix();
		
/*		f(r, R)
		{
			f(c, C)
				fprintf(stderr, "%d", a[r][c]);
			fprintf(stderr, "\n");
		}
		
		f(r, R)
		{
			f(c, C)
				fprintf(stderr, "%d  ", dp[r][c]);
			fprintf(stderr, "\n");
		}
		
		system("pause");*/
	}
}

void Write(const int test_case)
{
	printf("Case #%d: ", test_case);
	
	printf("%d\n", diff);
	
	for(int i = MAX_N - 1; 0 < i; i --)
		if(0 < ans[i]) printf("%d %d\n", i, ans[i]);
}

int main()
{
int TESTS;
	
	scanf("%d", & TESTS);
	
	for(int i = 1; i <= TESTS; i ++)
	{
		Read();
		
		Solve();
		
		Write(i);
	}
	
//	system("pause");
	
	return 0;
}
