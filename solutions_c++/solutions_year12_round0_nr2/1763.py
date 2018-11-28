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

int n, P, s, a[110];
int mem[110][110], vis[110][110], id;

int dp(int p, int left)
{
	//cout << "DP : " << p << " " << left << endl;
	if(p == n) return 0;//return !left ? 0 : -inf;
	int &m = mem[p][left];
	if(vis[p][left] == id) return m;
	vis[p][left] = id;
	
	m = dp(p + 1, left);
	
	int score = a[p];
	for(int i = 0; i <= score; i++)
		for(int j = i; j <= i + 2; j++)
		{
			int k = score - i - j;
			if(k < j) break;
			if(k - i > 2) continue;
			
			if(k >= P)
			{
				//cout << "\t" << p << " " << left << " : " << i << " + " << j << " + " << k << " = " << score << endl;
				if(j - i < 2 && k - i < 2) m = max( m, dp(p + 1, left) + 1 );
				else if(left > 0) m = max( m, dp(p + 1, left - 1) + 1 );
			}
		}
	
	return m;
}

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("B-small-attempt1.in", "r", stdin);
	//freopen("B-small-attempt1.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	
	int t;
	s(t);
	for(int test = 1; test <= t; test++)
	{
		s(n); s(s); s(P); 
		f(i, n) s(a[i]);
		id++;
		
		printf( "Case #%d: %d\n", test, dp(0, s) );
	}
}
