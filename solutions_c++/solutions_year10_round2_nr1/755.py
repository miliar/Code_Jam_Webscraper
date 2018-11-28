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
const int MAX_N = 1000;



int N, M, ans;
string s[MAX_N];



void Read()
{
	cin >> N >> M;
	
	f(i, N) cin >> s[i];
	f(i, M) cin >> s[N + i];
	
//	system("pause");
}

void Solve()
{
	ans = 0;
	
	f(i, N + M) f(j, sz(s[i])) if(s[i][j] == '/') s[i][j] = ' ';
	
	fo(i, N, N + M - 1)
	{
	int words = 0, max_words = 0;
	string t;
		
		stringstream ss(s[i]);
		
		while(ss >> t) words ++;
		
//		cout << words << "\n";
		
		f(j, i)
		{
		string t1, t2;
		int temp = 0;
			
			stringstream ss1(s[i]);
			stringstream ss2(s[j]);
			
			while(ss1 >> t1 && ss2 >> t2)
			{
				if(t1 != t2) break;
				
				temp ++;
			}
			
			max_words = max(max_words, temp);
		}
		
		ans += words - max_words;
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
