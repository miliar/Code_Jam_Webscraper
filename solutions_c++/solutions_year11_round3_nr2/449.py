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

const int mxn = 1000010;
int n, l, C, T;
int d[mxn], dd[mxn], Time[mxn];

int main()
{
	//freopen("in.txt", "r", stdin);
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	
	int t;
	s(t);
	for(int test = 1; test <= t; test++)
	{
		printf("Case #%d: ", test);
		s(l); s(T); s(n); s(C); 
		f(i, C) s(d[i]);
		int p1 = C, p2 = 0;
		while(p1 < n) 
		{
			d[p1++] = d[p2++];
			if(p2 == C) p2 = 0;
		}
		
		dd[0] = d[0];
		//for(int i = 1; i < n; i++) dd[i] = dd[i - 1] + d[i];
		f(i, n) Time[i] = d[i] * 2;
		//f(i, n) cout << Time[i] << " "; cout << endl;
		
		vector <double> dist;
		double ret = 0;
		int p = 0;
		while(p < n && ret <= T) ret += Time[p++];
		
		if(p == n) {printf("%d\n", (int)ret); continue;}
		dist.pb( (ret - T) / 2.0 ); ret = T;
		for(int i = p; i < n; i++) dist.pb(d[i]);
		//f(i, (int)dist.size()) cout << dist[i] << " "; cout << endl;
		sort(all(dist)); 
		//f(i, (int)dist.size()) cout << dist[i] << " "; cout << endl;
		
		for(p = dist.size() - 1; p >= 0 && l > 0; p--, l--) ret += dist[p];
		while(p >= 0) ret += 2 * dist[p--];
		
		cout << (int)ret << endl;
	}
}
