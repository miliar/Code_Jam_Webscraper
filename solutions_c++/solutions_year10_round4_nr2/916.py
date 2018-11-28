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

int M[1 << 11], m[1 << 10], m2[1 << 10], ptr;
int p[11][1 << 11], r;
int mem[11][1 << 11], vis[11][1 << 11], id;

//string s = "", add = "...";

int dp(int R, int M, vector <int> v)
{
	int P = v.size();
	//cout << R << " " << M << " " << P << endl;
	f(i, P) if(v[i] < 0) return inf;
	if(R == r) return 0;
	if(M == P)
	{
		vector <int> v2;
		for(int i = 0; i < P; i += 2) v2.pb( min(v[i], v[i + 1] ) );
		return dp(R + 1, 0, v2);
	}
	
	int &d = mem[R][M];
	if(vis[R][M] == id) return d;
	vis[R][M] = id;
	
	v[M]--;
	//s += add;
	//cout << s << " dont take " << R << " " << M << endl;
	//f(i, P) cout << m[i] << " "; cout << endl;
	d = dp(R, M + 1, v);
	
	v[M]++;
	//cout << s << " take " << R << " " << M << endl;
	d = min(d, dp(R, M + 1, v) + p[R][M]);
	//s = s.substr(0, s.length() - 3);
	
	return d;
}

int main()
{
	//freopen("in.txt", "r", stdin);
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	
	int t;
	s(t);
	vector <int> v;
	
	for(int test = 1; test <= t; test++)
	{
		v.clear();
		s(r);
		int lim = 1 << r;
		f(i, lim) s(M[i]);
		
		f(i, r)
		{
			lim >>= 1;
			f(j, lim) s(p[i][j]);
		}
		
		ptr = 0;
		id++;
		lim = 1 << r;
		for(int i = 0; i < lim; i += 2) v.pb( min(M[i], M[i + 1]) );
		
		int ret = dp(0, 0, v);
		printf("Case #%d: %d\n", test, ret);
	}
}
