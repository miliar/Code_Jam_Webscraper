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

char a[55][55];
int n, m;

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int t;
	s(t);
	for(int test = 1; test <= t; test++)
	{
		printf("Case #%d:\n", test);
		s(n); s(m);
		f(i, n) cin >> a[i];
		
		int ok = 1;
		f(i, n)
			f(j, m)
				if(a[i][j] == '#')
				{
					if(i == n - 1 || j == m - 1) {ok = 0; i = n; break;}
					if(a[i + 1][j] != '#' || a[i][j + 1] != '#' || a[i + 1][j + 1] != '#') {ok = 0; i = n; break;}
					a[i][j] = a[i + 1][j + 1] = '/';
					a[i + 1][j] = a[i][j + 1] = '\\';
				}
		if(!ok) puts("Impossible");
		else
			f(i, n) cout << a[i] << endl;
	}
}
