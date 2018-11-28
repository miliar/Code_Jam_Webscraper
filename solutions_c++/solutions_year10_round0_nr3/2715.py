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
#define gc getchar_unlocked
#define maxn (int)1e6
using namespace std;

inline void ss(int &n)
{
     n = 0;
     char c = gc();
     while(c < 48 || c > 57) c = gc();
     while(c >= 48 && c <= 57) n = (n << 1) + (n << 3) + c - 48, c = gc();
}

int r, n, k, a[2010], c[1010], next[1010];
int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	
	int t, p;
	s(t);
	for(int test = 1; test <= t; test++)
	{
		s(r); s(k); s(n);
		f(i, n) {s(a[i]); a[n + i] = a[i];}
		fill(c, 0);
				
		f(i, n)
		{
			int j, lim = 0;
			for(j = i; c[i] + a[j] <= k && lim < n; j++, lim++) c[i] += a[j];
			next[i] = j;
		}
		f(i, n) if(next[i] >= n) next[i] -= n;
		//f(i, n) cout << a[i] << " " << c[i] << " " << next[i] << endl;
		
		ull sum = 0;
		p = 0;
		while(r--)
		{
			sum += c[p];
			p = next[p];
		}
		
		cout << "Case #" << test << ": " << sum << endl;
	}
}
