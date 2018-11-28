#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <sstream>
#include <set>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <bitset>

#define f(i, n)             for(int i = 0; i < n; i++)
#define s(n)				scanf("%d",&n)
#define sl(n) 				scanf("%lld",&n)
#define sf(n) 				scanf("%lf",&n)
#define sc(n)               scanf("%s", &n)    
#define fill(a,v) 			memset(a, v, sizeof a)
#define ull 				unsigned long long
#define ll 					long long
#define bitcount 			__builtin_popcount
#define all(x) 				x.begin(), x.end()
#define pb          		push_back
#define gcd					__gcd
#define inf (int)1e9
#define gc getchar
#define maxn (int)1e6
using namespace std;

inline void ss(int &n)
{
     n = 0;
     char c = gc();
     while(c < 48 || c > 57) c = gc();
     while(c >= 48 && c <= 57) n = (n << 1) + (n << 3) + c - 48, c = gc();
}

struct state
{
	int com, x, y, t;
	state(){}
	state(int C, int X, int Y, int T)
	{
		com = C;
		x = X;
		y = Y;
		t = T;
	}
	
	bool operator < (const state &s) const
	{
		return t < s.t;
	}
};

int a[1005], n;

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("C-small-attempt0.in", "r", stdin);
	//freopen("C-small-attempt0.out", "w", stdout);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	int t;
	s(t);
	for(int test = 1; test <= t; test++)
	{
		s(n);
		int x = 0, sum = 0, m = inf;
		f(i, n)
		{
			s(a[i]);
			x ^= a[i];
			sum += a[i];
			m = min(m, a[i]);
		}
		
		printf("Case #%d: ", test);
		if(x) puts("NO");
		else printf("%d\n", sum - m);
	}
}
