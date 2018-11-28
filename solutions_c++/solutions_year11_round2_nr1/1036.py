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

char a[110][110];
int n;
double wp[110], owp[110], oowp[110];

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
		s(n);
		f(i, n) cin >> a[i];
		
		f(i, n)
		{
			int tot = 0, w = 0;
			f(j, n)
				if(a[i][j] != '.')
				{
					tot++;
					if(a[i][j] == '1') w++;
				}
			wp[i] = (1. * w) / tot;
		}
		
		f(i, n)
		{
			double x = 0;
			int c = 0;
			f(j, n)
				if(a[i][j] != '.')
				{
					c++;
					int tot = 0, w = 0;
					f(k, n)
					{
						if(k == i) continue;
						if(a[j][k] != '.')
						{
							tot++;
							if(a[j][k] == '1') w++;
						}
					}
					
					x += (1. * w) / tot;
				}
				owp[i] = x / c;
		}
		
		f(i, n)
		{
			double x = 0;
			int c = 0;
			f(j, n)
				if(a[i][j] != '.')
				{
					c++;
					x += owp[j];
				}
			oowp[i] = x / c;
		}
		//puts("WP");f(i, n) printf("%d : %.6lf\n", i, wp[i]);
		//puts("OWP");f(i, n) printf("%d : %.6lf\n", i, owp[i]);
		//puts("OOWP");f(i, n) printf("%d : %.6lf\n", i, oowp[i]);
		
		f(i, n)
		{
			double x = wp[i] / 4 + owp[i] / 2 + oowp[i] / 4;
			printf("%.6lf\n", x);
		}
	}
}
