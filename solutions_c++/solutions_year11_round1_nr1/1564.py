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

bool sv[110];

int main()
{
	//freopen("in.txt", "r", stdin);
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	
	sv[0] = sv[1] = 1;
	for(int i = 2; i < 11; i++)
		if(!sv[i])
			for(int j = i * i; j < 110; j += i)
				sv[j] = 1;
	
	int t;
	ll pd, pg, n;
	s(t);
	for(int test = 1; test <= t; test++)
	{
		printf("Case #%d: ", test);
		cin >> n >> pd >> pg;
		
		if(!pd)
		{
			puts(pg != 100 ? "Possible" : "Broken");
			continue;
		}
		
		if(!pg)
		{
			puts("Broken");
			continue;
		}
		
		ll wd = pd / gcd(pd, 100ll);
		ll d = (100 * wd) / pd;
		//cout << wd << " " << d << endl;
		
		if( d > n || (pd != 100 && pg == 100) )
		{
			puts("Broken");
			continue;
		}
		
		for(int i = 2; i < wd; i++)
			while(wd % i == 0) wd /= i;
		
		if(pg > wd)
		{
			puts("Possible");
			continue;
		}
		
		while(pg > 1 && pg % 2 == 0) pg /= 2;
		while(pg > 1 && pg % 5 == 0) pg /= 5;
		if(wd % pg != 0) puts("Broken"); 
		else puts("Possible");
	}
}
