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

int mem[30];

int main()
{
	//freopen("in.txt", "r", stdin);
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);
	fill(mem, -1);
	int t, n;
	s(t);
	vector <int> v;
	
	for(int test = 1; test <= t; test++)
	{
		s(n);
		if(mem[n] != -1)
		{
			printf("Case #%d: %d\n", test, mem[n]);
			continue;
		}
		
		int lim = 1 << (n - 1), x = 1 << (n - 2), cnt = 0;
		f(i, lim)
		{
			if(!(i & x)) continue;
			v.clear();
			f(j, n - 1) if(i & (1 << j)) v.pb(j + 2);
			
			bool found = 1;
			int rank = n;
			while(rank != 1 && found)
			{
				found = 0;
				f(j, v.size()) if(v[j] == rank) {found = 1; rank = j + 1; break;}
			}
			//if(found) {f(j, v.size()) cout << v[j] << " "; cout << endl;}
			if(found) 
			{
				cnt++;
				if(cnt == 100003) cnt = 0;
			}
		}
		
		printf("Case #%d: %d\n", test, mem[n] = cnt);
	}
}
