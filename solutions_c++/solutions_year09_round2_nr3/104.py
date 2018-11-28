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
const int MAX_N = 30;
const int MAX_Q = 200;
const int ADD = 100;

const int dr[4] = {- 1,   0,   0, + 1};
const int dc[4] = {  0, - 1, + 1,   0};


bool str_cmp(const string & a, const string & b)
{
	if(sz(a) == 0) return false;
	if(sz(b) == 0) return true;
	if(sz(a) != sz(b)) return (sz(a) < sz(b));
	return (a < b);
}

typedef struct type
{
	int r, c, n;
	string s;
	
	type (int _r = 0, int _c = 0, int _n = 0, string _s = "") : r(_r), c(_c), n(_n), s(_s) {}
};

typedef struct cmp
{
	bool operator () (const type & a, const type & b)
	{
		if(a.s != b.s) return(str_cmp(a.s, b.s));
		
		if(a.r != b.r) return (a.r < b.r);
		if(a.c != b.c) return (a.c < b.c);
		
		return false;
	}
};


int N, Q;
string a[MAX_N], ans[MAX_N][MAX_N][MAX_Q];
set<type, cmp> S;


void Read()
{
	f(i, MAX_N) a[i] = "";
	f(i, MAX_N) f(j, MAX_N) f(k, MAX_Q) ans[i][j][k] = "";
	S.clear();
	
	scanf("%d %d", & N, & Q);
	
	f(i, N)
	{
	char buff[1000];
		
		scanf("%s", buff);
		a[i] = buff;
	}
	
//	system("pause");
}

void Solve(const int test_case)
{
	printf("Case #%d:\n", test_case);
	
	f(r, N) f(c, N) if('0' <= a[r][c] && a[r][c] <= '9')
	{
	string t = "";
		t += a[r][c];
//		cerr << t << "#\n";
		
		S.insert(type(r, c, ADD + (a[r][c] - '0'), t));
		ans[r][c][a[r][c] - '0' + ADD] = t;
	}
//	wait;
	
	fx(it, S)
	{
	type now = * it;
		
//		cerr << now.r << "  "<< now.c << "\n";
//		cerr << now.n - ADD << "\n";
//		cerr << now.s << "#\n";
	}
//	wait;
	
	while(!S.empty())
	{
	type now = * S.begin();
		
		S.erase(S.begin());
		
		
	//	cerr << "Now\n";
//		cerr << now.r << "  "<< now.c << "\n";
//		cerr << now.n - ADD << "\n";
//		cerr << now.s << "#\n";
		
		
		
		f(i, 4) f(j, 4)
		{
		int sign_r = now.r + dr[i], sign_c = now.c + dc[i];
		int number_r = sign_r + dr[j], number_c = sign_c + dc[j];
		type next;
		bool add = false;
			
			if(!(0 <= sign_r && sign_r < N) || !(0 <= sign_c && sign_c < N)) continue;
			if(!(0 <= number_r && number_r < N) || !(0 <= number_c && number_c < N)) continue;
			
			if(a[sign_r][sign_c] == '+')
			{
				next.r = number_r;
				next.c = number_c;
				next.n = now.n + (a[number_r][number_c] - '0');
				next.s = now.s + a[sign_r][sign_c] + a[number_r][number_c];
				
				if(next.n < 0 || MAX_Q <= next.n) continue;
				
				if(str_cmp(next.s, ans[next.r][next.c][next.n])) {ans[next.r][next.c][next.n] = next.s; add = true;}
				
				if(add)
				{
					S.insert(next);
					
//					cerr <<"	"<< next.r << "  "<< next.c << "\n";
//					cerr <<"	"<< next.n - ADD << "\n";
//					cerr <<"	"<< next.s << "#\n";
				}
			}
			else
			{
				next.r = number_r;
				next.c = number_c;
				next.n = now.n - (a[number_r][number_c] - '0');
				next.s = now.s + a[sign_r][sign_c] + a[number_r][number_c];
				
				if(next.n < 0|| MAX_Q <= next.n) continue;
				
				if(str_cmp(next.s, ans[next.r][next.c][next.n])) {ans[next.r][next.c][next.n] = next.s; add = true;}
				
				if(add)
				{
					S.insert(next);
					
//					cerr <<"	"<< next.r << "  "<< next.c << "\n";
//					cerr <<"	"<< next.n - ADD << "\n";
//					cerr <<"	"<< next.s << "#\n";
				}
			}
		}
		
//		wait;
	}
	
	f(iter, Q)
	{
	int q;
	string p;
		
		scanf("%d", & q);
		
		f(i, N) f(j, N) if(str_cmp(ans[i][j][q + ADD], p)) p = ans[i][j][q + ADD];
		
		cout << p << "\n";
	}
	
//	system("pause");
}

int main()
{
int TESTS;
	
//	cerr << str_cmp("1+1", "2") << "\n";
	
	scanf("%d", & TESTS);
	
	for(int i = 1; i <= TESTS; i ++)
	{
		Read();
		
		Solve(i);
	}
	
//	system("pause");
	
	return 0;
}

/*
2
5 3
2+1-2
+3-4+
5+2+1
-4-0-
9+5+1
20 30 40
3 2
2+1
+4+
5+1
2 20



*/
