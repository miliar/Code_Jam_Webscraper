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
const int N = 110;


int a[N][N], b[N][N], ans;



void Read()
{
	f(i, N) f(j, N) a[i][j] = 0;
	
	int n, x1, x2, y1, y2;
	
	scanf("%d", & n);
	
	f(i, n)
	{
		scanf("%d %d %d %d", & y1, & x1, & y2, & x2);
		
		fo(x, x1, x2) fo(y, y1, y2) a[x][y] = 1;
	}
	
//	system("pause");
}

void Solve()
{
	ans = 0;
	
//	f(i, 10) {f(j, 10) printf("%d", a[i][j]);	printf("\n");}
//	system("pause");
	
	while(1)
	{
	bool done = true;
		
		f(i, N) f(j, N)
		{
		int n = 0;
			
			if(i == 1 && j == 5)
			{
				int fasfas = 15152;
			}
			
			if(0 <= i - 1) n ++;
			if(0 <= j - 1) n ++;
			
			if(a[i][j] == 1)
			{
			int c = 0;
				
				if(0 <= i - 1 && a[i - 1][j] == 1) c ++;
				if(0 <= j - 1 && a[i][j - 1] == 1) c ++;
				
				if(c == 0) {b[i][j] = 0; done = false;}
				else b[i][j] = 1;
			}
			else
			{
			int c = 0;
				
				if(0 <= i - 1 && a[i - 1][j] == 1) c ++;
				if(0 <= j - 1 && a[i][j - 1] == 1) c ++;
				
				if(c == n && n > 0) {b[i][j] = 1; done = false;}
				else b[i][j] = 0;
			}
		}
		
		f(i, N) f(j, N) a[i][j] = b[i][j];
		
//		f(i, 10) {f(j, 10) printf("%d", a[i][j]);	printf("\n");}
//		system("pause");
		
		if(done) break;
		
		ans ++;
	}
	
//	system("pause");
}

void Write(const int test_case)
{
	printf("Case #%d: ", test_case);
	
	printf("%d\n", ans);
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
