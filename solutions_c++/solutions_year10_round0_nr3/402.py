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
const int MAX_N = 10000;



int R, K, N;
int G[MAX_N];
int next_group[MAX_N];
LL people[MAX_N], ans;



void Read()
{
	scanf("%d %d %d", & R, & K, & N);
	
	f(i, N) scanf("%d", & G[i]);
	
	
	
	ans = 0;
	
	f(i, N)
	{
		next_group[i] = - 1;
		people[i] = 0LL;
	}
	
//	system("pause");
}

void Solve()
{
int group, cycle_length;
LL cycle_people;
	
	
	for(group = 0; next_group[group] < 0;)
	{
		next_group[group] = group;
		people[group] = G[group];
		
		for(int i = (group + 1) % N; i != group; i = (i + 1) % N)
		{
			if(people[group] + G[i] <= K)
			{
				people[group] += G[i];
			}
			else
			{
				next_group[group] = i;
				
				break;
			}
		}
		
		R --;
		ans += people[group];
		
		if(R == 0) return;
		
		group = next_group[group];
	}
	
	cycle_length = 1;
	cycle_people = people[group];
	
	for(int i = next_group[group]; i != group; i = next_group[i])
	{
		cycle_length ++;
		cycle_people += people[i];
	}
	
//	fprintf(stderr, "cycle length: %d   cycle people: %lld\n", cycle_length, cycle_people);
	
	int k = R / cycle_length;
	
//	fprintf(stderr, "k: %d\n", k);
	
	ans += LL(k) * LL(cycle_people);
	R -= k * cycle_length;
	
	if(R == 0) return;
	
	for(int i = group; ; i = next_group[i])
	{
		R --;
		ans += people[i];
		
		if(R == 0) return;
	}
	
//	system("pause");
}

void Write(const int test_case)
{
	printf("Case #%d: ", test_case);
	
	printf("%lld\n", ans);
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
